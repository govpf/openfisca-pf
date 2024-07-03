# -*- coding: utf-8 -*-

from openfisca_pf.base import YEAR, Variable
from openfisca_pf.entities import Pays


class degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Dégrèvement sur demande dans le cas d'une baisse de revenus d'un local loué en meublé de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.degrevement.pour_baisse_de_revenus_loue_en_meuble_de_tourisme
