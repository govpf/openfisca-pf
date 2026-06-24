# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    YEAR,
    ParameterNode,
    Period,
    Population,
    Variable
    )
from openfisca_pf.entities import Personne


# Versés hors du Territoire
class is_salaires_verses_hors_territoire_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Versés hors du Territoire, Dirigeant et associés de l'entreprise"


class is_salaires_verses_hors_territoire_non_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Versés hors du Territoire, Personnel salarié non dirigeant"


class is_salaires_verses_hors_territoire_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Versés hors du Territoire, Total"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        dirigeant = personne('is_salaires_verses_hors_territoire_dirigeant', period, parameters)
        non_dirigeant = personne('is_salaires_verses_hors_territoire_non_dirigeant', period, parameters)
        return dirigeant + non_dirigeant


# Versés dans le Territoire
class is_salaires_verses_dans_territoire_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Versés dans le Territoire , Dirigeant et associés de l'entreprise"


class is_salaires_verses_dans_territoire_non_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Versés dans le Territoire, Personnel salarié non dirigeant"


class is_salaires_verses_dans_territoire_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Versés dans le Territoire, Total"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        dirigeant = personne('is_salaires_verses_dans_territoire_dirigeant', period, parameters)
        non_dirigeant = personne('is_salaires_verses_dans_territoire_non_dirigeant', period, parameters)
        return dirigeant + non_dirigeant


# TOTAL 3
class is_salaires_verses_dirigeant_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Dirigeant et associés de l'entreprise"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        hors_territoire = personne('is_salaires_verses_hors_territoire_dirigeant', period, parameters)
        dans_territoire = personne('is_salaires_verses_dans_territoire_dirigeant', period, parameters)
        return hors_territoire + dans_territoire


class is_salaires_verses_non_dirigeant_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Personnel salarié non dirigeant"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        hors_territoire = personne('is_salaires_verses_hors_territoire_non_dirigeant', period, parameters)
        dans_territoire = personne('is_salaires_verses_dans_territoire_non_dirigeant', period, parameters)
        return hors_territoire + dans_territoire


class is_salaires_verses_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Traitements et salaires bruts de l'exercice, Total"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        dirigeant = personne('is_salaires_verses_dirigeant_total', period, parameters)
        non_dirigeant = personne('is_salaires_verses_non_dirigeant_total', period, parameters)
        return dirigeant + non_dirigeant


# Charges sociales déductibles
class is_charges_sociales_deductibles_verses_dans_territoire_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Charges sociales déductibles, Dirigeant et associés de l'entreprise"


class is_charges_sociales_deductibles_verses_dans_territoire_non_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Charges sociales déductibles, Personnel salarié non dirigeant"


class is_charges_sociales_deductibles_verses_dans_territoire_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Charges sociales déductibles, Total"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        dirigeant = personne('is_charges_sociales_deductibles_verses_dans_territoire_dirigeant', period, parameters)
        non_dirigeant = personne('is_charges_sociales_deductibles_verses_dans_territoire_non_dirigeant', period, parameters)
        return dirigeant + non_dirigeant


# Traitements et salaires nets déductibles
class is_salaires_deductibles_verses_dans_territoire_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Traitements et salaires nets déductibles, Dirigeant et associés de l'entreprise"


class is_salaires_deductibles_verses_dans_territoire_non_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Traitements et salaires nets déductibles, Personnel salarié non dirigeant"


class is_salaires_deductibles_verses_dans_territoire_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Traitements et salaires nets déductibles, Total"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        dirigeant = personne('is_salaires_deductibles_verses_dans_territoire_dirigeant', period, parameters)
        non_dirigeant = personne('is_salaires_deductibles_verses_dans_territoire_non_dirigeant', period, parameters)
        return dirigeant + non_dirigeant


# TOTAL 6
class is_deductibles_verses_dans_territoire_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Dirigeant et associés de l'entreprise"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        charges_sociales = personne('is_charges_sociales_deductibles_verses_dans_territoire_dirigeant', period, parameters)
        salaires = personne('is_salaires_deductibles_verses_dans_territoire_dirigeant', period, parameters)
        return charges_sociales + salaires


class is_deductibles_verses_dans_territoire_non_dirigeant(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Personnel salarié non dirigeant"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        charges_sociales = personne('is_charges_sociales_deductibles_verses_dans_territoire_non_dirigeant', period, parameters)
        salaires = personne('is_salaires_deductibles_verses_dans_territoire_non_dirigeant', period, parameters)
        return charges_sociales + salaires


class is_deductibles_verses_dans_territoire_total(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dépense de personnel de l'Exercice, Dépenses de personnel déductibles versées dans le territoire, Total"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        dirigeant = personne('is_deductibles_verses_dans_territoire_dirigeant', period, parameters)
        non_dirigeant = personne('is_deductibles_verses_dans_territoire_non_dirigeant', period, parameters)
        return dirigeant + non_dirigeant
