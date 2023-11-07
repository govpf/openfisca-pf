# -*- coding: utf-8 -*-

import numpy

from openfisca_core.model_api import not_
from openfisca_pf.entities import Personne
from openfisca_pf.base import YEAR, Variable
from openfisca_pf.enums import *


class commune(Variable):
    value_type = Enum
    possible_values = Commune
    entity = Personne
    definition_period = YEAR
    default_value = Commune.PAPEETE
    label = "Cammune a laquelle le local est rataché"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class archipel(Variable):
    value_type = Enum
    possible_values = Archipel
    entity = Personne
    definition_period = YEAR
    default_value = Archipel.ILES_SOUS_LE_VENT
    label = "Archipel auquel le local appartient"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        commune = local('commune', period, parameters)
        return numpy.select(
            [
                numpy.isin(commune, COMMUNES_DES_AUSTRALES),
                numpy.isin(commune, COMMUNES_DES_GAMBIERS),
                numpy.isin(commune, COMMUNES_DES_ILES_DU_VENT),
                numpy.isin(commune, COMMUNES_DES_ILES_SOUS_LE_VENT),
                numpy.isin(commune, COMMUNES_DES_MARQUISES),
                numpy.isin(commune, COMMUNES_DES_TUAMOTUS)
                ],
            [
                Archipel.AUSTRALES,
                Archipel.GAMBIERS,
                Archipel.ILES_DU_VENT,
                Archipel.ILES_SOUS_LE_VENT,
                Archipel.MARQUISES,
                Archipel.TUAMOTUS
                ]
            )


class logement_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est utilisé comme logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en meublé, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class meuble_de_tourisme(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en meublé de tourisme (Air B&B par exemple), False sinon."
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


class valeur_locative_loyers(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative calculer grace aux loyers d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        loyer_janvier = local('loyer_janvier', period, parameters)
        return loyer_janvier * 12


class valeur_locative_direct(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative direct d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        logement_social = local('logement_social', period, parameters)
        valeur_venale = local('valeur_venale', period, parameters)
        taux_archipel = local('taux_archipel', period, parameters)
        taux_logement_social = local('taux_logement_social', period, parameters)
        taux = numpy.where(logement_social, taux_logement_social, taux_archipel)
        return taux * valeur_venale


class valeur_locative_meuble_tourisme(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local loué en meuble de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_meuble_de_tourisme = local('taux_meuble_de_tourisme', period, parameters)
        return taux_meuble_de_tourisme * valeur_venale


class meuble_de_tourisme_eligible_a_un_degrevement(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local loue en meuble de tourisme est eligible à un degrevement, False sinon"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
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

    def formula(local, period, parameters):
        return local('meuble_de_tourisme_eligible_a_un_degrevement', period, parameters)


class meuble_de_tourisme_est_eligible_et_demande_un_degrevement(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local loue en meuble de tourisme est eligible à un degrevement et en a fait la demande, False sinon"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        meuble_de_tourisme_eligible_a_un_degrevement = local('meuble_de_tourisme_eligible_a_un_degrevement', period, parameters)
        meuble_de_tourisme_demande_un_degrevement = local('meuble_de_tourisme_demande_un_degrevement', period, parameters)
        return meuble_de_tourisme_eligible_a_un_degrevement * meuble_de_tourisme_demande_un_degrevement


class valeur_locative(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        loue = local('loue', period, parameters)
        meuble_de_tourisme = local('meuble_de_tourisme', period, parameters)
        valeur_locative_loyers = local('valeur_locative_loyers', period, parameters)
        valeur_locative_direct = local('valeur_locative_direct', period, parameters)
        valeur_locative_meuble_tourisme = local('valeur_locative_meuble_tourisme', period, parameters)
        return numpy.select(
            [not_(loue), loue * not_(meuble_de_tourisme), loue * meuble_de_tourisme],
            [valeur_locative_direct, valeur_locative_loyers, valeur_locative_meuble_tourisme]
            )


class base_imposable_apres_premier_degrevement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier non finale apres application du premier degrevement"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
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

    def formula(local, period, parameters):
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

    def formula(local, period, parameters):
        base_imposable_apres_second_degrevement = local('base_imposable_apres_second_degrevement', period, parameters)
        degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme = local('degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme', period, parameters)
        return base_imposable_apres_second_degrevement * (1.0 - degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme)


class contribution_fonciere_part_pays(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'impot foncier allant au territoire"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        taux_part_pays = local('taux_part_pays', period, parameters)
        base_imposable = local('base_imposable', period, parameters)
        return taux_part_pays * base_imposable


class contribution_fonciere_part_commune(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'impot foncier allant à la commune"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        taux_part_commune = local('taux_part_commune', period, parameters)
        contribution_fonciere_part_pays = local('contribution_fonciere_part_pays', period, parameters)
        return taux_part_commune * contribution_fonciere_part_pays


class contribution_fonciere(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant total de l'impot foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        contribution_fonciere_part_pays = local('contribution_fonciere_part_pays', period, parameters)
        contribution_fonciere_part_commune = local('contribution_fonciere_part_commune', period, parameters)
        return contribution_fonciere_part_pays + contribution_fonciere_part_commune
