# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    max_,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.functions.currency import arrondi_inferieur


class duree_restante_exonerations_temporaires_abattements_et_credits(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Durée restante des exonérations temporaraires"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        duree_restante_exoneration_temporaire_nouvelle_construction = personne('duree_restante_exoneration_temporaire_nouvelle_construction', period, parameters)
        duree_restante_abattement_nouvelle_construction = personne('duree_restante_abattement_nouvelle_construction', period, parameters)
        duree_restante_exoneration_temporaire_habitation_principale = personne('duree_restante_exoneration_temporaire_habitation_principale', period, parameters)
        duree_credit_photovoltaique = personne('duree_credit_photovoltaique', period, parameters)
        return max_(
            duree_restante_exoneration_temporaire_nouvelle_construction + max_(duree_restante_abattement_nouvelle_construction, duree_credit_photovoltaique),
            duree_restante_exoneration_temporaire_habitation_principale + duree_credit_photovoltaique
            )


class total_des_avantages_impot_foncier(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant total des avantages d'impôt foncier dont bénéficie le bient"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        exoneration_permanente = personne('montant_exoneration_permanente', period, parameters)
        exoneration_temporaire = personne('montant_exoneration_temporaire', period, parameters)
        credit = personne('montant_credit', period, parameters)
        return exoneration_permanente + exoneration_temporaire + credit


class impot_foncier_part_pays_apres_exonerations_permanentes(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de la part pays de l'impôt foncier après déduction des exonérations permanentes d'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        avant = personne('impot_foncier_part_pays_brute', period, parameters)
        montant = personne('montant_exoneration_permanente', period, parameters)
        return avant - montant


class impot_foncier_part_pays_apres_exonerations_temporaires(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de la part pays de l'impôt foncier après déduction des exonérations permanentes et des exonérations temporaires d'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        avant = personne('impot_foncier_part_pays_apres_exonerations_permanentes', period, parameters)
        montant = personne('montant_exoneration_temporaire', period, parameters)
        return avant - montant


class impot_foncier_part_pays_nette(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de la part pays nette de l'impôt foncier après déduction des exonérations permanentes, des exonérations temporaires et des crédits d'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        avant = personne('impot_foncier_part_pays_apres_exonerations_temporaires', period, parameters)
        montant = personne('montant_credit', period, parameters)
        return avant - montant


class taux_part_commune(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant de la part commune nette de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        commune_fiscale = personne('commune_fiscale', period, parameters)
        return parameters(period).dicp.impot_foncier.commune_fiscale[commune_fiscale].taux


class impot_foncier_part_commune_nette(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de la part commune nette de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        part_pays = personne('impot_foncier_part_pays_apres_exonerations_temporaires', period, parameters)
        taux = personne('taux_part_commune', period, parameters)
        return arrondi_inferieur(part_pays * taux)


class impot_foncier_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant total de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        impot_foncier_part_pays_nette = personne('impot_foncier_part_pays_nette', period, parameters)
        impot_foncier_part_commune_nette = personne('impot_foncier_part_commune_nette', period, parameters)
        return impot_foncier_part_pays_nette + impot_foncier_part_commune_nette
