# -*- coding: utf-8 -*-
import numpy
from openfisca_core.model_api import not_, YEAR, Variable
from openfisca_core.periods import Period
from openfisca_core.parameters import Parameter
from openfisca_pf.entities import Personne
from openfisca_pf.enums.geographie import *


class Destination(Enum):
    NON_LOUE = "NON_LOUE"
    LOUE = "LOUE"
    LOUE_MEUBLE = "LOUE_MEUBLE"
    MEUBLE_DE_TOURISME = "MEUBLE_DE_TOURISME"
    VILLA_DE_LUXE = "VILLA_DE_LUXE"
    LOGEMENT_SOCIAL = "LOGEMENT_SOCIAL"


DESTINATIONS_CORRESPONDANTS_A_DE_LA_LOCATION = Destination.encode(numpy.asarray([
    Destination.LOUE,
    Destination.LOUE_MEUBLE
    ]))


DESTINATIONS_NE_CORRESPONDANTS_PAS_A_DE_LA_LOCATION = Destination.encode(numpy.asarray([
    Destination.NON_LOUE,
    Destination.MEUBLE_DE_TOURISME,
    Destination.VILLA_DE_LUXE,
    Destination.LOGEMENT_SOCIAL
    ]))


class destination(Variable):
    value_type = Enum
    possible_values = Destination
    entity = Personne
    definition_period = YEAR
    default_value = Destination.NON_LOUE
    label = "Destination du local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class valeur_venale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur vénale d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class loyer_janvier(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Loyer de janvier d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class somme_des_tarifs_de_la_nuitee_factures(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Chiffre d'affaire annuel d'un local loué en meuble de tourisme, hors promotions"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class villa_de_luxe(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en villa de luxe, sinon False."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        destination = local('destination', period, parameters)
        return destination == Destination.VILLA_DE_LUXE


class non_loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = True
    label = "True si le local est non-loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        destination = local('destination', period, parameters)
        return numpy.isin(destination, DESTINATIONS_NE_CORRESPONDANTS_PAS_A_DE_LA_LOCATION)


class logement_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est utilisé comme logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        destination = local('destination', period, parameters)
        return destination == Destination.LOGEMENT_SOCIAL


class loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        destination = local('destination', period, parameters)
        return numpy.isin(destination, DESTINATIONS_CORRESPONDANTS_A_DE_LA_LOCATION)


class meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en meublé, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        destination = local('destination', period, parameters)
        return destination == Destination.LOUE_MEUBLE


class meuble_de_tourisme(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en meublé de tourisme (Air B&B par exemple), False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        destination = local('destination', period, parameters)
        return destination == Destination.MEUBLE_DE_TOURISME


class valeur_locative_loyers(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative calculer grace aux loyers d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        loyer_janvier = local('loyer_janvier', period, parameters)
        return loyer_janvier * 12


class valeur_locative_direct(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative direct d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        logement_social = local('logement_social', period, parameters)
        valeur_venale = local('valeur_venale', period, parameters)
        taux_archipel = local('taux_archipel', period, parameters)
        taux_logement_social = local('taux_logement_social', period, parameters)
        taux = numpy.where(logement_social, taux_logement_social, taux_archipel)
        return taux * valeur_venale


class valeur_locative_sociale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative direct d'un local utilisé comme logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_logement_social = local('taux_logement_social', period, parameters)
        return valeur_venale * taux_logement_social


class valeur_locative_meuble_tourisme(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local loué en meuble de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_meuble_de_tourisme = local('taux_meuble_de_tourisme', period, parameters)
        return taux_meuble_de_tourisme * valeur_venale


class valeur_locative_villa_de_luxe(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local loué en villa de luxe"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_villa_de_luxe = local('taux_villa_de_luxe', period, parameters)
        return taux_villa_de_luxe * valeur_venale


class valeur_locative(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):

        logement_social = local('logement_social', period, parameters)
        loue = local('loue', period, parameters)
        meuble_de_tourisme = local('meuble_de_tourisme', period, parameters)
        villa_de_luxe = local('villa_de_luxe', period, parameters)

        valeur_locative_direct = local('valeur_locative_direct', period, parameters)
        valeur_locative_sociale = local('valeur_locative_sociale', period, parameters)
        valeur_locative_loyers = local('valeur_locative_loyers', period, parameters)
        valeur_locative_meuble_tourisme = local('valeur_locative_meuble_tourisme', period, parameters)
        valeur_locative_villa_de_luxe = local('valeur_locative_villa_de_luxe', period, parameters)

        return numpy.select(
            [logement_social, loue, meuble_de_tourisme, villa_de_luxe],
            [valeur_locative_sociale, valeur_locative_loyers, valeur_locative_meuble_tourisme, valeur_locative_villa_de_luxe],
            valeur_locative_direct
            )


class meuble_de_tourisme_eligible_a_un_degrevement(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local loue en meuble de tourisme est eligible à un degrevement, False sinon"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        somme_des_tarifs_de_la_nuitee_factures = local('somme_des_tarifs_de_la_nuitee_factures', period, parameters)
        valeur_locative_meuble_tourisme = local('valeur_locative_meuble_tourisme', period, parameters)
        return somme_des_tarifs_de_la_nuitee_factures <= (0.25 * valeur_locative_meuble_tourisme)


class meuble_de_tourisme_demande_un_degrevement(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le proprietaire du local loue en meuble de tourisme demande degrevement, False sinon"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        return local('meuble_de_tourisme_eligible_a_un_degrevement', period, parameters)


class meuble_de_tourisme_est_eligible_et_demande_un_degrevement(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local loue en meuble de tourisme est eligible à un degrevement et en a fait la demande, False sinon"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        meuble_de_tourisme_eligible_a_un_degrevement = local('meuble_de_tourisme_eligible_a_un_degrevement', period, parameters)
        meuble_de_tourisme_demande_un_degrevement = local('meuble_de_tourisme_demande_un_degrevement', period, parameters)
        return meuble_de_tourisme_eligible_a_un_degrevement * meuble_de_tourisme_demande_un_degrevement


class base_imposable_apres_premier_degrevement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier non finale apres application du premier degrevement"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        valeur_locative = local('valeur_locative', period, parameters)
        premier_degrevement = local('premier_degrevement', period, parameters)
        return valeur_locative * (1.0 - premier_degrevement)


class base_imposable_apres_second_degrevement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier utilisé pour calculer la part du territoire et la part comunale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        base_imposable_apres_premier_degrevement = local('base_imposable_apres_premier_degrevement', period, parameters)
        loue = local('loue', period, parameters)
        meuble = local('meuble', period, parameters)
        second_degrevement_si_non_loue = local('second_degrevement_si_non_loue', period, parameters)
        second_degrevement_si_loue_meuble = local('second_degrevement_si_loue_meuble', period, parameters)
        second_degrevement_si_loue_non_meuble = local('second_degrevement_si_loue_non_meuble', period, parameters)
        second_degrevement = numpy.select(
            [not_(loue), meuble, not_(meuble)],
            [second_degrevement_si_non_loue, second_degrevement_si_loue_meuble, second_degrevement_si_loue_non_meuble]
            )
        return base_imposable_apres_premier_degrevement * (1.0 - second_degrevement)


class base_imposable(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier utilisé pour calculer la part du territoire et la part comunale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        base_imposable_apres_second_degrevement = local('base_imposable_apres_second_degrevement', period, parameters)
        meuble_de_tourisme = local('meuble_de_tourisme', period, parameters)
        degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme = local('degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme', period, parameters)
        return numpy.where(
            meuble_de_tourisme,
            base_imposable_apres_second_degrevement * (1.0 - degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme),
            base_imposable_apres_second_degrevement
            )


class contribution_fonciere_part_pays(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'impot foncier allant au territoire"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        base_imposable = local('base_imposable', period, parameters)
        taux_part_pays = local('taux_part_pays', period, parameters)
        return base_imposable * taux_part_pays


class contribution_fonciere_part_commune(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'impot foncier allant à la commune"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        contribution_fonciere_part_pays = local('contribution_fonciere_part_pays', period, parameters)
        taux_part_commune = local('taux_part_commune', period, parameters)
        return contribution_fonciere_part_pays * taux_part_commune


class contribution_fonciere(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant total de l'impot foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        contribution_fonciere_part_pays = local('contribution_fonciere_part_pays', period, parameters)
        contribution_fonciere_part_commune = local('contribution_fonciere_part_commune', period, parameters)
        return contribution_fonciere_part_pays + contribution_fonciere_part_commune
