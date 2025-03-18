from openfisca_core.model_api import DAY, Variable
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne


class is_resultat_courant_avant_impots(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Résultat courant avant impôt (GW)"

    def formula(person, period):
        exploitation = person('is_resultat_exploitation', period)
        financier = person('is_resultat_financier', period)
        return exploitation + financier


class is_resultat_impots_benefices(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Impôts sur les bénéfices (HK)"


class is_resultat_total_produits(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total des produits (HL)"

    def formula(person, period):
        exploitation = person('is_resultat_exploitation_total_produits', period)
        financier = person('is_resultat_financier_total_produits', period)
        exceptionnel = person('is_resultat_exceptionnel_total_produits', period)
        return exploitation + financier + exceptionnel


class is_resultat_total_charges(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total des charges (HM)"

    def formula(person, period):
        exploitation = person('is_resultat_exploitation_total_charges', period)
        financier = person('is_resultat_financier_total_charges', period)
        exceptionnel = person('is_resultat_exceptionnel_total_charges', period)
        impot = person('is_resultat_impots_benefices', period)
        return exploitation + financier + exceptionnel + impot


class is_resultat_benefice_ou_perte(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Bénéfice ou perte (HN)"

    def formula(person, period):
        produits = person('is_resultat_total_produits', period)
        charges = person('is_resultat_total_charges', period)
        return produits - charges
