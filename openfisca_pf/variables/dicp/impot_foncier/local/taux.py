# -*- coding: utf-8 -*-

from openfisca_pf.entities import Personne
from openfisca_pf.base import YEAR, Variable
from openfisca_pf.enums.geographie import *


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
        taux_archipel_gambiers_pays = local.pays('taux_archipel_gambiers_pays', period, parameters)
        taux_archipel_iles_du_vent_pays = local.pays('taux_archipel_iles_du_vent_pays', period, parameters)
        taux_archipel_iles_sous_le_vent_pays = local.pays('taux_archipel_iles_sous_le_vent_pays', period, parameters)
        taux_archipel_marquises_pays = local.pays('taux_archipel_marquises_pays', period, parameters)
        taux_archipel_tuamotus_pays = local.pays('taux_archipel_tuamotus_pays', period, parameters)
        return numpy.select(
            [
                archipel == Archipel.AUSTRALES,
                archipel == Archipel.GAMBIERS,
                archipel == Archipel.ILES_DU_VENT,
                archipel == Archipel.ILES_SOUS_LE_VENT,
                archipel == Archipel.MARQUISES,
                archipel == Archipel.TUAMOTUS
            ],
            [
                taux_archipel_australes_pays,
                taux_archipel_gambiers_pays,
                taux_archipel_iles_du_vent_pays,
                taux_archipel_iles_sous_le_vent_pays,
                taux_archipel_marquises_pays,
                taux_archipel_tuamotus_pays
            ])


class taux_logement_social(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.02
    label = "Taux permettant de calculer la valeur locative direct d'un local utilisé comme logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_logement_social_pays', period, parameters)


class taux_meuble_de_tourisme(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.06
    label = "Taux permettant de calculer la valeur locative d'un local loué en meuble de tourisme en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_meuble_de_tourisme_pays', period, parameters)


class taux_villa_de_luxe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.06
    label = "Taux permettant de calculer la valeur locative d'un local loué en villa de luxe en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_villa_de_luxe_pays', period, parameters)


class taux_part_pays(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la part pays de la contribution à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_part_pays_pays', period, parameters)


class taux_part_commune(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux utilisé pour calculer la contribution foncière allant à la commune"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        commune = local('commune', period, parameters)
        return parameters(period).dicp.impot_foncier.taux.commune[commune]
