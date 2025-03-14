# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (Period, DAY, Enum, select, Variable, where, isin, Parameters)
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activity import Activite, ACTIVITE_TAUX_IS, ACTIVITE_EXONERATRICE, \
    ACTIVITE_EXONERATRICE_TAUX_A_SAISIR
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

    def formula(local: Personne, period: Period, parameters: Parameters):
        activite_principale = local('is_activite_principale', period, parameters)
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

    def formula(person: Personne, period):
        ca_zrae = person('is_element_imposition_zrae_ca', period)
        ca = person('is_element_imposition_ca', period)
        is_zrae = (ca_zrae > 0) * (ca > 0)
        quotient_zrae = ca_zrae / where((ca > 0), ca, -1)
        return is_zrae * quotient_zrae


class is_brut_taux_activite(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IS Activité à la date de clotûre"

    def formula(person: Personne, period, parameters):
        activite_principale = person('is_activite_principale', period)
        possede_taux_is = person('is_activite_principale_possede_taux_is', period)
        activite_taux = where(possede_taux_is, activite_principale.decode_to_str(), 'NORMALE')
        taux_principal = parameters(period).dicp.impot_societe.taux.activite[activite_taux]
        return taux_principal


class is_brut_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Is Societe"

    def formula(person: Personne, period, parameters):
        taux_principal = person('is_brut_taux_activite', period)
        is_zrae = person('is_est_zrae', period)
        quotient_zrae = person('is_quotient_zrae', period)
        taux_zrae = parameters(period).dicp.impot_societe.taux.activite['zone_revitalisation_zrae']
        return where(is_zrae, (taux_principal * (1 - quotient_zrae) + (taux_zrae * quotient_zrae)), taux_principal)


class is_activite_principale_possede_abattement(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activite taux IS ?"

    def formula(local: Personne, period: Period, parameters: Parameters):
        activite_principale = local('is_activite_principale', period, parameters)
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

    def formula(local: Personne, period: Period, parameters):
        activite_principale = local('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_EXONERATRICE_TAUX_A_SAISIR)


class is_brut_abattement_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Brut Abattement IS"

    def formula(person: Personne, period, parameters):
        activite_principale = person('is_activite_principale', period)
        possede_abattement = person('is_activite_principale_possede_abattement', period)
        abattement_taux_est_a_saisir = person('is_brut_abattement_taux_est_a_saisir', period)
        abattement_saisie = person('is_brut_abattement_taux_saisie', period)

        nbr_exercice = person('is_nombre_exercices', period)
        nbr_exercice = where(nbr_exercice > 0, nbr_exercice, 999)

        # NotImplementedError returned by "parameters(period).dicp.impot_societe.taux.activite_exoneration_is[activite_principale]"
        societes_gestion_fonds_garantie = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.SOCIETES_GESTION_FONDS_GARANTIE
        hotel_residence_international = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.HOTEL_RESIDENCE_INTERNATIONAL
        concessions_minieres = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.CONCESSIONS_MINIERES
        membre_groupe_fiscal = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.MEMBRE_GROUPE_FISCAL
        gie = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.GIE
        scpr = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.SCPR
        scm = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.SCM
        obnl = parameters(period).dicp.impot_societe.taux.activite_exoneration_is.OBNL

        abattement = select([
            activite_principale == Activite.SOCIETES_GESTION_FONDS_GARANTIE,
            activite_principale == Activite.HOTEL_RESIDENCE_INTERNATIONAL,
            activite_principale == Activite.CONCESSIONS_MINIERES,
            activite_principale == Activite.MEMBRE_GROUPE_FISCAL,
            activite_principale == Activite.GIE,
            activite_principale == Activite.SCPR,
            activite_principale == Activite.SCM,
            activite_principale == Activite.OBNL,
            True
            ], [
            societes_gestion_fonds_garantie.calc(nbr_exercice),
            hotel_residence_international.calc(nbr_exercice),
            concessions_minieres.calc(nbr_exercice),
            membre_groupe_fiscal.calc(nbr_exercice),
            gie.calc(nbr_exercice),
            scpr.calc(nbr_exercice),
            scm.calc(nbr_exercice),
            obnl.calc(nbr_exercice),
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

    def formula(person: Personne, period, parameters):
        resultat_fiscal = person('is_resultat_fiscal_benefice_apres_report_deficitaire', period)
        is_brut_base = arrondi_millier_inferieur(resultat_fiscal)
        return is_brut_base


class is_brut_due(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Somme Brut Is Societe Due"

    def formula(person: Personne, period, parameters):

        brut_base = person('is_brut_base', period)
        abattement = person('is_brut_abattement_taux', period)
        taux_brut = person('is_brut_taux', period)
        is_brut_due = brut_base * (1 - abattement) * taux_brut
        return is_brut_due
