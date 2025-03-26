# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (Period, DAY, select, Variable, where, isin, not_)
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activity import Activite, ACTIVITE_ABATTEMENT_IMF, ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_IMF


class imf_brut_base(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Base IMF"

    def formula(person: Personne, period, parameters):
        produits_exploitation = person('is_resultat_exploitation_total_produits', period)
        transfert_charge_exploitation = person('is_resultat_exploitation_resprises_amortissements_provisions_transfert_charges', period)
        produits_financier = person('is_resultat_financier_total_produits', period)
        transfert_charge_financier = person('is_resultat_financier_transfert_charges', period)
        return produits_exploitation - transfert_charge_exploitation + produits_financier - transfert_charge_financier


class imf_brut_taux_benefice(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF Béneficiare"

    def formula(person: Personne, period, parameters):
        taux = parameters(period).dicp.impot_societe.taux.imf.benefice
        return taux


class imf_brut_taux_deficit(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF Déficitaire"

    def formula(person: Personne, period, parameters):
        taux = parameters(period).dicp.impot_societe.taux.imf.deficit
        return taux


class imf_est_deficitaire(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "L'IMF est-il déficitaire ?"

    def formula(person: Personne, period, parameters):
        deficit = person('is_resultat_fiscal_deficit_total', period)
        return deficit > 0


class imf_est_beneficiaire(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "L'IMF est-il bénéficiare ?"

    def formula(person: Personne, period, parameters):
        deficitaire = person('imf_est_deficitaire', period)
        return not_(deficitaire)


class imf_brut_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF à la date de clotûre"

    def formula(person: Personne, period, parameters):
        taux_benefice = person('imf_brut_taux_benefice', period)
        taux_deficit = person('imf_brut_taux_deficit', period)
        deficitaire = person('imf_est_deficitaire', period)
        taux = where(deficitaire, taux_deficit, taux_benefice)
        return taux


class is_nombre_mois_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Nombre de mois qu'a duré l'exercice"
    default_value = 12


class imf_brut_montant_minimum(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant minimum d'IMF à la date de clotûre"

    def formula(person: Personne, period, parameters):
        nombre_mois = person('is_nombre_mois_exercice', period)
        montant = parameters(period).dicp.impot_societe.montant.imf.minimum
        return (montant / 12) * nombre_mois


class imf_brut_montant_maximum(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant maximum d'IMF à la date de clotûre"

    def formula(person: Personne, period, parameters):
        nombre_mois = person('is_nombre_mois_exercice', period)
        montant = parameters(period).dicp.impot_societe.montant.imf.maximum
        return (montant / 12) * nombre_mois


class imf_brut_possede_abattement(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité possède un abattement IMF ?"

    def formula(local: Personne, period: Period, parameters):
        activite_principale = local('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_ABATTEMENT_IMF)


class imf_brut_abattement_taux_saisie(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF Abattement Saisie"


class imf_brut_abattement_taux_est_a_saisir(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Taux Abattement IMF doit être saisie"

    def formula(local: Personne, period: Period, parameters):
        activite_principale = local('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_IMF)


class imf_brut_abattement_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF Abattement"

    def formula(person: Personne, period, parameters):
        activite_principale = person('is_activite_principale', period)
        possede_abattement = person('imf_brut_possede_abattement', period)
        abattement_taux_est_a_saisir = person('imf_brut_abattement_taux_est_a_saisir', period)
        abattement_saisie = person('imf_brut_abattement_taux_saisie', period)

        nbr_exercice = person('is_nombre_exercices', period)
        nbr_exercice = where(nbr_exercice > 0, nbr_exercice, 999)

        # NotImplementedError returned by "parameters(period).dicp.impot_societe.taux.activite_exoneration_is[activite_principale]"
        societes_gestion_fonds_garantie = parameters(period).dicp.impot_societe.taux.imf_abattement.SOCIETES_GESTION_FONDS_GARANTIE

        abattement = select([
            activite_principale == Activite.SOCIETES_GESTION_FONDS_GARANTIE,
            ], [
            societes_gestion_fonds_garantie.calc(nbr_exercice),
            ], 0.0)

        abattement = where(abattement_taux_est_a_saisir, abattement_saisie, abattement)
        abattement = where(possede_abattement, abattement, 0)

        return abattement


class imf_brut_base_imposable(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Base IMF Brut Imposable"

    def formula(person: Personne, period, parameters):
        base = person('imf_brut_base', period)
        abattement = person('imf_brut_abattement_taux', period)
        return base * (1 - abattement)


class imf_brut_due(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant IMF brut due"

    def formula(person: Personne, period, parameters):
        base_imposable = person('imf_brut_base_imposable', period)
        taux = person('imf_brut_taux', period)
        imf_due = base_imposable * taux
        montant_min = person('imf_brut_montant_minimum', period)
        montant_max = person('imf_brut_montant_maximum', period)
        montant = select([
            imf_due < montant_min,
            montant_max < imf_due
            ], [
            montant_min,
            montant_max
            ], imf_due)
        return montant
