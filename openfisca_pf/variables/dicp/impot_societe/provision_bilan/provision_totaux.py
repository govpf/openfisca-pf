# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    YEAR,
    ParameterNode,
    Period,
    Population,
    Variable
    )
from openfisca_pf.entities import Personne

class is_provisions_reglementees_total_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions réglementées total I montant au debut de l'exercice (3Z)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        reglementees_un = personne('is_provision_reglementees_un_montant_au_debut_de_l_exercice', period)
        reglementees_deux = personne('is_provision_reglementees_deux_montant_au_debut_de_l_exercice', period)
        autres_provisions = personne('is_provision_reglementees_autres_provisions_reglementees_montant_au_debut_de_l_exercice', period)
        return reglementees_un + reglementees_deux + autres_provisions


class is_provisions_reglementees_total_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions réglementées total I augmentations dotations de l'exercice (TS)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        reglementees_un = personne('is_provision_reglementees_un_augmentations_dotations_de_l_exercice', period)
        reglementees_deux = personne('is_provision_reglementees_deux_augmentations_dotations_de_l_exercice', period)
        autres_provisions = personne('is_provision_reglementees_autres_provisions_reglementees_augmentations_dotations_de_l_exercice', period)
        return reglementees_un + reglementees_deux + autres_provisions


class is_provisions_reglementees_total_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions réglementées total I diminutions reprises de l'exercice (TT)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        reglementees_un = personne('is_provision_reglementees_un_diminutions_reprises_de_l_exercice', period)
        reglementees_deux = personne('is_provision_reglementees_deux_diminutions_reprises_de_l_exercice', period)
        autres_provisions = personne('is_provision_reglementees_autres_provisions_reglementees_diminutions_reprises_de_l_exercice', period)
        return reglementees_un + reglementees_deux + autres_provisions


class is_provisions_reglementees_total_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions réglementées total I montant à la fin de l'exercice (TU)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        reglementees_un = personne('is_provision_reglementees_un_montant_a_la_fin_de_l_exercice', period)
        reglementees_deux = personne('is_provision_reglementees_deux_montant_a_la_fin_de_l_exercice', period)
        autres_provisions = personne('is_provision_reglementees_autres_provisions_reglementees_montant_a_la_fin_de_l_exercice', period)
        return reglementees_un + reglementees_deux + autres_provisions


class is_provisions_pour_risques_et_charges_total_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour risques et charges total montant au début de l'exercice (5Z)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provision_charges_sociales = personne('is_provision_pour_charges_sociales_et_fiscales_sur_conges_a_payer_montant_au_debut_de_l_exercice', period)
        autres_provisions = personne('is_provision_autres_provisions_pour_risques_et_charges_montant_au_debut_de_l_exercice', period)
        return provision_charges_sociales + autres_provisions


class is_provisions_pour_risques_et_charges_total_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour risques et charges total augmentations dotations de l'exercice (TV)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provision_charges_sociales = personne('is_provision_pour_charges_sociales_et_fiscales_sur_conges_a_payer_augmentations_dotation_de_l_exercice', period)
        autres_provisions = personne('is_provision_autres_provisions_pour_risques_et_charges_augmentations_dotation_de_l_exercice', period)
        return provision_charges_sociales + autres_provisions


class is_provisions_pour_risques_et_charges_total_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour risques et charges total diminutions reprises de l'exercice (TW)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provision_charges_sociales = personne('is_provision_pour_charges_sociales_et_fiscales_sur_conges_a_payer_diminution_reprises_de_l_exercice', period)
        autres_provisions = personne('is_provision_autres_provisions_pour_risques_et_charges_diminution_reprises_de_l_exercice', period)
        return provision_charges_sociales + autres_provisions


class is_provisions_pour_risques_et_charges_total_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour risques et charges total montant à la fin de l'exercice (TX)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provision_charges_sociales = personne('is_provision_pour_charges_sociales_et_fiscales_sur_conges_a_payer_montant_a_la_fin_de_l_exercice', period)
        autres_provisions = personne('is_provision_autres_provisions_pour_risques_et_charges_montant_a_la_fin_de_l_exercice', period)
        return provision_charges_sociales + autres_provisions


class is_provisions_pour_depreciation_total_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour dépréciation total montant au début de l'exercice (7B)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        sur_immobilisations_incorporelles = personne('is_provision_sur_immobilisations_incorporelles_montant_au_debut_de_l_exercice', period)
        sur_immobilisations_corporelles = personne('is_provision_sur_immobilisations_corporelles_montant_au_debut_de_l_exercice', period)
        sur_immobilisations_autres_immobilisations_financieres = personne('is_provision_sur_immobilisations_autres_immobilisations_financieres_montant_au_debut_de_l_exercice', period)
        stocks_et_en_cours = personne('is_provision_sur_stocks_et_en_cours_montant_au_debut_de_l_exercice', period)
        comptes_clients = personne('is_provision_sur_comptes_clients_montant_au_debut_de_l_exercice', period)
        autres_provisions = personne('is_provision_autres_provisions_pour_depreciation_montant_au_debut_de_l_exercice', period)
        return sur_immobilisations_incorporelles + sur_immobilisations_corporelles + sur_immobilisations_autres_immobilisations_financieres + stocks_et_en_cours + comptes_clients + autres_provisions


