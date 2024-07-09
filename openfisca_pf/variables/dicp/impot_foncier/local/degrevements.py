# -*- coding: utf-8 -*-

import numpy

from openfisca_pf.base import YEAR, Variable
from openfisca_pf.entities import Personne


class degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Dégrèvement sur demande dans le cas d'une baisse de revenus d'un local loué en meublé de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme_pays = local.pays('degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme_pays', period, parameters)
        meuble_de_tourisme_est_eligible_et_demande_un_degrevement = local('meuble_de_tourisme_est_eligible_et_demande_un_degrevement', period, parameters)
        return numpy.where(meuble_de_tourisme_est_eligible_et_demande_un_degrevement, degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme_pays, 0)
