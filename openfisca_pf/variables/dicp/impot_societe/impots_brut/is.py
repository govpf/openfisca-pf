# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (ArrayLike, Period, DAY, Enum, select, Variable, where, isin, ParameterNode, Population)
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activity import Activite, ACTIVITE_TAUX_IS, ACTIVITE_ABATTEMENT_IS, \
    ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_IS
from openfisca_pf.functions.currency import arrondi_millier_inferieur


class is_activite_principale(Variable):
    value_type = Enum
    possible_values = Activite
    entity = Personne
    definition_period = DAY
    default_value = Activite.NORMALE
    label = "Activité principale societe"


class is_brut_possede_taux_is(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité possède un taux IS ?"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_TAUX_IS)


class is_est_zrae(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité est ZRAE ?"


class is_quotient_zrae(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Quotient ZRAE"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        ca_zrae = personne('is_element_imposition_zrae_ca', period)
        ca_imposition = personne('is_element_imposition_ca', period)
        ca_net = personne('is_resultat_exploitation_chiffre_affaires_net_total', period)
        ca = where((ca_imposition > 0), ca_imposition, ca_net)
        possede_quotient = (ca_zrae > 0) * (ca > 0)
        quotient_zrae = ca_zrae / where((ca > 0), ca, -1)
        return possede_quotient * quotient_zrae


class is_brut_taux_activite(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IS Activité à la date de clotûre"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period)
        possede_taux_is = personne('is_brut_possede_taux_is', period)
        activite_taux = where(possede_taux_is, activite_principale.decode_to_str(), 'NORMALE')
        taux_principal = parameters(period).dicp.impot_societe.taux.is_par_activite[activite_taux]
        return taux_principal


class is_brut_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Is Societe"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        taux_principal = personne('is_brut_taux_activite', period)
        is_zrae = personne('is_est_zrae', period)
        quotient_zrae = personne('is_quotient_zrae', period)
        taux_zrae = parameters(period).dicp.impot_societe.taux.is_par_activite['zone_revitalisation_zrae']
        return where(is_zrae, (taux_principal * (1 - quotient_zrae) + (taux_zrae * quotient_zrae)), taux_principal)


class is_brut_possede_abattement(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité possède un abattement IS ?"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_ABATTEMENT_IS)


class is_brut_abattement_taux_saisie(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Brut Abattement Saisie"


class is_nombre_exercices(Variable):
    value_type = int
    entity = Personne
    default_value = 0
    definition_period = DAY
    label = "Nombre d'exercices"


class is_brut_abattement_taux_est_a_saisir(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Taux Abattement doit être saisie"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_IS)


class is_brut_abattement_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Brut Abattement IS"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period)
        possede_abattement = personne('is_brut_possede_abattement', period)
        abattement_taux_est_a_saisir = personne('is_brut_abattement_taux_est_a_saisir', period)
        abattement_saisie = personne('is_brut_abattement_taux_saisie', period)

        nombre_exercices = personne('is_nombre_exercices', period)
        nombre_exercices = where(nombre_exercices > 0, nombre_exercices, 999)

        # NotImplementedError returned by "parameters(period).dicp.impot_societe.taux.activite_exoneration_is[activite_principale]"
        societes_gestion_fonds_garantie = parameters(period).dicp.impot_societe.taux.is_abattement.SOCIETES_GESTION_FONDS_GARANTIE

        abattement = select([
            activite_principale == Activite.SOCIETES_GESTION_FONDS_GARANTIE,
            ], [
            societes_gestion_fonds_garantie.calc(nombre_exercices),
            ], 0.0)

        abattement = where(abattement_taux_est_a_saisir, abattement_saisie, abattement)
        abattement = where(possede_abattement, abattement, 0)

        return abattement


class is_brut_base(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Base Brut Is Societe"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        resultat_fiscal = personne('is_resultat_fiscal_benefice_apres_report_deficitaire', period)
        base = arrondi_millier_inferieur(resultat_fiscal)
        return base


class is_brut_base_imposable(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Base Brut imposable Is Societe"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base = personne('is_brut_base', period)
        abattement = personne('is_brut_abattement_taux', period)
        base_imposable = base * (1 - abattement)
        return base_imposable


class is_brut_due(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Somme Brut Is Societe Due"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        brut_base = personne('is_brut_base_imposable', period)
        taux_brut = personne('is_brut_taux', period)
        is_brut_due = brut_base * taux_brut
        return is_brut_due
