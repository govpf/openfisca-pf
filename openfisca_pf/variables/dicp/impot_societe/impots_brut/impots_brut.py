# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    isin,
    ParameterNode,
    Period,
    Population,
    select,
    Variable,
    where
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activity import (
    Activite,
    ACTIVITE_TAUX_IS,
    ACTIVITE_EXONERATRICE,
    ACTIVITE_EXONERATRICE_TAUX_A_SAISIR
    )
from openfisca_pf.functions.currency import arrondi_millier_inferieur


class is_activite_principale(Variable):
    value_type = Enum
    possible_values = Activite
    entity = Personne
    definition_period = DAY
    default_value = Activite.NORMALE
    label = "Activité principale societe"


class is_activite_principale_possede_taux_is(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité possède un taux IS ?"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period)
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
        possede_taux_is = personne('is_activite_principale_possede_taux_is', period)
        activite_taux = where(possede_taux_is, activite_principale.decode_to_str(), 'NORMALE')
        taux_principal = parameters(period).dicp.impot_societe.taux.activite[activite_taux]
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
        taux_zrae = parameters(period).dicp.impot_societe.taux.activite['zone_revitalisation_zrae']
        return where(is_zrae, (taux_principal * (1 - quotient_zrae) + (taux_zrae * quotient_zrae)), taux_principal)


class is_activite_principale_possede_abattement(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité possède un abattement IS ?"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period)
        return isin(activite_principale, ACTIVITE_EXONERATRICE)


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
        activite_principale = personne('is_activite_principale', period)
        return isin(activite_principale, ACTIVITE_EXONERATRICE_TAUX_A_SAISIR)


class is_brut_abattement_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Brut Abattement IS"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period)
        possede_abattement = personne('is_activite_principale_possede_abattement', period)
        abattement_taux_est_a_saisir = personne('is_brut_abattement_taux_est_a_saisir', period)
        abattement_saisie = personne('is_brut_abattement_taux_saisie', period)

        nombre_exercices = personne('is_nombre_exercices', period)
        nombre_exercices = where(nombre_exercices > 0, nombre_exercices, 999)

        # NotImplementedError returned by "parameters(period).dicp.impot_societe.taux.activite_exoneration_is[activite_principale]"
        societes_gestion_fonds_garantie = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.SOCIETES_GESTION_FONDS_GARANTIE
        activites_croisieres = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.ACTIVITES_CROISIERE
        concessions_minieres = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.CONCESSIONS_MINIERES
        membre_groupe_fiscal = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.MEMBRE_GROUPE_FISCAL
        gie = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.GIE
        scpr = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.SCPR
        scm = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.SCM
        obnl = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.OBNL

        abattement = select([
            activite_principale == Activite.SOCIETES_GESTION_FONDS_GARANTIE,
            activite_principale == Activite.ACTIVITES_CROISIERE,
            activite_principale == Activite.CONCESSIONS_MINIERES,
            activite_principale == Activite.MEMBRE_GROUPE_FISCAL,
            activite_principale == Activite.GIE,
            activite_principale == Activite.SCPR,
            activite_principale == Activite.SCM,
            activite_principale == Activite.OBNL,
            True
            ], [
            societes_gestion_fonds_garantie.calc(nombre_exercices),
            activites_croisieres.calc(nombre_exercices),
            concessions_minieres.calc(nombre_exercices),
            membre_groupe_fiscal.calc(nombre_exercices),
            gie.calc(nombre_exercices),
            scpr.calc(nombre_exercices),
            scm.calc(nombre_exercices),
            obnl.calc(nombre_exercices),
            0.0
            ])

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
        is_brut_base = arrondi_millier_inferieur(resultat_fiscal)
        return is_brut_base


class is_brut_due(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Somme Brut Is Societe Due"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:

        brut_base = personne('is_brut_base', period)
        abattement = personne('is_brut_abattement_taux', period)
        taux_brut = personne('is_brut_taux', period)
        is_brut_due = brut_base * (1 - abattement) * taux_brut
        return is_brut_due
