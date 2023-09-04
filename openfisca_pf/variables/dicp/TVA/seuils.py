# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class seuil_tva_franchise_en_base(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"En dessous de ce seuil, l'entreprise est éligible à la franchise en base"
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.seuils.franchise_en_base)


class seuil_tva_regime_simplifiee_activite_commerciale(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"En dessous de ce seuil, l'entreprise dont l'activité est commerciale est éligible au régime simplifié"
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.seuils.regime_simplifie.activite_commerciale)


class seuil_tva_regime_simplifiee_activite_prestation(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"En dessous de ce seuil, l'entreprise dont l'activité est de la prestation est éligible au régime simplifié"
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.seuils.regime_simplifie.activite_prestation)


class seuil_tva_regime_reel_trimestriel(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"En dessous de ce seuil, l'entreprise est éligible au régime réel trimestriel"
    # reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return (parameters(period).dicp.tva.seuils.regime_reel_trimestriel)
