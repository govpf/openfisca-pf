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
    entity = Personne
    definition_period = YEAR
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "L'entreprise peut etre une personne physique(P) ou morale (M)\n\nCela dépend du type de société"
    reference = "https://law.gov.example/salary"  # Always use the most official source

    def formula(personne, period, parameters):
        type_societe = personne('type_societe', period)
        return where(type_societe == TypeSociete.EI, TypePersonne.P, TypePersonne.M)


class type_societe(Variable):
    value_type = Enum
    possible_values = TypeSociete
    default_value = TypeSociete.EI
    entity = Personne
    definition_period = YEAR
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Statuts de la société"
    reference = "https://law.gov.example/salary"  # Always use the most official source


class activite_commerciale(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"L'entreprise pratique une activité commerciale"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        chiffre_affaire_total_ventes = personne('chiffre_affaire_total_ventes', period)
        return chiffre_affaire_total_ventes > 0


class activite_prestations(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"L'entreprise pratique une activité de prestations"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(personne, period, parameters):
        chiffre_affaire_total_ventes = personne('chiffre_affaire_total_prestations', period)
        return chiffre_affaire_total_ventes > 0


class nombre_entreprises_contribuables_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays"

    def formula(pays, period, parameters):
        return pays.nb_persons(Pays.CONTRIBUABLES)


class chiffre_affaire_prestations_contribuables_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Chiffre d'affaire total en prestation des entreprises contribuables du pays"

    def formula(pays, period, parameters):
        ca = pays.members('chiffre_affaire_total_prestations', period)
        return pays.sum(ca)


class chiffre_affaire_ventes_contribuables_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Chiffre d'affaire total en ventes des entreprises contribuables du pays"

    def formula(pays, period, parameters):
        ca = pays.members('chiffre_affaire_total_ventes', period)
        return pays.sum(ca)


class base_imposable_it_prestations_contribuables_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Chiffre d'affaire total en prestation des entreprises contribuables du pays"

    def formula(pays, period, parameters):
        ca = pays.members('base_imposable_it_prestations', period)
        return pays.sum(ca)


class base_imposable_it_ventes_contribuables_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Chiffre d'affaire total en ventes des entreprises contribuables du pays"

    def formula(pays, period, parameters):
        ca = pays.members('base_imposable_it_ventes', period)
        return pays.sum(ca)
