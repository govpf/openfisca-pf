# -*- coding: utf-8 -*-

from openfisca_pf.constants import units
from openfisca_pf.entities import *
from openfisca_pf.base import *


class regularisation_autre_tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant à appliquer pour régulariser le montant de TVA exigible"
    unit = units.XPF
    default_value = 0


class sous_total_tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = units.XPF
    label = u"Montant de TVA exigible: \n\n#tva_exigible = #tva_due_taux_reduit + #tva_due_taux_intermediaire + #tva_due_taux_normal + #regularisation_tva_exigible"

    def formula(personne, period, parameters):
        tva_due_taux_reduit = personne('tva_due_taux_reduit', period)
        tva_due_taux_intermediaire = personne('tva_due_taux_intermediaire', period)
        tva_due_taux_normal = personne('tva_due_taux_normal', period)
        return tva_due_taux_reduit + tva_due_taux_intermediaire + tva_due_taux_normal


class tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = units.XPF
    label = u"Montant de TVA exigible: \n\n#tva_exigible = #tva_due_taux_reduit + #tva_due_taux_intermediaire + #tva_due_taux_normal + #regularisation_tva_exigible"

    def formula(personne, period, parameters):
        sous_total_tva_exigible = personne('sous_total_tva_exigible', period)
        regularisation_autre_tva_exigible = personne('regularisation_autre_tva_exigible', period)
        return sous_total_tva_exigible + regularisation_autre_tva_exigible
