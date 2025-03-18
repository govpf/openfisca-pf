# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    isin,
    Parameters,
    Period,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impots import FormeLegale
from openfisca_pf.functions.enum import enum_set
from openfisca_pf.variables.dicp.impot_foncier.commun import CategoryBien


# ##################################################
# ###                BIENS PUBLIC                ###
# ##################################################


"""
Les immeubles propriété de l'Etat, de la Polynésie française, des communes, des districts, des établissements publics,
lorsqu'ils sont affectés à un service public, ou s'ils sont reconnus d'utilité générale et improductifs de revenus
"""


class eligible_exoneration_permanente_bien_public(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les biens public"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        non_loue = personne('non_loue', period, parameters)
        forme_legale = personne('forme_legale', period, parameters)
        categorie = personne('categorie_du_bien', period, parameters)

        return (forme_legale == FormeLegale.ADM) \
            * (categorie == CategoryBien.ADMINISTRATIF) \
            * non_loue


class exoneration_permanente_bien_public_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les biens public s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_bien_public_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les biens public et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_bien_public', period, parameters)
        applique = personne('exoneration_permanente_bien_public_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_bien_public(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour un bien public"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_permanente_bien_public_eligible_et_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)

        return select(
            [eligible_et_appliquee],
            [brute],
            0
            )


# ##################################################
# ###               LIEUX DE CULTE               ###
# ##################################################


"""
Les édifices servant à l'exercice public des cultes, églises, temples, maisons de réunions religieuses
"""


FORMES_LEGALES_EGLISES = enum_set(
    FormeLegale,
    FormeLegale.EGL,
    FormeLegale.ASSO
    )


class eligible_exoneration_permanente_lieu_de_culte(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les lieux de cultes"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        forme_legale = personne('forme_legale', period, parameters)
        categorie = personne('categorie_du_bien', period, parameters)
        non_loue = personne('non_loue', period, parameters)

        return isin(forme_legale, FORMES_LEGALES_EGLISES) \
            * (categorie == CategoryBien.CULTE) \
            * non_loue


class exoneration_permanente_lieu_de_culte_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les lieux de cultes s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_lieu_de_culte_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les lieux de cultes et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_lieu_de_culte', period, parameters)
        applique = personne('exoneration_permanente_lieu_de_culte_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_lieu_de_culte(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour un lieu de culte"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_permanente_lieu_de_culte_eligible_et_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)
        return select(
            [eligible_et_appliquee],
            [brute],
            0
            )


# ##################################################
# ###            BÂTIMENTS SCOLAIRES             ###
# ##################################################


"""
Les bâtiments scolaires français ou reconnus d'utilité publique
"""


class eligible_exoneration_permanente_batiment_scolaire(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les bâtiments scolaires français ou reconnus d'utilité publique"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        forme_legale = personne('forme_legale', period, parameters)
        categorie = personne('categorie_du_bien', period, parameters)
        non_loue = personne('non_loue', period, parameters)

        return (forme_legale == FormeLegale.ADM) \
            * (categorie == CategoryBien.ENSEIGNEMENT) \
            * non_loue


class exoneration_permanente_batiment_scolaire_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les bâtiments scolaires s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_batiment_scolaire_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les batiments scolaires et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_batiment_scolaire', period, parameters)
        applique = personne('exoneration_permanente_batiment_scolaire_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_batiment_scolaire(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour les bâtiments scolaires français ou reconnus d'utilité publique"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_permanente_batiment_scolaire_eligible_et_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)

        return select(
            [eligible_et_appliquee],
            [brute],
            0
            )


# ##################################################
# ###                 CONSULATS                  ###
# ##################################################


"""
Les bâtiments affectés au service des consulats étrangers lorsqu'ils appartiennent à la nation sous réserve de réciprocité
"""


FORMES_LEGALES_CONSULAT = enum_set(
    FormeLegale,
    FormeLegale.ADM,
    FormeLegale.CONSULAT
    )


class eligible_exoneration_permanente_consulat(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les bâtiments affectés au service des consulats étrangers"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        forme_legale = personne('forme_legale', period, parameters)
        categorie = personne('categorie_du_bien', period, parameters)
        non_loue = personne('non_loue', period, parameters)

        return isin(forme_legale, FORMES_LEGALES_CONSULAT) \
            * (categorie == CategoryBien.CONSULAT) \
            * non_loue


class exoneration_permanente_consulat_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les consulats s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_consulat_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les consulat et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_consulat', period, parameters)
        applique = personne('exoneration_permanente_consulat_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_consulat(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour les bâtiments affectés au service des consulats étrangers"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_permanente_consulat_eligible_et_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)

        return select(
            [eligible_et_appliquee],
            [brute],
            0
            )


# ##################################################
# ###             BÂTIMENTS AGRICOLES            ###
# ##################################################


"""
Les bâtiments servant aux exploitations agricoles pour loger leurs animaux, serrer ou préparer leur propre récolte
"""


class eligible_exoneration_permanente_batiment_agricole(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les bâtiments agricoles"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        categorie = personne('categorie_du_bien', period, parameters)
        non_loue = personne('non_loue', period, parameters)

        # note: les agriculteurs sont labellisés sous de diverses formes légales
        # ce qui ne nous permet pas de contraindre cette exonération à la forme légale du propriétaire
        return (categorie == CategoryBien.AGRICOLE) \
            * non_loue


class exoneration_permanente_batiment_agricole_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les bâtiments agricoles s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_batiment_agricole_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les bâtiments agricoles et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_batiment_agricole', period, parameters)
        applique = personne('exoneration_permanente_batiment_agricole_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_batiment_agricole(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour les bâtiments agricoles"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_permanente_batiment_agricole_eligible_et_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)
        return select(
            [eligible_et_appliquee],
            [brute],
            0
            )


# ##################################################
# ###            BÂTIMENTS ASSOCIATIFS           ###
# ##################################################


"""
Les bâtiments appartenant aux associations ou organismes de bienfaisance,
aux associations sportives ou aux associations culturelles dont le but est autre que le partage des bénéfices
et dont les revenus sont affectés à de telles œuvres, suivant décision du conseil des ministres
"""


class eligible_exoneration_permanente_batiment_associatif(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les bâtiments associatifs"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        forme_legale = personne('forme_legale', period, parameters)
        categorie = personne('categorie_du_bien', period, parameters)
        non_loue = personne('non_loue', period, parameters)

        return (forme_legale == FormeLegale.ASSO) \
            * (categorie == CategoryBien.ASSOCIATIF) \
            * non_loue


class exoneration_permanente_batiment_associatif_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les bâtiments associatif s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_batiment_associatif_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les bâtiments associatifs et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_batiment_associatif', period, parameters)
        applique = personne('exoneration_permanente_batiment_associatif_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_batiment_associatif(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour les bâtiments associatifs"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_batiment_associatif', period, parameters)
        apliquee = personne('exoneration_permanente_batiment_associatif_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)

        return select(
            [eligible * apliquee],
            [brute],
            0
            )


# ##################################################
# ###        HABITATIONS À FAIBLE VALEUR         ###
# ##################################################


"""
A la condition qu'elles servent à la résidence principale de leur propriétaire,
les habitations dont la valeur vénale est égale ou inférieure à 500.000 francs.
"""


class eligible_exoneration_permanente_habitation_principale(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les habitations principales à faible valeur"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        categorie = personne('categorie_du_bien', period, parameters)
        habitation_principale = personne('habitation_principale', period, parameters)
        valeur_venale = personne('valeur_venale', period, parameters)
        non_loue = personne('non_loue', period, parameters)

        return (categorie == CategoryBien.LOGEMENT) \
            * habitation_principale \
            * (valeur_venale <= 500_000) \
            * non_loue


class exoneration_permanente_habitation_principale_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les habitations principales à faible valeur s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_habitation_principale_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les habitations principales et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_habitation_principale', period, parameters)
        applique = personne('exoneration_permanente_habitation_principale_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_habitation_principale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour une habitation principale à faible valeur"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_permanente_habitation_principale_eligible_et_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)

        return select(
            [eligible_et_appliquee],
            [brute],
            0
            )


# ##################################################
# ###              HALLES ET MARCHÉS             ###
# ##################################################


"""
Les halles et marchés municipaux
"""


class eligible_exoneration_permanente_halle_et_marche(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les bâtiments associatifs"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        forme_legale = personne('forme_legale', period, parameters)
        categorie = personne('categorie_du_bien', period, parameters)
        non_loue = personne('non_loue', period, parameters)

        return (forme_legale == FormeLegale.ADM) \
            * (categorie == CategoryBien.COMMERCE) \
            * non_loue


class exoneration_permanente_halle_et_marche_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les halles et marchés s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_halle_et_marche_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les halles et marchés et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_halle_et_marche', period, parameters)
        applique = personne('exoneration_permanente_halle_et_marche_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_halle_et_marche(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour les bâtiments associatifs"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_permanente_halle_et_marche_eligible_et_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)
        return select(
            [eligible_et_appliquee],
            [brute],
            0
            )


# ##################################################
# ###            LOGEMENTS SOCIAUX OPH           ###
# ##################################################


"""
Les immeubles affectés au logement social mis en location dans le cadre de la réglementation relative
à l'habitat social en Polynésie française sont exemptés de l'impôt foncier sur les propriétés bâties
pour toute la durée de la location.
"""


FORMES_LEGALES_OPH = enum_set(
    FormeLegale,
    FormeLegale.ADM,
    FormeLegale.EPIC
    )


class eligible_exoneration_permanente_logement_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente pour les logements sociaux de l'OPH"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        forme_legale = personne('forme_legale', period, parameters)
        categorie = personne('categorie_du_bien', period, parameters)
        logement_social = personne('logement_social', period, parameters)
        loue = personne('loue', period, parameters)

        return isin(forme_legale, FORMES_LEGALES_OPH) \
            * (categorie == CategoryBien.LOGEMENT) \
            * logement_social \
            * loue


class exoneration_permanente_logement_social_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que l'exonération permanente pour les logements sociaux OPH s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class exoneration_permanente_logement_social_eligible_et_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce le bien est éligible à l'exonération permanente pour les logements sociaux et est-ce que cette exonération s'applique à ce bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible = personne('eligible_exoneration_permanente_logement_social', period, parameters)
        applique = personne('exoneration_permanente_logement_social_appliquee', period, parameters)
        return eligible * applique


class montant_exoneration_permanente_logement_social(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'exonération permanente pour les logements sociaux de l'OPH"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_et_appliquee = personne('exoneration_permanente_logement_social_eligible_et_appliquee', period, parameters)
        brute = personne('impot_foncier_part_pays_brute', period, parameters)

        return select(
            [eligible_et_appliquee],
            [brute],
            0
            )


# ##################################################
# ###     APPLICATION EXONERATION PERMANENTE     ###
# ##################################################


class eligible_exoneration_permanente(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien est eligible à une exonération permanente"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        eligible_exoneration_permanente_bien_public = personne('eligible_exoneration_permanente_bien_public', period, parameters)
        eligible_exoneration_permanente_lieu_de_culte = personne('eligible_exoneration_permanente_lieu_de_culte', period, parameters)
        eligible_exoneration_permanente_batiment_scolaire = personne('eligible_exoneration_permanente_batiment_scolaire', period, parameters)
        eligible_exoneration_permanente_consulat = personne('eligible_exoneration_permanente_consulat', period, parameters)
        eligible_exoneration_permanente_batiment_agricole = personne('eligible_exoneration_permanente_batiment_agricole', period, parameters)
        eligible_exoneration_permanente_batiment_associatif = personne('eligible_exoneration_permanente_batiment_associatif', period, parameters)
        eligible_exoneration_permanente_habitation_principale = personne('eligible_exoneration_permanente_habitation_principale', period, parameters)
        eligible_exoneration_permanente_halle_et_marche = personne('eligible_exoneration_permanente_halle_et_marche', period, parameters)
        eligible_exoneration_permanente_logement_social = personne('eligible_exoneration_permanente_logement_social', period, parameters)

        return eligible_exoneration_permanente_bien_public \
            + eligible_exoneration_permanente_lieu_de_culte \
            + eligible_exoneration_permanente_batiment_scolaire \
            + eligible_exoneration_permanente_consulat \
            + eligible_exoneration_permanente_batiment_agricole \
            + eligible_exoneration_permanente_batiment_associatif \
            + eligible_exoneration_permanente_habitation_principale \
            + eligible_exoneration_permanente_halle_et_marche \
            + eligible_exoneration_permanente_logement_social


class exoneration_permanente_appliquee(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce qu'une exonération permanente s'applique au bien"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        exoneration_permanente_bien_public_eligible_et_appliquee = personne('exoneration_permanente_bien_public_eligible_et_appliquee', period, parameters)
        exoneration_permanente_lieu_de_culte_eligible_et_appliquee = personne('exoneration_permanente_lieu_de_culte_eligible_et_appliquee', period, parameters)
        exoneration_permanente_batiment_scolaire_eligible_et_appliquee = personne('exoneration_permanente_batiment_scolaire_eligible_et_appliquee', period, parameters)
        exoneration_permanente_consulat_eligible_et_appliquee = personne('exoneration_permanente_consulat_eligible_et_appliquee', period, parameters)
        exoneration_permanente_batiment_agricole_eligible_et_appliquee = personne('exoneration_permanente_batiment_agricole_eligible_et_appliquee', period, parameters)
        exoneration_permanente_batiment_associatif_eligible_et_appliquee = personne('exoneration_permanente_batiment_associatif_eligible_et_appliquee', period, parameters)
        exoneration_permanente_habitation_principale_eligible_et_appliquee = personne('exoneration_permanente_habitation_principale_eligible_et_appliquee', period, parameters)
        exoneration_permanente_halle_et_marche_eligible_et_appliquee = personne('exoneration_permanente_halle_et_marche_eligible_et_appliquee', period, parameters)
        exoneration_permanente_logement_social_eligible_et_appliquee = personne('exoneration_permanente_logement_social_eligible_et_appliquee', period, parameters)

        return exoneration_permanente_bien_public_eligible_et_appliquee \
            + exoneration_permanente_lieu_de_culte_eligible_et_appliquee \
            + exoneration_permanente_batiment_scolaire_eligible_et_appliquee \
            + exoneration_permanente_consulat_eligible_et_appliquee \
            + exoneration_permanente_batiment_agricole_eligible_et_appliquee \
            + exoneration_permanente_batiment_associatif_eligible_et_appliquee \
            + exoneration_permanente_habitation_principale_eligible_et_appliquee \
            + exoneration_permanente_halle_et_marche_eligible_et_appliquee \
            + exoneration_permanente_logement_social_eligible_et_appliquee


class montant_exoneration_permanente(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant d'exonération permanente"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_1950_11_16(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_exoneration_permanente_bien_public = personne('montant_exoneration_permanente_bien_public', period, parameters)
        montant_exoneration_permanente_lieu_de_culte = personne('montant_exoneration_permanente_lieu_de_culte', period, parameters)
        montant_exoneration_permanente_batiment_scolaire = personne('montant_exoneration_permanente_batiment_scolaire', period, parameters)
        montant_exoneration_permanente_consulat = personne('montant_exoneration_permanente_consulat', period, parameters)
        montant_exoneration_permanente_batiment_agricole = personne('montant_exoneration_permanente_batiment_agricole', period, parameters)
        montant_exoneration_permanente_batiment_associatif = personne('montant_exoneration_permanente_batiment_associatif', period, parameters)
        montant_exoneration_permanente_habitation_principale = personne('montant_exoneration_permanente_habitation_principale', period, parameters)
        montant_exoneration_permanente_halle_et_marche = personne('montant_exoneration_permanente_halle_et_marche', period, parameters)
        montant_exoneration_permanente_logement_social = personne('montant_exoneration_permanente_logement_social', period, parameters)
        return montant_exoneration_permanente_bien_public \
            + montant_exoneration_permanente_lieu_de_culte \
            + montant_exoneration_permanente_batiment_scolaire \
            + montant_exoneration_permanente_consulat \
            + montant_exoneration_permanente_batiment_agricole \
            + montant_exoneration_permanente_batiment_associatif \
            + montant_exoneration_permanente_habitation_principale \
            + montant_exoneration_permanente_halle_et_marche \
            + montant_exoneration_permanente_logement_social
