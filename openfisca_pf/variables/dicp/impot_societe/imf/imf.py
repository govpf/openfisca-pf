# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (Period, DAY, select, Variable, where, isin, not_)
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activity import Activite, ACTIVITE_EXONERATRICE_TAUX_A_SAISIR


class is_imf_base(Variable):
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


class is_imf_taux_benefice(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF Béneficiare"

    def formula(person: Personne, period, parameters):
        taux = parameters(period).dicp.impot_societe.taux.imf.benefice
        return taux


class is_imf_taux_deficit(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF Déficitaire"

    def formula(person: Personne, period, parameters):
        taux = parameters(period).dicp.impot_societe.taux.imf.deficit
        return taux


class is_imf_est_deficitaire(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "L'IMF est-il déficitaire ?"

    def formula(person: Personne, period, parameters):
        deficit = person('is_resultat_fiscal_deficit_total', period)
        return deficit > 0


class is_imf_est_beneficiaire(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "L'IMF est-il bénéficiare ?"

    def formula(person: Personne, period, parameters):
        deficitaire = person('is_imf_est_deficitaire', period)
        return not_(deficitaire)


class is_imf_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF à la date de clotûre"

    def formula(person: Personne, period, parameters):
        taux_benefice = person('is_imf_taux_benefice', period)
        taux_deficit = person('is_imf_taux_deficit', period)
        deficitaire = person('is_imf_est_deficitaire', period)
        taux = where(deficitaire, taux_deficit, taux_benefice)
        return taux


class is_nombre_mois_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Nombre de mois qu'a duré l'exercice"
    default_value = 12


class is_imf_montant_minimum(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant minimum d'IMF à la date de clotûre"

    def formula(person: Personne, period, parameters):
        nombre_mois = person('is_nombre_mois_exercice', period)
        montant = parameters(period).dicp.impot_societe.montant.imf.minimum
        return (montant / 12) * nombre_mois


class is_imf_montant_maximum(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant maximum d'IMF à la date de clotûre"

    def formula(person: Personne, period, parameters):
        nombre_mois = person('is_nombre_mois_exercice', period)
        montant = parameters(period).dicp.impot_societe.montant.imf.maximum
        return (montant / 12) * nombre_mois


class is_imf_abattement_taux_saisie(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF Abattement Saisie"


class is_imf_abattement_taux_est_a_saisir(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Taux Abattement IMF doit être saisie"

    def formula(local: Personne, period: Period, parameters):
        activite_principale = local('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_EXONERATRICE_TAUX_A_SAISIR)


class is_imf_abattement_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux IMF Abattement"

    def formula(person: Personne, period, parameters):
        activite_principale = person('is_activite_principale', period)
        possede_abattement = person('is_activite_principale_possede_abattement', period)
        abattement_taux_est_a_saisir = person('is_imf_abattement_taux_est_a_saisir', period)
        abattement_saisie = person('is_imf_abattement_taux_saisie', period)

        nbr_exercice = person('is_nombre_exercices', period)
        nbr_exercice = where(nbr_exercice > 0, nbr_exercice, 999)

        # NotImplementedError returned by "parameters(period).dicp.impot_societe.taux.activite_exoneration_is[activite_principale]"
        societes_gestion_fonds_garantie = parameters(period).dicp.impot_societe.taux.imf_exoneration_is.SOCIETES_GESTION_FONDS_GARANTIE
        activites_croisieres = parameters(period).dicp.impot_societe.taux.imf_exoneration_is.ACTIVITES_CROISIERE
        concessions_minieres = parameters(period).dicp.impot_societe.taux.imf_exoneration_is.CONCESSIONS_MINIERES
        membre_groupe_fiscal = parameters(period).dicp.impot_societe.taux.imf_exoneration_is.MEMBRE_GROUPE_FISCAL
        gie = parameters(period).dicp.impot_societe.taux.imf_exoneration_is.GIE
        scpr = parameters(period).dicp.impot_societe.taux.imf_exoneration_is.SCPR
        scm = parameters(period).dicp.impot_societe.taux.imf_exoneration_is.SCM
        obnl = parameters(period).dicp.impot_societe.taux.imf_exoneration_is.OBNL

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
            societes_gestion_fonds_garantie.calc(nbr_exercice),
            activites_croisieres.calc(nbr_exercice),
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


class is_imf_montant(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant IMF"

    def formula(person: Personne, period, parameters):
        imf_base = person('is_imf_base', period)
        taux = person('is_imf_taux', period)
        abattement = person('is_imf_abattement_taux', period)
        imf_due = imf_base * (1 - abattement) * taux
        montant_min = person('is_imf_montant_minimum', period)
        montant_max = person('is_imf_montant_maximum', period)
        montant = select([
            imf_due < montant_min,
            montant_max < imf_due,
            True
            ], [
            montant_min,
            montant_max,
            imf_due
            ])
        return montant
