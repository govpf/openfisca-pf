# -*- coding: utf-8 -*-

from openfisca_pf.base import YEAR, Variable
from openfisca_pf.entities import Personne


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

