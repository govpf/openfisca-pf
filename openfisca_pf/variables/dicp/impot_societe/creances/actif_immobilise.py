# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    DAY
    )
from openfisca_pf.entities import Personne


class is_creances_creances_rattachees_a_des_participations_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Créances rattachees à des participations montant brut (7K)"


class is_creances_creances_rattachees_a_des_participations_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Créances rattachees à des participations à un an au plus (7K)"


class is_creances_creances_rattachees_a_des_participations_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Créances rattachees à des participations à plus d'un an (7K)"


class is_creances_prets_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Prêts montant brut (7L)"


class is_creances_prets_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Prêts à un an au plus (7L)"


class is_creances_prets_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Prêts à plus d'un an (7L)"


class is_creances_autres_immobilisations_financieres_montant_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Autres immobilisations financières montant brut (7M)"


class is_creances_autres_immobilisations_financieres_a_un_an_au_plus(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Autres immobilisations financières à un an au plus (7M)"


class is_creances_autres_immobilisations_financieres_a_plus_d_un_an(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Autres immobilisations financières à plus d'un an (7M)"