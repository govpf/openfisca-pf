# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class redevable_tva_franchise_en_base(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca_total = entreprise('chiffre_affaire_total', period)
        pas_option_tva_regime_simplifie = (entreprise('option_tva_regime_simplifie', period) == OuiNon.N) * entreprise('option_tva_regime_simplifie_possible', period)
        pas_option_tva_regime_reel_trimestriel = (entreprise('option_tva_regime_reel_trimestriel', period) == OuiNon.N) * entreprise('option_tva_regime_reel_trimestriel_possible', period)
        pas_option_tva_regime_reel_mensuel = (entreprise('option_tva_regime_reel_mensuel', period) == OuiNon.N) * entreprise('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_franchise_en_base = entreprise.pays('seuil_tva_franchise_en_base', period)
        ca_inferieur_a_seuil = ca_total < seuil_tva_franchise_en_base
        return ca_inferieur_a_seuil * pas_option_tva_regime_simplifie * pas_option_tva_regime_reel_trimestriel * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_simplifie(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca_total = entreprise('chiffre_affaire_total', period)
        pas_redevable_tva_franchise_en_base = not_(entreprise('redevable_tva_franchise_en_base', period))
        pas_option_tva_regime_reel_trimestriel = (entreprise('option_tva_regime_reel_trimestriel', period) == OuiNon.N) * entreprise('option_tva_regime_reel_trimestriel_possible', period)
        pas_option_tva_regime_reel_mensuel = (entreprise('option_tva_regime_reel_mensuel', period) == OuiNon.N) * entreprise('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_regime_simplifiee_activite_commerciale = entreprise.pays('seuil_tva_regime_simplifiee_activite_commerciale', period)
        seuil_tva_regime_simplifiee_activite_prestation = entreprise.pays('seuil_tva_regime_simplifiee_activite_prestation', period)
        ca_inferieur_a_seuil_activite_commerciale = ca_total < seuil_tva_regime_simplifiee_activite_commerciale
        ca_inferieur_a_seuil_activite_prestations = ca_total < seuil_tva_regime_simplifiee_activite_prestation
        activite_commerciale = entreprise('activite_commerciale', period)
        inferieur_seuil = where(activite_commerciale, ca_inferieur_a_seuil_activite_commerciale, ca_inferieur_a_seuil_activite_prestations)
        return inferieur_seuil * pas_redevable_tva_franchise_en_base * pas_option_tva_regime_reel_trimestriel * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_reel_trimestriel(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca_total = entreprise('chiffre_affaire_total', period)
        pas_redevable_tva_franchise_en_base = not_(entreprise('redevable_tva_franchise_en_base', period))
        pas_redevable_tva_regime_simplifie = not_(entreprise('redevable_tva_regime_simplifie', period))
        pas_option_tva_regime_reel_mensuel = (entreprise('option_tva_regime_reel_mensuel', period) == OuiNon.N) * entreprise('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_regime_reel_trimestriel = entreprise.pays('seuil_tva_regime_reel_trimestriel', period)
        ca_inferieur_seuil = ca_total < seuil_tva_regime_reel_trimestriel
        return ca_inferieur_seuil * pas_redevable_tva_franchise_en_base * pas_redevable_tva_regime_simplifie * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_reel_mensuel(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        redevable_tva_franchise_en_base = entreprise('redevable_tva_franchise_en_base', period)
        redevable_tva_regime_simplifie = entreprise('redevable_tva_regime_simplifie', period)
        redevable_tva_regime_reel_trimestriel = entreprise('redevable_tva_regime_reel_trimestriel', period)
        return not_(redevable_tva_regime_reel_trimestriel) * not_(redevable_tva_franchise_en_base) * not_(redevable_tva_regime_simplifie)


class option_tva_regime_simplifie_possible(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"L'entreprise peut opter pour le régime simplifié de TVA"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca_total = entreprise('chiffre_affaire_total', period)
        seuil_tva_franchise_en_base = entreprise.pays('seuil_tva_franchise_en_base', period)
        ca_inferieur_a_seuil = ca_total < seuil_tva_franchise_en_base
        return ca_inferieur_a_seuil


class option_tva_regime_simplifie(Variable):
    value_type = Enum
    entity = Entreprise
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = u"Défini si l'entreprise à opté pour le régime simplifié alors qu'elle est éligible à la franchise en base"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source


class option_tva_regime_reel_trimestriel_possible(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"L'entreprise peut opter pour le régime réel trimestriel de TVA"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca_total = entreprise('chiffre_affaire_total', period)
        seuil_tva_regime_simplifiee_activite_commerciale = entreprise.pays('seuil_tva_regime_simplifiee_activite_commerciale', period)
        seuil_tva_regime_simplifiee_activite_prestation = entreprise.pays('seuil_tva_regime_simplifiee_activite_prestation', period)
        ca_inferieur_a_seuil_activite_commerciale = ca_total < seuil_tva_regime_simplifiee_activite_commerciale
        ca_inferieur_a_seuil_activite_prestations = ca_total < seuil_tva_regime_simplifiee_activite_prestation
        activite_commerciale = entreprise('activite_commerciale', period)
        inferieur_seuil = where(activite_commerciale, ca_inferieur_a_seuil_activite_commerciale, ca_inferieur_a_seuil_activite_prestations)
        return inferieur_seuil


class option_tva_regime_reel_trimestriel(Variable):
    value_type = Enum
    entity = Entreprise
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = u"Défini si l'entreprise à opté pour le régime réel trimestriel alors qu'elle est éligible à un régime plus favorable"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source


class option_tva_regime_reel_mensuel_possible(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"L'entreprise peut opter pour le régime réel mensuel de TVA"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca_total = entreprise('chiffre_affaire_total', period)
        seuil_tva_regime_reel_trimestriel = entreprise.pays('seuil_tva_regime_reel_trimestriel', period)
        ca_inferieur_seuil = ca_total < seuil_tva_regime_reel_trimestriel
        return ca_inferieur_seuil


class option_tva_regime_reel_mensuel(Variable):
    value_type = Enum
    entity = Entreprise
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = u"Défini si l'entreprise à opté pour le régime réel mensuel alors qu'elle est éligible à un régime plus favorable"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source
