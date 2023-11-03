# -*- coding: utf-8 -*-

from openfisca_pf.entities import Pays
from openfisca_pf.base import YEAR, Variable
from openfisca_pf.enums import Archipel


class taux_archipel_australes_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Australes"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_archipel[Archipel.AUSTRALES.name]


class taux_archipel_gambiers_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et des archipels des Gambiers"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_archipel[Archipel.GAMBIERS.name]


class taux_archipel_iles_du_vent_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Îles du vent"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_archipel[Archipel.ILES_DU_VENT.name]


class taux_archipel_iles_sous_le_vent_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Îles sous le vent"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_archipel[Archipel.ILES_SOUS_LE_VENT.name]


class taux_archipel_marquises_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Marquises"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_archipel[Archipel.MARQUISES.name]


class taux_archipel_tuamotus_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et des archipels des Touamotus"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_archipel[Archipel.TUAMOTUS.name]


class taux_logement_social_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.02
    label = "Taux permettant de calculer la valeur locative direct d'un local utilisé comme logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_logement_social


class taux_meuble_tourisme_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.06
    label = "Taux permettant de calculer la valeur locative d'un local loué en meuble de tourisme en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_meuble_tourisme


class premier_degrevement_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Premier dégrèvement appliqué à la valeur locative pour calculer la base imposable de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.degrevement.premier_degrevement


class second_degrevement_si_non_loue_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local n'est pas loué"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.degrevement.second_degrevement_si_non_loue


class second_degrevement_si_loue_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.degrevement.second_degrevement_si_loue_meuble


class second_degrevement_si_loue_non_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en non-meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.degrevement.second_degrevement_si_loue_non_meuble


class taux_part_pays_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la part pays de la contribution à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_pays
