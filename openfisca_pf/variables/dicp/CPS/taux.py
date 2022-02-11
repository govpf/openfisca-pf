# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class taux_cps(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de CPS"
    set_input = set_input_divide_by_period
    unit = '/1'
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        taux_annee = pays('taux_cps_annee', period.this_year)
        return where(taux_annee, taux_annee, parameters(period).dicp.cps.taux)


class taux_cps_annee(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de CPS défini annuellement"
    unit = '/1'
    set_input = set_input_divide_by_period
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return (parameters(period).dicp.cps.taux)

