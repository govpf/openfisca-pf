# -*- coding: utf-8 -*-

import numpy

from openfisca_pf.base import YEAR, Variable
from openfisca_pf.entities import Personne
from openfisca_core.periods import Period
from openfisca_core.parameters import Parameter


class premier_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Premier abattement appliqué à la valeur locative pour calculer la base imposable de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('premier_abattement_pays', period, parameters)


class second_abattement_si_non_loue(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local n'est pas loué"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('second_abattement_si_non_loue_pays', period, parameters)


class second_abattement_si_loue_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('second_abattement_si_loue_meuble_pays', period, parameters)


class second_abattement_si_loue_non_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en non-meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('second_abattement_si_loue_non_meuble_pays', period, parameters)


class second_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Second abattement appliqué pour calculer la base imposable de l'impôt foncier en fonction de sa situation"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):

        loue = local('loue', period, parameters)
        meuble = local('meuble', period, parameters)
        non_meuble = local('non_meuble', period, parameters)
        second_abattement_si_non_loue = local('second_abattement_si_non_loue', period, parameters)
        second_abattement_si_loue_meuble = local('second_abattement_si_loue_meuble', period, parameters)
        second_abattement_si_loue_non_meuble = local('second_abattement_si_loue_non_meuble', period, parameters)
        return numpy.select(
            [loue and meuble, loue and non_meuble],
            [second_abattement_si_loue_meuble, second_abattement_si_loue_non_meuble],
            second_abattement_si_non_loue
            )
