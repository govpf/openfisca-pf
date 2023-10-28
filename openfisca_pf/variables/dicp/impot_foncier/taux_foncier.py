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


class taux_archipel_tuamotus_et_gambiers_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et des archipels des Touamotus et des Gambiers"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_archipel[Archipel.TUAMOTUS_ET_GAMBIERS.name]


class taux_logement_social_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct d'un local utilisé comme logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_logement_social


class degrevement_base_seule_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Premier dégrèvement appliqué à la valeur locative pour calculer la base imposable de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.degrevement.base_seule


class degrevement_base_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.degrevement.base_meuble


class degrevement_base_non_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en non-meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.degrevement.base_non_meuble


class taux_part_pays_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la part pays de la contribution à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux_pays
