# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Enum,
    not_,
    ParameterNode,
    Period,
    Population,
    YEAR,
    Variable,
    where
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Personne
from openfisca_pf.enums.common import OuiNon


class redevable_tva_franchise_en_base(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://www.impot-polynesie.gov.pf/code/7-chap-vii-regimes-dimposition"
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period)
        pas_option_tva_regime_simplifie = (personne('option_tva_regime_simplifie', period) == OuiNon.N) \
            * personne('option_tva_regime_simplifie_possible', period)
        pas_option_tva_regime_reel_trimestriel = (personne('option_tva_regime_reel_trimestriel', period) == OuiNon.N) \
            * personne('option_tva_regime_reel_trimestriel_possible', period)
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period) == OuiNon.N) \
            * personne('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_franchise_en_base = parameters(period).dicp.tva.seuils.regime.franchise_en_base
        ca_inferieur_a_seuil = ca_total < seuil_tva_franchise_en_base
        return ca_inferieur_a_seuil * pas_option_tva_regime_simplifie * pas_option_tva_regime_reel_trimestriel * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_simplifie(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://www.impot-polynesie.gov.pf/code/7-chap-vii-regimes-dimposition"
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period)
        pas_redevable_tva_franchise_en_base = not_(personne('redevable_tva_franchise_en_base', period))
        pas_option_tva_regime_reel_trimestriel = (personne('option_tva_regime_reel_trimestriel', period) == OuiNon.N) \
            * personne('option_tva_regime_reel_trimestriel_possible', period)
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period) == OuiNon.N) \
            * personne('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_regime_simplifiee_activite_commerciale = parameters(period).dicp.tva.seuils.regime.simplifie.activite_commerciale
        seuil_tva_regime_simplifiee_activite_prestation = parameters(period).dicp.tva.seuils.regime.simplifie.activite_prestation
        ca_inferieur_a_seuil_activite_commerciale = ca_total < seuil_tva_regime_simplifiee_activite_commerciale
        ca_inferieur_a_seuil_activite_prestations = ca_total < seuil_tva_regime_simplifiee_activite_prestation
        activite_commerciale = personne('activite_commerciale', period)
        inferieur_seuil = where(activite_commerciale, ca_inferieur_a_seuil_activite_commerciale, ca_inferieur_a_seuil_activite_prestations)
        return inferieur_seuil * pas_redevable_tva_franchise_en_base * pas_option_tva_regime_reel_trimestriel * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_reel_trimestriel(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://www.impot-polynesie.gov.pf/code/7-chap-vii-regimes-dimposition"
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period)
        pas_redevable_tva_franchise_en_base = not_(personne('redevable_tva_franchise_en_base', period))
        pas_redevable_tva_regime_simplifie = not_(personne('redevable_tva_regime_simplifie', period))
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period) == OuiNon.N) \
            * personne('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_regime_reel_trimestriel = parameters(period).dicp.tva.seuils.regime.reel_trimestriel
        ca_inferieur_seuil = ca_total < seuil_tva_regime_reel_trimestriel
        return ca_inferieur_seuil * pas_redevable_tva_franchise_en_base * pas_redevable_tva_regime_simplifie * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_reel_mensuel(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la franchise en base de TVA"
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevable_tva_franchise_en_base = personne('redevable_tva_franchise_en_base', period)
        redevable_tva_regime_simplifie = personne('redevable_tva_regime_simplifie', period)
        redevable_tva_regime_reel_trimestriel = personne('redevable_tva_regime_reel_trimestriel', period)
        return not_(redevable_tva_regime_reel_trimestriel) * not_(redevable_tva_franchise_en_base) * not_(redevable_tva_regime_simplifie)


class option_tva_regime_simplifie_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "L'entreprise peut opter pour le régime simplifié de TVA"
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period)
        seuil_tva_franchise_en_base = parameters(period).dicp.tva.seuils.regime.franchise_en_base
        ca_inferieur_a_seuil = ca_total < seuil_tva_franchise_en_base
        return ca_inferieur_a_seuil


class option_tva_regime_simplifie(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = "Défini si l'entreprise à opté pour le régime simplifié alors qu'elle est éligible à la franchise en base"
    unit = units.BOOLEAN


class option_tva_regime_reel_trimestriel_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "L'entreprise peut opter pour le régime réel trimestriel de TVA"
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period)
        seuil_tva_regime_simplifiee_activite_commerciale = parameters(period).dicp.tva.seuils.regime.simplifie.activite_commerciale
        seuil_tva_regime_simplifiee_activite_prestation = parameters(period).dicp.tva.seuils.regime.simplifie.activite_prestation
        activite_commerciale = personne('activite_commerciale', period)
        ca_inferieur_a_seuil_activite_commerciale = ca_total < seuil_tva_regime_simplifiee_activite_commerciale
        ca_inferieur_a_seuil_activite_prestations = ca_total < seuil_tva_regime_simplifiee_activite_prestation
        inferieur_seuil = where(activite_commerciale, ca_inferieur_a_seuil_activite_commerciale, ca_inferieur_a_seuil_activite_prestations)
        return inferieur_seuil


class option_tva_regime_reel_trimestriel(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = "Défini si l'entreprise à opté pour le régime réel trimestriel alors qu'elle est éligible à un régime plus favorable"
    unit = units.BOOLEAN


class option_tva_regime_reel_mensuel_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "L'entreprise peut opter pour le régime réel mensuel de TVA"
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period)
        seuil_tva_regime_reel_trimestriel = parameters(period).dicp.tva.seuils.regime.reel_trimestriel
        ca_inferieur_seuil = ca_total < seuil_tva_regime_reel_trimestriel
        return ca_inferieur_seuil


class option_tva_regime_reel_mensuel(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = "Défini si l'entreprise à opté pour le régime réel mensuel alors qu'elle est éligible à un régime plus favorable"
    unit = units.BOOLEAN
