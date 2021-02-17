# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class type_personne(Variable):
    value_type = Enum
    possible_values = TypePersonne
    default_value = TypePersonne.P
    entity = Entreprise
    definition_period = YEAR
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "L'entreprise peut etre une personne physique(P) ou morale (M)\n\nCela dépend du type de société"
    reference = "https://law.gov.example/salary"  # Always use the most official source

    def formula(entreprise, period, parameters):
        type_societe = entreprise('type_societe', period)
        return where(type_societe == TypeSociete.EI, TypePersonne.P, TypePersonne.M)


class type_societe(Variable):
    value_type = Enum
    possible_values = TypeSociete
    default_value = TypeSociete.EI
    entity = Entreprise
    definition_period = YEAR
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Statuts de la société"
    reference = "https://law.gov.example/salary"  # Always use the most official source


class activite_commerciale(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"L'entreprise pratique une activité commerciale"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        chiffre_affaire_total_ventes = entreprise('chiffre_affaire_total_ventes', period)
        return chiffre_affaire_total_ventes > 0


class activite_prestations(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"L'entreprise pratique une activité de prestations"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        chiffre_affaire_total_ventes = entreprise('chiffre_affaire_total_prestations', period)
        return chiffre_affaire_total_ventes > 0
