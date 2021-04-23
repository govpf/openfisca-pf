# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA exigible: \n\n#tva_exigible = #tva_due_taux_reduit + #tva_due_taux_intermediaire + #tva_due_taux_normal + #regularisation_tva_exigible"

    def formula(personne, period, parameters):
        tva_due_taux_reduit = personne(f'tva_due_taux_reduit', period)
        tva_due_taux_intermediaire = personne(f'tva_due_taux_intermediaire', period)
        tva_due_taux_normal = personne(f'tva_due_taux_normal', period)
        regularisation_tva_exigible = personne(f'regularisation_tva_exigible', period)
        return tva_due_taux_reduit + tva_due_taux_intermediaire + tva_due_taux_normal + regularisation_tva_exigible


class regularisation_tva_exigible(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant à appliquer pour régulariser le montant de TVA exigible"
