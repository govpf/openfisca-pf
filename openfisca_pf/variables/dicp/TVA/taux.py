# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class taux_tva_reduit(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de TVA réduit"
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.taux.reduit)


class taux_tva_intermediaire(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de TVA intermédiaire"
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.taux.intermediaire)


class taux_tva_normal(Variable):
    value_type = float
    entity = Pays
    definition_period = MONTH
    label = u"Taux de TVA réduit"
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.taux.normal)