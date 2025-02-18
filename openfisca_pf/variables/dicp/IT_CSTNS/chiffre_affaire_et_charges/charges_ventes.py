# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne


class charges_total_ventes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total des charges concernant des ventes avant abattement"
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters):
        value = 0
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_ventes]:
            value += personne(f'charges_{activite}', period)
        return value


class charges_apport_en_societe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Apport en société"


class charges_baguettes_revente_au_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Bagettes revente au détail"


class charges_coprah(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Coprah"


class charges_farine_riz_sucre(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Farine, riz, sucre"


class charges_hydrocarbures_au_detail(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Hydrcarbures au détail"


class charges_importateurs_grossistes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Importateurs grossistes"


class charges_lait_frais(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Lait frais"


class charges_negociants_detaillants_ca_superieur_20mf(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Négociants détaillants CA > 20M"


class charges_tabacs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Tabacs"


class charges_timbres_postes_et_fiscaux(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Timbres postes et fiscaux"


class charges_ventes_sans_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes sans abattement"


class charges_ventes_a_l_aventure_armateurs(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes à l'aventure (armateurs)"


class charges_ventes_a_l_aventure_goelettes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes à l'aventure (goelettes)"


class charges_ventes_en_gros(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes en gros"


class charges_vente_gros_lait_frais(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes en gros lait frais d'origine local"


class charges_ventes_inferieur_20_millions(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Charges dans la catégorie Ventes < 20 millions"
