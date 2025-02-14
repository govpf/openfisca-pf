# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    Enum,
    OuiNon,
    not_,
    Parameters,
    Period,
    YEAR,
    Variable,
    where
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Pays, Personne


class redevable_tva_franchise_en_base(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://www.impot-polynesie.gov.pf/code/7-chap-vii-regimes-dimposition"
    unit = units.BOOLEAN

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period, parameters)
        pas_option_tva_regime_simplifie = (personne('option_tva_regime_simplifie', period, parameters) == OuiNon.N) * personne('option_tva_regime_simplifie_possible', period, parameters)
        pas_option_tva_regime_reel_trimestriel = (personne('option_tva_regime_reel_trimestriel', period, parameters) == OuiNon.N) * personne('option_tva_regime_reel_trimestriel_possible', period, parameters)
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period, parameters) == OuiNon.N) * personne('option_tva_regime_reel_mensuel_possible', period, parameters)
        seuil_tva_franchise_en_base = personne.pays('seuil_tva_franchise_en_base', period, parameters)
        ca_inferieur_a_seuil = ca_total < seuil_tva_franchise_en_base
        return ca_inferieur_a_seuil * pas_option_tva_regime_simplifie * pas_option_tva_regime_reel_trimestriel * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_simplifie(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://www.impot-polynesie.gov.pf/code/7-chap-vii-regimes-dimposition"
    unit = units.BOOLEAN

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period, parameters)
        pas_redevable_tva_franchise_en_base = not_(personne('redevable_tva_franchise_en_base', period, parameters))
        pas_option_tva_regime_reel_trimestriel = (personne('option_tva_regime_reel_trimestriel', period, parameters) == OuiNon.N) * personne('option_tva_regime_reel_trimestriel_possible', period, parameters)
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period, parameters) == OuiNon.N) * personne('option_tva_regime_reel_mensuel_possible', period, parameters)
        seuil_tva_regime_simplifiee_activite_commerciale = personne.pays('seuil_tva_regime_simplifiee_activite_commerciale', period, parameters)
        seuil_tva_regime_simplifiee_activite_prestation = personne.pays('seuil_tva_regime_simplifiee_activite_prestation', period, parameters)
        ca_inferieur_a_seuil_activite_commerciale = ca_total < seuil_tva_regime_simplifiee_activite_commerciale
        ca_inferieur_a_seuil_activite_prestations = ca_total < seuil_tva_regime_simplifiee_activite_prestation
        activite_commerciale = personne('activite_commerciale', period, parameters)
        inferieur_seuil = where(activite_commerciale, ca_inferieur_a_seuil_activite_commerciale, ca_inferieur_a_seuil_activite_prestations)
        return inferieur_seuil * pas_redevable_tva_franchise_en_base * pas_option_tva_regime_reel_trimestriel * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_reel_trimestriel(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://www.impot-polynesie.gov.pf/code/7-chap-vii-regimes-dimposition"
    unit = units.BOOLEAN

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period, parameters)
        pas_redevable_tva_franchise_en_base = not_(personne('redevable_tva_franchise_en_base', period, parameters))
        pas_redevable_tva_regime_simplifie = not_(personne('redevable_tva_regime_simplifie', period, parameters))
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period, parameters) == OuiNon.N) * personne('option_tva_regime_reel_mensuel_possible', period, parameters)
        seuil_tva_regime_reel_trimestriel = personne.pays('seuil_tva_regime_reel_trimestriel', period, parameters)
        ca_inferieur_seuil = ca_total < seuil_tva_regime_reel_trimestriel
        return ca_inferieur_seuil * pas_redevable_tva_franchise_en_base * pas_redevable_tva_regime_simplifie * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_reel_mensuel(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la franchise en base de TVA"
    unit = units.BOOLEAN

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        redevable_tva_franchise_en_base = personne('redevable_tva_franchise_en_base', period, parameters)
        redevable_tva_regime_simplifie = personne('redevable_tva_regime_simplifie', period, parameters)
        redevable_tva_regime_reel_trimestriel = personne('redevable_tva_regime_reel_trimestriel', period, parameters)
        return not_(redevable_tva_regime_reel_trimestriel) * not_(redevable_tva_franchise_en_base) * not_(redevable_tva_regime_simplifie)


class option_tva_regime_simplifie_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "L'entreprise peut opter pour le régime simplifié de TVA"
    unit = units.BOOLEAN

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period, parameters)
        seuil_tva_franchise_en_base = personne.pays('seuil_tva_franchise_en_base', period, parameters)
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

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period)
        seuil_tva_regime_simplifiee_activite_commerciale = personne.pays('seuil_tva_regime_simplifiee_activite_commerciale', period, parameters)
        seuil_tva_regime_simplifiee_activite_prestation = personne.pays('seuil_tva_regime_simplifiee_activite_prestation', period, parameters)
        activite_commerciale = personne('activite_commerciale', period, parameters)
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

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        ca_total = personne('chiffre_affaire_total', period, parameters)
        seuil_tva_regime_reel_trimestriel = personne.pays('seuil_tva_regime_reel_trimestriel', period, parameters)
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


class nombre_entreprises_redevables_franchise_base_TVA_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables de la franchise en base de TVA"
    unit = units.INTEGER

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        redevable_tva_franchise_en_base = pays.members('redevable_tva_franchise_en_base', period, parameters)
        return pays.sum(redevable_tva_franchise_en_base * 1)


class nombre_entreprises_redevables_regime_simplifie_TVA_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables du régime simplfié de TVA"
    unit = units.INTEGER

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        redevable_tva_regime_simplifie = pays.members('redevable_tva_regime_simplifie', period, parameters)
        return pays.sum(redevable_tva_regime_simplifie * 1)


class nombre_entreprises_redevables_regime_reel_trimestriel_TVA_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables du régime réel trimestriel de TVA"
    unit = units.INTEGER

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        redevable_tva_regime_reel_trimestriel = pays.members('redevable_tva_regime_reel_trimestriel', period, parameters)
        return pays.sum(redevable_tva_regime_reel_trimestriel * 1)


class nombre_entreprises_redevables_regime_reel_mensuel_TVA_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = "Nombre d'entreprises du pays redevables du régime réel trimestriel de TVA"
    unit = units.INTEGER

    def formula(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        redevable_tva_regime_reel_mensuel = pays.members('redevable_tva_regime_reel_mensuel', period, parameters)
        return pays.sum(redevable_tva_regime_reel_mensuel * 1)
