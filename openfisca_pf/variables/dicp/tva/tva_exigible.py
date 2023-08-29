# -*- coding: utf-8 -*-

from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    unit = 'currency-XPF'
    label = u"Montant de TVA exigible: \n\n#tva_exigible = #tva_due_taux_reduit + #tva_due_taux_intermediaire + #tva_due_taux_normal + #regularisation_tva_exigible"

    def formula(personne, period, parameters):
        tva_due_taux_reduit = personne(f'tva_due_taux_reduit', period)
        tva_due_taux_intermediaire = personne(f'tva_due_taux_intermediaire', period)
        tva_due_taux_normal = personne(f'tva_due_taux_normal', period)
        regularisation_autre_tva_exigible = personne(f'regularisation_autre_tva_exigible', period)
        return tva_due_taux_reduit + tva_due_taux_intermediaire + tva_due_taux_normal + regularisation_autre_tva_exigible


class regularisation_autre_tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant à appliquer pour régulariser le montant de TVA exigible"
    unit = 'currency-XPF'
