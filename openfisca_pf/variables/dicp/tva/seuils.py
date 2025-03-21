# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    GroupPopulation,
    ParameterNode,
    Period,
    YEAR,
    Variable
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Pays


class seuil_tva_regime_franchise_en_base(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "En dessous de ce seuil, l'entreprise est éligible à la franchise en base"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]
    unit = units.XPF

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.seuils.regime.franchise_en_base


class seuil_tva_regime_simplifiee_activite_commerciale(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "En dessous de ce seuil, l'entreprise dont l'activité est commerciale est éligible au régime simplifié"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]
    unit = units.XPF

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.seuils.regime.simplifie.activite_commerciale


class seuil_tva_regime_simplifiee_activite_prestation(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "En dessous de ce seuil, l'entreprise dont l'activité est de la prestation est éligible au régime simplifié"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]
    unit = units.XPF

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.seuils.regime.simplifie.activite_prestation


class seuil_tva_regime_reel_trimestriel(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = "En dessous de ce seuil, l'entreprise est éligible au régime réel trimestriel"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot",
        "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"
        ]
    unit = units.XPF

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.tva.seuils.regime.reel_trimestriel
