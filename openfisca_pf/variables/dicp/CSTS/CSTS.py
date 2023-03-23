# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne
import openfisca_pf.constants.DICP.references_csts as references


class cst_s_due_totale_par_employes(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Sum of the taxes paid by a household"
    reference = [references.REFERENCE_CODE_LP_TAUX_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_TAUX]
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        cst_s_i = personne.members('cst_s', period)
        return personne.sum(cst_s_i)


class cst_s_due_totale(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"CST-S due par l'entreprise sur l'ensemble des salaires déclarés par tranche"
    reference = [references.REFERENCE_CODE_LP_TAUX_CSTS, references.REFERENCE_LIEN_CODE, references.REFERENCE_LIEN_TAUX]
    unit = 'currency-XPF'

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        # print(parameters(period).dicp.cst_s.taux.rates[0])
        value = 0
        for i, taux in enumerate(parameters(period).dicp.cst_s.taux.rates):
            value += personne('cst_s_due_tranche_' + str(i + 1), period)
        return value
