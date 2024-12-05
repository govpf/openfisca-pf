# -*- coding: utf-8 -*-

# This file defines the base enum needed by our legislation.

import numpy
from openfisca_core.model_api import Enum
from openfisca_core.taxscales import MarginalRateTaxScale


class TypePersonne(Enum):
    P = u'Personne physique'
    M = u'Personne morale'


class TypeSociete(Enum):
    EI = u'Entreprise Individuelle'
    EURL = u'Entreprise Unipersonnelle à Responsabilité Limitée'
    SARL = u'Société à Responsabilité Limitée'
    SNC = u'Société en Nom Collectif'
    SA = u'Société Anonyme'
    SAS = u'Société par Action Simplifiée'
    SCI = u'Société Civile Immobilière'


class OuiNon(Enum):
    O = u'Oui'
    N = u'Non'


class TypeContrat(Enum):
    Aucun = u'Aucun contrat'
    CDI = u'Contrat à durée indéterminée'
    CDD = u'Contrat à durée déterminée'
    Extras = u'Contrat d\'extras'


class RegimeCPS(Enum):
    NonAffilie = u'La personne n\'est pas affiliée'
    RSPF = u'Régime de solidarité'
    RNS = u'Régime des non salariés'
    RS = u'Régime des salariés'


# This function round up if result is 0.5 so for ex 1.5 => 2, 1.6 => 2 but 1.4 => 1
def arrondiSup(valeur):
    return numpy.rint(numpy.nextafter(valeur, valeur + 1))


# This function round down if result is 0.5 so for ex 1.5 => 1, 1.6 => 2 and 1.4 => 1
def arrondiInf(valeur):
    return numpy.rint(numpy.nextafter(valeur, valeur - 1))


# Calculations are grouped per date, so we know the parameters for each entry is the same, thus we can create only one scale for all of them
def creerBareme(personne, period, impot, type):
    nbTranches = personne.pays(f'nombre_tranches_{impot}_{type}', period)[0]
    bareme = MarginalRateTaxScale(name = 'Bareme custom')
    for tranche in range(1, nbTranches + 1):
        bareme.add_bracket(personne.pays(f'seuil_{impot}_{type}_tranche_{tranche}', period)[0], personne.pays(f'taux_{impot}_{type}_tranche_{tranche}', period)[0])
    return bareme


def calculerBaseImposableVentesTranche(personne, period, tranche, impot):
    nbTranches = personne.pays(f'nombre_tranches_{impot}_ventes', period)[0]
    if tranche > nbTranches:
        return 0
    seuil_tranche_inferieure = personne.pays(f'seuil_{impot}_ventes_tranche_{tranche}', period)
    ca = personne(f'base_imposable_{impot}_ventes', period)
    if tranche == nbTranches:
        valeur = (numpy.select(
            [ca <= seuil_tranche_inferieure, ca > seuil_tranche_inferieure],
            [0, ca - seuil_tranche_inferieure],
            ))
    else:
        seuil_tranche_superieure = personne.pays(f'seuil_{impot}_ventes_tranche_{tranche + 1}', period)
        valeur = (numpy.select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))
    return valeur


def calculerBaseImposablePrestationsTranche(personne, period, tranche, impot):
    nbTranches = personne.pays(f'nombre_tranches_{impot}_prestations', period)[0]
    if tranche > nbTranches:
        return 0
    seuil_tranche_inferieure = personne.pays(f'seuil_{impot}_prestations_tranche_{tranche}', period)
    ca = personne(f'base_imposable_{impot}_prestations', period) + personne(f'base_imposable_{impot}_ventes', period) / 4
    if tranche == nbTranches:
        caVenteTranche = 0
        for i in range(tranche, personne.pays(f'nombre_tranches_{impot}_ventes', period)[0] + 1):
            caVenteTranche += personne(f'base_imposable_{impot}_ventes_tranche_{i}', period) / 4
        valeur = (numpy.select(
            [ca <= seuil_tranche_inferieure, ca > seuil_tranche_inferieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche],
            ))
    else:
        caVenteTranche = personne(f'base_imposable_{impot}_ventes_tranche_{tranche}', period) / 4
        seuil_tranche_superieure = personne.pays(f'seuil_{impot}_prestations_tranche_{tranche + 1}', period)
        valeur = (numpy.select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))
    return valeur


# This function aims at getting a source variable using the aggregation of a prefix and another variable
# variable = [variable 1, variable 2, variable3]
# prefix = blabla
# return [source(blablavariable1), source(blablavariable2), source(blablavariable3)]
def aggregateVariables(source, period, prefix, variable):
    returnValue = []
    index = 0
    for item in variable:
        value = source(prefix + item, period)[index]
        returnValue.append(value)
        index = index + 1
    return numpy.array(returnValue)
