# -*- coding: utf-8 -*-

"""
Calcul de la base de l'impôt foncier en Polynésie Française.
Aussi appelé "valeur locative nette".
"""

from openfisca_pf.base import (
    ArrayLike,
    min_,
    not_,
    Parameters,
    Period,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.functions.currency import arrondi_inferieur


# ##################################################
# ###            ABATTEMENT D'OFFICE             ###
# ##################################################


class taux_abattement_office_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux du première abattement d'office de 25%"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.office.taux  # 0.25


class taux_abattement_office(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux du première abattement d'office de 25%"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_abattement_office_pays', period, parameters)  # 0.25


class montant_abattement_office(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant du première abattement d'office de 25%"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('valeur_locative_brute', period, parameters)
        taux = personne('taux_abattement_office', period, parameters)  # 0.25
        return base * taux


class base_imposable_apres_abattement_office(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Base imposable intermédiaire après application du première abattement d'office de 25%"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('valeur_locative_brute', period, parameters)
        montant = personne('montant_abattement_office', period, parameters)
        return base - montant


# ##################################################
# ###             ABATTEMENT LOCATIF             ###
# ##################################################


class taux_abattement_locatif_location_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux de l'abattement locatif quand le bien est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.locatif.location_meuble.taux


class taux_abattement_locatif_location_non_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux de l'abattement locatif quand le bien est loué en non meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.locatif.location_non_meuble.taux


class taux_abattement_locatif_location_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux de l'abattement locatif quand le bien est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_abattement_locatif_location_meuble_pays', period, parameters)


class taux_abattement_locatif_location_non_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux de l'abattement locatif quand le bien est loué en non meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_abattement_locatif_location_non_meuble_pays', period, parameters)


class taux_abattement_locatif(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux de l'abattement locatif en fonction de comment le bien est loué"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        location_meuble = personne('location_meuble', period, parameters)
        location_non_meuble = personne('location_non_meuble', period, parameters)
        taux_location_meuble = personne('taux_abattement_locatif_location_meuble', period, parameters)
        taux_location_non_meuble = personne('taux_abattement_locatif_location_non_meuble', period, parameters)
        return select(
            [
                location_meuble,
                location_non_meuble
            ],
            [
                taux_location_meuble,
                taux_location_non_meuble
            ],
            0.
        )


class eligible_abattement_locatif(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est éligible à un abatement locatif"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        location_meuble = personne('location_meuble', period, parameters)
        location_non_meuble = personne('location_non_meuble', period, parameters)
        return location_meuble + location_non_meuble


class abattement_locatif_applique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'abatement locatif s'applique pour ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne('eligible_abattement_locatif', period, parameters)


class abattement_locatif_eligible_et_applique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'abatement locatif s'applique pour ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_abattement_locatif', period, parameters)
        applique = personne('abattement_locatif_applique', period, parameters)
        return eligible * applique


class montant_abattement_locatif(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant de l'abattement locatif"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_applique = personne('abattement_locatif_eligible_et_applique', period, parameters)
        base = personne('base_imposable_apres_abattement_office', period, parameters)
        taux = personne('taux_abattement_locatif', period, parameters)
        return select(
            [eligible_et_applique],
            [base * taux],
            0.
            )


class base_imposable_apres_abattement_locatif(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Base imposable intermédiaire après application de l'abattement locatif"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('base_imposable_apres_abattement_office', period, parameters)
        montant = personne('montant_abattement_locatif', period, parameters)
        return base - montant


# ##################################################
# ###      ABATTEMENT NOUVELLE CONSTRUCTION      ###
# ##################################################


AGE_MIN_ABATTEMENT_NOUVELLE_CONSTRUCTION: int = 6
"""
Age minimum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions
"""


AGE_MAX_ABATTEMENT_NOUVELLE_CONSTRUCTION: int = 8
"""
Age maximum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions
"""


class age_min_abattement_nouvelle_construction_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MIN_ABATTEMENT_NOUVELLE_CONSTRUCTION


class age_max_abattement_nouvelle_construction_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Age maximum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return AGE_MAX_ABATTEMENT_NOUVELLE_CONSTRUCTION


class age_min_abattement_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('age_min_abattement_nouvelle_construction_pays', period, parameters)


class age_max_abattement_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('age_max_abattement_nouvelle_construction_pays', period, parameters)


class eligible_abattement_nouvelle_construction(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à l'abattement de 50% les trois années qui suivent l'exonération temporaire de cinq ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        terrain = personne('terrain', period, parameters)
        return not_(terrain)


class abattement_nouvelle_construction_applique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'abattement de 50% les trois années qui suivent l'exonération temporaire de cinq ans pour les nouvelles constructions s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        exonere_dix_ans = personne('exoneration_temporaire_habitation_principale_eligible_et_appliquee', period, parameters)
        eligible = personne('eligible_abattement_nouvelle_construction', period, parameters)
        age_du_bien = personne('age_du_bien', period, parameters)
        age_min = personne('age_min_abattement_nouvelle_construction', period, parameters)
        age_max = personne('age_max_abattement_nouvelle_construction', period, parameters)
        return not_(exonere_dix_ans) \
            * eligible \
            * age_min <= age_du_bien <= age_max


class abattement_nouvelle_construction_eligible_et_applique(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à l'abattement de 50% les trois années qui suivent l'exonération temporaire de cinq ans pour les nouvelles constructions et cet abattement s'applique"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_abattement_nouvelle_construction', period, parameters)
        applique = personne('abattement_nouvelle_construction_applique', period, parameters)
        return eligible * applique


class taux_abattement_nouvelle_construction_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Age maximum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.nouvelle_construction.taux


class taux_abattement_nouvelle_construction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Age minimum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_abattement_nouvelle_construction_pays', period, parameters)


class montant_abattement_nouvelle_construction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant de l'exonération temporaire pour les nouvelles constructions dans la phase de cinq à huit ans"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_applique = personne('abattement_nouvelle_construction_eligible_et_applique', period, parameters)
        base = personne('base_imposable_apres_abattement_locatif', period, parameters)
        taux = personne('taux_abattement_nouvelle_construction', period, parameters)
        return select(
            [eligible_et_applique],
            [base * taux],
            0
            )


class duree_restante_abattement_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Durée restante de l'abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022_12_13(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_abattement_nouvelle_construction', period, parameters)
        age_du_bien = personne('age_du_bien', period, parameters)
        age_min = personne('age_min_abattement_nouvelle_construction', period, parameters)
        age_max = personne('age_max_abattement_nouvelle_construction', period, parameters)

        return select(
            [eligible],
            [min_(age_max - age_du_bien, age_max - age_min + 1)],
            0
            )


class base_imposable_apres_abattement_nouvelle_construction(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Base imposable intermédiaire après application de l'exonération temporaire dehuit ans pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('base_imposable_apres_abattement_locatif', period, parameters)
        montant = personne('montant_abattement_nouvelle_construction', period, parameters)
        return base - montant


# ##################################################
# ###            VALEUR LOCATIVE NETTE           ###
# ##################################################


class valeur_locative_nette(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Base imposable de l'impot foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('base_imposable_apres_abattement_locatif', period, parameters)
        return arrondi_inferieur(base)

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('base_imposable_apres_abattement_nouvelle_construction', period, parameters)
        return arrondi_inferieur(base)
