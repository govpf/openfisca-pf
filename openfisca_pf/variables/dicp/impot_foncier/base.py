# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    not_,
    Parameters,
    Period,
    select,
    Variable,
    YEAR
)
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.functions.currency import arrondi_inferieur


class taux_premier_abattement_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux du première abattement de 25%"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.premier.taux


class taux_premier_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux du première abattement de 25%"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_premier_abattement_pays', period, parameters)


class montant_premier_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Montant du première abattement de 25%"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('valeur_locative_brute', period, parameters)
        taux = personne('taux_premier_abattement', period, parameters)
        return base * taux


class base_imposable_apres_premier_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Base imposable intermédiaire après application du première abattement de 25%"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('valeur_locative_brute', period, parameters)
        montant = personne('montant_premier_abattement', period, parameters)
        return base - montant


class taux_second_abattement_location_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux du second abattement quand le bien est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.second.location_meuble.taux


class taux_second_abattement_location_non_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.
    label = "Taux du second abattement quand le bien est loué en non meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.second.location_non_meuble.taux


class taux_second_abattement_location_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux du second abattement quand le bien est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_second_abattement_location_meuble_pays', period, parameters)


class taux_second_abattement_location_non_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux du second abattement quand le bien est loué en non meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('taux_second_abattement_location_non_meuble_pays', period, parameters)


class taux_second_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Taux du second abattement en fonction de comment le bien est loué"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        location_meuble = personne('location_meuble', period, parameters)
        location_non_meuble = personne('location_non_meuble', period, parameters)
        taux_location_meuble = personne('taux_second_abattement_location_meuble', period, parameters)
        taux_location_non_meuble = personne('taux_second_abattement_location_non_meuble', period, parameters)
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


class montant_second_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Base imposable intermédiaire après application du second abattement qui est fonction du type de location"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('base_imposable_apres_premier_abattement', period, parameters)
        taux = personne('taux_second_abattement', period, parameters)
        return base * taux


class base_imposable_apres_second_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.
    label = "Base imposable intermédiaire après application du second abattement qui est fonction du type de location"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('base_imposable_apres_premier_abattement', period, parameters)
        montant = personne('montant_second_abattement', period, parameters)
        return base - montant


class age_min_abattement_nouvelle_construction_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.nouvelle_construction.age_min


class age_min_abattement_nouvelle_construction(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age minimum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        return personne.pays('age_min_abattement_nouvelle_construction_pays', period, parameters)


class age_max_abattement_nouvelle_construction_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Age maximum pour qu'une nouvelle construction soit eligible à un abattement pour les nouvelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(pays: Pays, period: Period, parameters: Parameters) -> ArrayLike:
        return parameters(period).dicp.impot_foncier.base.abattement.nouvelle_construction.age_max


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
    label = "Est-ce que le bien est elligible à l'abattement de 50% les trois années qui suivent l'exonération temporaire de cinq ans pour les noubelles constructions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        terrain = personne('terrain', period, parameters)
        age_du_bien = personne('age_du_bien', period, parameters)
        age_min = personne('age_min_abattement_nouvelle_construction', period, parameters)
        age_max = personne('age_max_abattement_nouvelle_construction', period, parameters)
        return not_(terrain) * (age_min <= age_du_bien <= age_max)


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
        base = personne('base_imposable_apres_second_abattement', period, parameters)
        eligible = personne('eligible_abattement_nouvelle_construction', period, parameters)
        taux = personne('taux_abattement_nouvelle_construction', period, parameters)
        return select(
            [eligible],
            [base * taux],
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
        base = personne('base_imposable_apres_second_abattement', period, parameters)
        montant = personne('montant_abattement_nouvelle_construction', period, parameters)
        return base - montant


class valeur_locative_nette(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Base imposable de l'impot foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('base_imposable_apres_second_abattement', period, parameters)
        return arrondi_inferieur(base)

    def formula_1999_01_01(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base = personne('base_imposable_apres_abattement_nouvelle_construction', period, parameters)
        return arrondi_inferieur(base)
