# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    date,
    Enum,
    ETERNITY,
    isin,
    max_,
    not_,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_foncier import CategoryBien, TypeLocation, MEUBLE_OU_NON_MEUBLE
from openfisca_pf.functions.time import annee_de_la_date


class age_du_bien(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Age du bien immobilier calculé à partir de la date de fin des travaux et la periode"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_fin_des_travaux = personne('date_de_fin_des_travaux', period)
        return max_(
            period.date.year - annee_de_la_date(date_de_fin_des_travaux),
            0
            )


class annee_actuelle(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Année à partir de laquelle le bien est soumis à l'impôt foncier"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return period.start.year


class annee_premiere_imposition(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Année à partir de laquelle le bien est soumis à l'impôt foncier"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        date_de_fin_des_travaux = personne('date_de_fin_des_travaux', period)
        return annee_de_la_date(date_de_fin_des_travaux) + 1


class categorie_du_bien(Variable):
    value_type = Enum
    possible_values = CategoryBien
    entity = Personne
    definition_period = YEAR
    default_value = CategoryBien.AUTRE
    label = "Catégorie du bien servant à préciser comment le bien est utilisé"


class date_du_permis_de_construire(Variable):
    value_type = date
    entity = Personne
    definition_period = ETERNITY
    default_value = date(1970, 1, 1)
    label = "Date du permis de construire."


class date_du_certificat_de_conformite(Variable):
    value_type = date
    entity = Personne
    definition_period = ETERNITY
    default_value = date(1970, 1, 1)
    label = "Date du certificat de conformité."


class date_de_fin_des_travaux(Variable):
    value_type = date
    entity = Personne
    definition_period = ETERNITY
    default_value = date(1970, 1, 1)
    label = "Date de la fin des travaux de construction du bien immobilier. Elle est égale à la date du certificat de conformité si cette dernière est connue."

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('date_du_certificat_de_conformite', period)


class habitation_principale(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est une habitation principale, False sinon."


class location_meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en meublé, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        loue = personne('loue', period)
        type_de_location = personne('type_de_location', period)
        return loue * (type_de_location == TypeLocation.MEUBLE)


class location_meuble_de_tourisme(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en meublé de tourisme (Air B&B par exemple), False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        loue = personne('loue', period)
        type_de_location = personne('type_de_location', period)
        return loue * (type_de_location == TypeLocation.MEUBLE_DE_TOURISME)


class location_non_meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en non-meublé, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Population, period: Period, parameters: ParameterNode):
        loue = personne('loue', period)
        type_de_location = personne('type_de_location', period)
        return loue * (type_de_location == TypeLocation.NON_MEUBLE)


class location_simple(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en meublé ou en non meublé mais pas en meublé de tourisme ni en villa de luxe, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        loue = personne('loue', period)
        type_de_location = personne('type_de_location', period)
        return loue * isin(type_de_location, MEUBLE_OU_NON_MEUBLE)


class location_villa_de_luxe(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué en villa de luxe, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        loue = personne('loue', period)
        type_de_location = personne('type_de_location', period)
        return loue * (type_de_location == TypeLocation.VILLA_DE_LUXE)


class logement_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est un logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class logement_non_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = True
    label = "True si le bien n'est pas un logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        logement_social = personne('logement_social', period)
        return not_(logement_social)


class loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le bien est loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class loyer_de_janvier(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Loyer de janvier percu pour la location bien immobilier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class non_loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = True
    label = "True si le bien n'est pas loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        loue = personne('loue', period)
        return not_(loue)


class bien_occupe_avant_la_fin_des_travaux(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "Est-ce que le bien à été occupé avant la fin des travaux, auquel cas il ne sera pas eligible à une exoneration temporaraire de dix ans pour les habitations principale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class terrain(Variable):
    value_type = bool
    entity = Personne
    definition_period = ETERNITY
    default_value = False
    label = "True si le bien immobilier est un terrain, sinon False."


class type_de_location(Variable):
    value_type = Enum
    possible_values = TypeLocation
    entity = Personne
    definition_period = YEAR
    default_value = TypeLocation.NON_MEUBLE
    label = "Type de location qui est faite du bien immobilier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class valeur_venale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur vénale du bien immobilier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"
