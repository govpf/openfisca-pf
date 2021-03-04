# -*- coding: utf-8 -*-

# This file defines the base enum needed by our legislation.
from openfisca_core.model_api import *
import numpy
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


# This function round up if result is 0.5 so for ex 1.5 => 2, 1.6 => 2 but 1.4 => 1
def arrondiSup(valeur):
    return numpy.rint(numpy.nextafter(valeur, valeur + 1))


# This function round down if result is 0.5 so for ex 1.5 => 1, 1.6 => 2 and 1.4 => 1
def arrondiInf(valeur):
    return numpy.rint(numpy.nextafter(valeur, valeur - 1))


def creerBaremeIT(entreprise, period, type):
    nbTranches = entreprise.pays(f'nombre_tranches_it_{type}', period)[0]
    bareme = MarginalRateTaxScale(name = 'Bareme IT')
    for tranche in range(1, nbTranches + 1):
        bareme.add_bracket(entreprise.pays(f'seuil_it_{type}_tranche_{tranche}', period)[0], entreprise.pays(f'taux_it_{type}_tranche_{tranche}', period)[0])
    return bareme


def creerBaremeCSTNS(entreprise, period, type):
    nbTranches = entreprise.pays(f'nombre_tranches_cstns_{type}', period)[0]
    bareme = MarginalRateTaxScale(name = 'Bareme CSTNS')
    for tranche in range(1, nbTranches + 1):
        bareme.add_bracket(entreprise.pays(f'seuil_cstns_{type}_tranche_{tranche}', period)[0], entreprise.pays(f'taux_cstns_{type}_tranche_{tranche}', period)[0])
    return bareme


def creerBareme(entreprise, period, impot, type):
    nbTranches = entreprise.pays(f'nombre_tranches_{impot}_{type}', period)[0]
    bareme = MarginalRateTaxScale(name = 'Bareme CSTNS')
    for tranche in range(1, nbTranches + 1):
        bareme.add_bracket(entreprise.pays(f'seuil_{impot}_{type}_tranche_{tranche}', period)[0], entreprise.pays(f'taux_{impot}_{type}_tranche_{tranche}', period)[0])
    return bareme


def calculerBaseImposableVentesTranche(entreprise, period, tranche, impot):
    nbTranches = entreprise.pays(f'nombre_tranches_{impot}_ventes', period)[0]
    if tranche > nbTranches:
        return 0
    seuil_tranche_inferieure = entreprise.pays(f'seuil_{impot}_ventes_tranche_{tranche}', period)
    ca = entreprise(f'base_imposable_{impot}_ventes', period)
    if tranche == nbTranches:
        valeur = (select(
            [ca <= seuil_tranche_inferieure, ca > seuil_tranche_inferieure],
            [0, ca - seuil_tranche_inferieure],
            ))
    else:
        seuil_tranche_superieure = entreprise.pays(f'seuil_{impot}_ventes_tranche_{tranche + 1}', period)
        valeur = (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))
    return valeur


def calculerBaseImposablePrestationsTranche(entreprise, period, tranche, impot):
    nbTranches = entreprise.pays(f'nombre_tranches_{impot}_prestations', period)[0]
    if tranche > nbTranches:
        return 0
    seuil_tranche_inferieure = entreprise.pays(f'seuil_{impot}_prestations_tranche_{tranche}', period)
    ca = entreprise(f'base_imposable_{impot}_prestations', period) + entreprise(f'base_imposable_{impot}_ventes', period) / 4
    if tranche == nbTranches:
        caVenteTranche = 0
        for i in range(tranche, entreprise.pays(f'nombre_tranches_{impot}_ventes', period)[0] + 1):
            caVenteTranche += entreprise(f'base_imposable_{impot}_ventes_tranche_{i}', period) / 4
        valeur = (select(
            [ca <= seuil_tranche_inferieure, ca > seuil_tranche_inferieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche],
            ))
    else:
        caVenteTranche = entreprise(f'base_imposable_{impot}_ventes_tranche_{tranche}', period) / 4
        seuil_tranche_superieure = entreprise.pays(f'seuil_{impot}_prestations_tranche_{tranche + 1}', period)
        valeur = (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))
    return valeur
