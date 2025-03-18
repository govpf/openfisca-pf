from openfisca_core.model_api import DAY, Variable
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne


# Produits
class is_resultat_financier_participations(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Produits financiers de participations (GJ)"


class is_resultat_financier_valeurs_mobilieres(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Produits des autres valeurs mobilières et créances de l'actif immobilisé (GK)"


class is_resultat_financier_autres_interets(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Autres intérêts et produits assimilés (GL)"


class is_resultat_financier_transfert_charges(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Reprises sur provisions et transfert de charges (GM)"


class is_resultat_financier_differences_positives_change(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Différences positives de change (GN)"


class is_resultat_financier_total_produits(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total des produits financiers (GP)"

    def formula(person, period):
        participation = person('is_resultat_financier_participations', period)
        immobilier = person('is_resultat_financier_valeurs_mobilieres', period)
        interets = person('is_resultat_financier_autres_interets', period)
        charges = person('is_resultat_financier_transfert_charges', period)
        change = person('is_resultat_financier_differences_positives_change', period)
        return participation + immobilier + interets + charges + change


# Charges
class is_resultat_financier_charges_interets(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Intérêts et charges assimilées (GR)"


class is_resultat_financier_differences_negative_change(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Différence négative de change (GS)"


class is_resultat_financier_total_charges(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total des charges financières (GU)"

    def formula(person, period):
        interets = person('is_resultat_financier_charges_interets', period)
        change = person('is_resultat_financier_differences_negative_change', period)
        return interets + change


# Résultat financier
class is_resultat_financier(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Total des charges financières (GV)"

    def formula(person, period):
        produits = person('is_resultat_financier_total_produits', period)
        charges = person('is_resultat_financier_total_charges', period)
        return produits - charges
