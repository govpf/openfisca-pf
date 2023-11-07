# -*- coding: utf-8 -*-

import numpy

from openfisca_pf.entities import Personne
from openfisca_pf.base import YEAR, Variable


class premier_degrevement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Premier dégrèvement appliqué à la valeur locative pour calculer la base imposable de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('premier_degrevement_pays', period, parameters)


class second_degrevement_si_non_loue(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local n'est pas loué"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('second_degrevement_si_non_loue_pays', period, parameters)


class second_degrevement_si_loue_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('second_degrevement_si_loue_meuble_pays', period, parameters)


class second_degrevement_si_loue_non_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second dégrèvement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en non-meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('second_degrevement_si_loue_non_meuble_pays', period, parameters)


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
