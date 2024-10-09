# -*- coding: utf-8 -*-

from openfisca_pf.entities import Pays
from openfisca_pf.base import YEAR, Variable


class premier_abattement_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Premier abattement appliqué à la valeur locative pour calculer la base imposable de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.abattements.premier


class second_abattement_si_non_loue_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local n'est pas loué"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.abattements.second_si_non_loue


class second_abattement_si_loue_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.abattements.second_si_loue_meuble


class second_abattement_si_loue_non_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en non-meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.abattements.second_si_loue_non_meuble
