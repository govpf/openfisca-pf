# -*- coding: utf-8 -*-

from openfisca_core.model_api import *
from openfisca_pf.entities import *


class base_imposable_tva_taux_reduit(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imposable de la TVA à taux réduit"
    unit = 'currency-XPF'
    reference = "https://www.impot-polynesie.gov.pf/code/3-chap-iii-taux"


class base_imposable_tva_taux_intermediaire(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imposable de la TVA à taux intermediaire"
    unit = 'currency-XPF'
    reference = "https://www.impot-polynesie.gov.pf/code/3-chap-iii-taux"


class base_imposable_tva_taux_normal(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imposable de la TVA à taux normal"
    unit = 'currency-XPF'
    reference = "https://www.impot-polynesie.gov.pf/code/3-chap-iii-taux"
