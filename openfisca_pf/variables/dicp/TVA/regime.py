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
    entity = Personne
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        ca_total = personne('chiffre_affaire_total', period)
        pas_option_tva_regime_simplifie = (personne('option_tva_regime_simplifie', period) == OuiNon.N) * personne('option_tva_regime_simplifie_possible', period)
        pas_option_tva_regime_reel_trimestriel = (personne('option_tva_regime_reel_trimestriel', period) == OuiNon.N) * personne('option_tva_regime_reel_trimestriel_possible', period)
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period) == OuiNon.N) * personne('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_franchise_en_base = personne.pays('seuil_tva_franchise_en_base', period)
        ca_inferieur_a_seuil = ca_total < seuil_tva_franchise_en_base
        return ca_inferieur_a_seuil * pas_option_tva_regime_simplifie * pas_option_tva_regime_reel_trimestriel * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_simplifie(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        ca_total = personne('chiffre_affaire_total', period)
        pas_redevable_tva_franchise_en_base = not_(personne('redevable_tva_franchise_en_base', period))
        pas_option_tva_regime_reel_trimestriel = (personne('option_tva_regime_reel_trimestriel', period) == OuiNon.N) * personne('option_tva_regime_reel_trimestriel_possible', period)
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period) == OuiNon.N) * personne('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_regime_simplifiee_activite_commerciale = personne.pays('seuil_tva_regime_simplifiee_activite_commerciale', period)
        seuil_tva_regime_simplifiee_activite_prestation = personne.pays('seuil_tva_regime_simplifiee_activite_prestation', period)
        ca_inferieur_a_seuil_activite_commerciale = ca_total < seuil_tva_regime_simplifiee_activite_commerciale
        ca_inferieur_a_seuil_activite_prestations = ca_total < seuil_tva_regime_simplifiee_activite_prestation
        activite_commerciale = personne('activite_commerciale', period)
        inferieur_seuil = where(activite_commerciale, ca_inferieur_a_seuil_activite_commerciale, ca_inferieur_a_seuil_activite_prestations)
        return inferieur_seuil * pas_redevable_tva_franchise_en_base * pas_option_tva_regime_reel_trimestriel * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_reel_trimestriel(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        ca_total = personne('chiffre_affaire_total', period)
        pas_redevable_tva_franchise_en_base = not_(personne('redevable_tva_franchise_en_base', period))
        pas_redevable_tva_regime_simplifie = not_(personne('redevable_tva_regime_simplifie', period))
        pas_option_tva_regime_reel_mensuel = (personne('option_tva_regime_reel_mensuel', period) == OuiNon.N) * personne('option_tva_regime_reel_mensuel_possible', period)
        seuil_tva_regime_reel_trimestriel = personne.pays('seuil_tva_regime_reel_trimestriel', period)
        ca_inferieur_seuil = ca_total < seuil_tva_regime_reel_trimestriel
        return ca_inferieur_seuil * pas_redevable_tva_franchise_en_base * pas_redevable_tva_regime_simplifie * pas_option_tva_regime_reel_mensuel


class redevable_tva_regime_reel_mensuel(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible à la franchise en base de TVA"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        redevable_tva_franchise_en_base = personne('redevable_tva_franchise_en_base', period)
        redevable_tva_regime_simplifie = personne('redevable_tva_regime_simplifie', period)
        redevable_tva_regime_reel_trimestriel = personne('redevable_tva_regime_reel_trimestriel', period)
        return not_(redevable_tva_regime_reel_trimestriel) * not_(redevable_tva_franchise_en_base) * not_(redevable_tva_regime_simplifie)


class option_tva_regime_simplifie_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"L'entreprise peut opter pour le régime simplifié de TVA"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        ca_total = personne('chiffre_affaire_total', period)
        seuil_tva_franchise_en_base = personne.pays('seuil_tva_franchise_en_base', period)
        ca_inferieur_a_seuil = ca_total < seuil_tva_franchise_en_base
        return ca_inferieur_a_seuil


class option_tva_regime_simplifie(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = u"Défini si l'entreprise à opté pour le régime simplifié alors qu'elle est éligible à la franchise en base"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source


class option_tva_regime_reel_trimestriel_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"L'entreprise peut opter pour le régime réel trimestriel de TVA"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        ca_total = personne('chiffre_affaire_total', period)
        seuil_tva_regime_simplifiee_activite_commerciale = personne.pays('seuil_tva_regime_simplifiee_activite_commerciale', period)
        seuil_tva_regime_simplifiee_activite_prestation = personne.pays('seuil_tva_regime_simplifiee_activite_prestation', period)
        ca_inferieur_a_seuil_activite_commerciale = ca_total < seuil_tva_regime_simplifiee_activite_commerciale
        ca_inferieur_a_seuil_activite_prestations = ca_total < seuil_tva_regime_simplifiee_activite_prestation
        activite_commerciale = personne('activite_commerciale', period)
        inferieur_seuil = where(activite_commerciale, ca_inferieur_a_seuil_activite_commerciale, ca_inferieur_a_seuil_activite_prestations)
        return inferieur_seuil


class option_tva_regime_reel_trimestriel(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = u"Défini si l'entreprise à opté pour le régime réel trimestriel alors qu'elle est éligible à un régime plus favorable"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source


class option_tva_regime_reel_mensuel_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"L'entreprise peut opter pour le régime réel mensuel de TVA"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        ca_total = personne('chiffre_affaire_total', period)
        seuil_tva_regime_reel_trimestriel = personne.pays('seuil_tva_regime_reel_trimestriel', period)
        ca_inferieur_seuil = ca_total < seuil_tva_regime_reel_trimestriel
        return ca_inferieur_seuil


class option_tva_regime_reel_mensuel(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = u"Défini si l'entreprise à opté pour le régime réel mensuel alors qu'elle est éligible à un régime plus favorable"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source


class nombre_entreprises_redevables_franchise_base_TVA_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de la franchise en base de TVA"

    def formula(pays, period, parameters):
        redevable_tva_franchise_en_base = pays.members('redevable_tva_franchise_en_base', period)
        return pays.sum(redevable_tva_franchise_en_base * 1)


class nombre_entreprises_redevables_regime_simplifie_TVA_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables du régime simplfié de TVA"

    def formula(pays, period, parameters):
        redevable_tva_regime_simplifie = pays.members('redevable_tva_regime_simplifie', period)
        return pays.sum(redevable_tva_regime_simplifie * 1)


class nombre_entreprises_redevables_regime_reel_trimestriel_TVA_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables du régime réel trimestriel de TVA"

    def formula(pays, period, parameters):
        redevable_tva_regime_reel_trimestriel = pays.members('redevable_tva_regime_reel_trimestriel', period)
        return pays.sum(redevable_tva_regime_reel_trimestriel * 1)


class nombre_entreprises_redevables_regime_reel_mensuel_TVA_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables du régime réel trimestriel de TVA"

    def formula(pays, period, parameters):
        redevable_tva_regime_reel_mensuel = pays.members('redevable_tva_regime_reel_mensuel', period)
        return pays.sum(redevable_tva_regime_reel_mensuel * 1)
