# -*- coding: utf-8 -*-

# This file defines the base enum needed by our legislation.
from openfisca_core.model_api import *
import numpy
from openfisca_core.taxscales import MarginalRateTaxScale


class TypePersonne(Enum):
    P = u'Personne physique'
    M = u'Personne morale'


class OuiNon(Enum):
    O = u'Oui'
    N = u'Non'


# This function round up if result is 0.5 so for ex 1.5 => 2, 1.6 => 2 but 1.4 => 1
def arrondiSup(valeur):
    return numpy.rint(numpy.nextafter(valeur, valeur + 1))


# This function round down if result is 0.5 so for ex 1.5 => 1, 1.6 => 2 and 1.4 => 1
def arrondiInf(valeur):
    return numpy.rint(numpy.nextafter(valeur, valeur - 1))


def creerBaremeIT(entreprise, period, type):
    nbTranches = entreprise.pays(f'nombre_tranches_it_{type}', period)[0]
    bareme = MarginalRateTaxScale(name = 'Bareme perso')
    for tranche in range(1, nbTranches + 1):
        bareme.add_bracket(entreprise.pays(f'seuil_it_{type}_tranche_{tranche}', period)[0], entreprise.pays(f'taux_it_{type}_tranche_{tranche}', period)[0])
    return bareme
