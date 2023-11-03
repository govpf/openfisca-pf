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
                numpy.isin(commune, COMMUNES_DES_ILES_DU_VENT),
                numpy.isin(commune, COMMUNES_DES_ILES_SOUS_LE_VENT),
                numpy.isin(commune, COMMUNES_DES_MARQUISES),
                numpy.isin(commune, COMMUNES_DES_TUAMOTUS_ET_DES_GAMBIERS)
                ],
            [
                Archipel.AUSTRALES,
                Archipel.ILES_DU_VENT,
                Archipel.ILES_SOUS_LE_VENT,
                Archipel.MARQUISES,
                Archipel.TUAMOTUS_ET_GAMBIERS
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


class taux_archipel(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel du local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        archipel = local('archipel', period, parameters)
        taux_archipel_australes_pays = local.pays('taux_archipel_australes_pays', period, parameters)
        taux_archipel_iles_du_vent_pays = local.pays('taux_archipel_iles_du_vent_pays', period, parameters)
        taux_archipel_iles_sous_le_vent_pays = local.pays('taux_archipel_iles_sous_le_vent_pays', period, parameters)
        taux_archipel_marquises_pays = local.pays('taux_archipel_marquises_pays', period, parameters)
        taux_archipel_tuamotus_et_gambiers_pays = local.pays('taux_archipel_tuamotus_et_gambiers_pays', period, parameters)
        return numpy.select(
            [archipel == Archipel.AUSTRALES, archipel == Archipel.ILES_DU_VENT, archipel == Archipel.ILES_SOUS_LE_VENT, archipel == Archipel.MARQUISES, archipel == Archipel.TUAMOTUS_ET_GAMBIERS],
            [taux_archipel_australes_pays, taux_archipel_iles_du_vent_pays, taux_archipel_iles_sous_le_vent_pays, taux_archipel_marquises_pays, taux_archipel_tuamotus_et_gambiers_pays]
            )


class taux_logement_social(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct d'un local utilisé comme logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_logement_social_pays', period, parameters)


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


class taux_meuble_tourisme(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.06
    label = "Taux permettant de calculer la valeur locative d'un local loué en meuble de tourisme en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_meuble_tourisme_pays', period, parameters)


class valeur_locative_meuble_tourisme(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local loué en meuble de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        valeur_venale = local('valeur_venale', period, parameters)
        taux_meuble_tourisme = local('taux_meuble_tourisme', period, parameters)
        return taux_meuble_tourisme * valeur_venale


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
            [loue * not_(meuble_de_tourisme), loue * meuble_de_tourisme, not_(loue)],
            [valeur_locative_loyers, valeur_locative_meuble_tourisme, valeur_locative_direct]
            )


class degrevement_base_seule(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Premier dégrèvement appliqué à la valeur locative pour calculer la base imposable de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('degrevement_base_seule_pays', period, parameters)


class degrevement_base_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('degrevement_base_meuble_pays', period, parameters)


class degrevement_base_non_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en non-meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('degrevement_base_non_meuble_pays', period, parameters)


class base_imposable_apres_premier_degrevement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier non finale apres application du premier degrevement"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        valeur_locative = local('valeur_locative', period, parameters)
        premier_degrevement = local('degrevement_base_seule', period, parameters)
        return valeur_locative * (1.0 - premier_degrevement)


class base_imposable(Variable):
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
        degrevement_base_meuble = local('degrevement_base_meuble', period, parameters)
        degrevement_base_non_meuble = local('degrevement_base_non_meuble', period, parameters)
        second_degrevement = numpy.select(
            [loue * meuble, loue * not_(meuble), not_(loue)],
            [degrevement_base_meuble, degrevement_base_non_meuble, 0]
            )
        return base_imposable_apres_premier_degrevement * (1.0 - second_degrevement)


class taux_part_pays(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la part pays de la contribution à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_part_pays_pays', period, parameters)


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


class taux_part_commune(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux utilisé pour calculer la contribution foncière allant à la commune"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        commune = local('commune', period, parameters)
        return parameters(period).dicp.impot_foncier.taux_centime_additionnel_communal[commune]


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
