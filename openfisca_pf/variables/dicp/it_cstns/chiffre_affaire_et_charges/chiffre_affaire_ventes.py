# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    floor,
    Parameter,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.constants.units import XPF


class chiffre_affaire_total_ventes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire concernant des ventes avant abattement"
    reference = []
    unit = XPF
    default_value = 0.

    def formula(personne: Population, period: Period, parameters: Parameter) -> ArrayLike:
        total = 0.
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_ventes]:
            chiffre_d_affaire_activite = personne(f'chiffre_affaire_{activite}', period)
            total += floor(chiffre_d_affaire_activite / 1000.) * 1000.
        return total


class chiffre_affaire_apport_en_societe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Apport en société"
    unit = XPF


class chiffre_affaire_baguettes_revente_au_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Bagettes revente au détail"
    unit = XPF


class chiffre_affaire_coprah(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Coprah"
    unit = XPF


class chiffre_affaire_farine_riz_sucre(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Farine, riz, sucre"
    unit = XPF


class chiffre_affaire_hydrocarbures_au_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Hydrcarbures au détail"
    unit = XPF


class chiffre_affaire_importateurs_grossistes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Importateurs grossistes"
    unit = "currency-XPF"


class chiffre_affaire_lait_frais(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Lait frais"
    unit = XPF


class chiffre_affaire_negociants_detaillants_ca_superieur_20mf(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Négociants détaillants CA > 20M"
    unit = XPF


class chiffre_affaire_tabacs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Tabacs"
    unit = XPF


class chiffre_affaire_timbres_postes_et_fiscaux(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Timbres postes et fiscaux"
    unit = XPF


class chiffre_affaire_ventes_sans_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes sans abattement"
    unit = XPF


class chiffre_affaire_ventes_a_l_aventure_armateurs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes à l'aventure (armateurs)"
    unit = XPF


class chiffre_affaire_ventes_a_l_aventure_goelettes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes à l'aventure (goelettes)"
    unit = XPF


class chiffre_affaire_ventes_en_gros(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes en gros"
    unit = XPF


class chiffre_affaire_vente_gros_lait_frais(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes en gros lait frais d'origine local"
    unit = XPF


class chiffre_affaire_ventes_inferieur_20_millions(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Chiffre d'affaire dans la catégorie Ventes < 20 millions"
    unit = XPF