class is_provisions_pour_depreciation_total_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour dépréciation total augmentations dotations de l'exercice (TY)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        sur_immobilisations_incorporelles = personne('is_provision_sur_immobilisations_incorporelles_augmentations_dotations_de_l_exercice', period)
        sur_immobilisations_corporelles = personne('is_provision_sur_immobilisations_corporelles_augmentations_dotations_de_l_exercice', period)
        sur_immobilisations_autres_immobilisations_financieres = personne('is_provision_sur_immobilisations_autres_immobilisations_financieres_augmentations_dotations_de_l_exercice', period)
        stocks_et_en_cours = personne('is_provision_sur_stocks_et_en_cours_augmentations_dotations_de_l_exercice', period)
        comptes_clients = personne('is_provision_sur_comptes_clients_augmentations_dotations_de_l_exercice', period)
        autres_provisions = personne('is_provision_autres_provisions_pour_depreciation_augmentations_dotations_de_l_exercice', period)
        return sur_immobilisations_incorporelles + sur_immobilisations_corporelles + sur_immobilisations_autres_immobilisations_financieres + stocks_et_en_cours + comptes_clients + autres_provisions


class is_provisions_pour_depreciation_total_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour dépréciation total diminutions reprises de l'exercice (TZ)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        sur_immobilisations_incorporelles = personne('is_provision_sur_immobilisations_incorporelles_diminutions_reprises_de_l_exercice', period)
        sur_immobilisations_corporelles = personne('is_provision_sur_immobilisations_corporelles_diminutions_reprises_de_l_exercice', period)
        sur_immobilisations_autres_immobilisations_financieres = personne('is_provision_sur_immobilisations_autres_immobilisations_financieres_diminutions_reprises_de_l_exercice', period)
        stocks_et_en_cours = personne('is_provision_sur_stocks_et_en_cours_diminutions_reprises_de_l_exercice', period)
        comptes_clients = personne('is_provision_sur_comptes_clients_diminutions_reprises_de_l_exercice', period)
        autres_provisions = personne('is_provision_autres_provisions_pour_depreciation_diminutions_reprises_de_l_exercice', period)
        return sur_immobilisations_incorporelles + sur_immobilisations_corporelles + sur_immobilisations_autres_immobilisations_financieres + stocks_et_en_cours + comptes_clients + autres_provisions


class is_provisions_pour_depreciation_total_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions pour dépréciation total montant à la fin de l'exercice (UA)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        sur_immobilisations_incorporelles = personne('is_provision_sur_immobilisations_incorporelles_montant_a_la_fin_de_l_exercice', period)
        sur_immobilisations_corporelles = personne('is_provision_sur_immobilisations_corporelles_montant_a_la_fin_de_l_exercice', period)
        sur_immobilisations_autres_immobilisations_financieres = personne('is_provision_sur_immobilisations_autres_immobilisations_financieres_montant_a_la_fin_de_l_exercice', period)
        stocks_et_en_cours = personne('is_provision_sur_stocks_et_en_cours_montant_a_la_fin_de_l_exercice', period)
        comptes_clients = personne('is_provision_sur_comptes_clients_montant_a_la_fin_de_l_exercice', period)
        autres_provisions = personne('is_provision_autres_provisions_pour_depreciation_montant_a_la_fin_de_l_exercice', period)
        return sur_immobilisations_incorporelles + sur_immobilisations_corporelles + sur_immobilisations_autres_immobilisations_financieres + stocks_et_en_cours + comptes_clients + autres_provisions


class is_provisions_total_general_montant_au_debut_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions total général montant au début de l'exercice (7C)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provisions_reglementees = personne('is_provisions_reglementees_total_montant_au_debut_de_l_exercice', period)
        provisions_pour_risques_et_charges = personne('is_provisions_pour_risques_et_charges_total_montant_au_debut_de_l_exercice', period)
        provisions_pour_depreciation = personne('is_provisions_pour_depreciation_total_montant_au_debut_de_l_exercice', period)
        return provisions_reglementees + provisions_pour_risques_et_charges + provisions_pour_depreciation


class is_provisions_total_general_augmentations_dotations_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions total général augmentations dotations de l'exercice (UB)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provisions_reglementees = personne('is_provisions_reglementees_total_augmentations_dotations_de_l_exercice', period)
        provisions_pour_risques_et_charges = personne('is_provisions_pour_risques_et_charges_total_augmentations_dotations_de_l_exercice', period)
        provisions_pour_depreciation = personne('is_provisions_pour_depreciation_total_augmentations_dotations_de_l_exercice', period)
        return provisions_reglementees + provisions_pour_risques_et_charges + provisions_pour_depreciation


class is_provisions_total_general_diminutions_reprises_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions total général diminutions reprises de l'exercice (UC)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provisions_reglementees = personne('is_provisions_reglementees_total_diminutions_reprises_de_l_exercice', period)
        provisions_pour_risques_et_charges = personne('is_provisions_pour_risques_et_charges_total_diminutions_reprises_de_l_exercice', period)
        provisions_pour_depreciation = personne('is_provisions_pour_depreciation_total_diminutions_reprises_de_l_exercice', period)
        return provisions_reglementees + provisions_pour_risques_et_charges + provisions_pour_depreciation


class is_provisions_total_general_montant_a_la_fin_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions total général montant à la fin de l'exercice (UD)"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        provisions_reglementees = personne('is_provisions_reglementees_total_montant_a_la_fin_de_l_exercice', period)
        provisions_pour_risques_et_charges = personne('is_provisions_pour_risques_et_charges_total_montant_a_la_fin_de_l_exercice', period)
        provisions_pour_depreciation = personne('is_provisions_pour_depreciation_total_montant_a_la_fin_de_l_exercice', period)
        return provisions_reglementees + provisions_pour_risques_et_charges + provisions_pour_depreciation