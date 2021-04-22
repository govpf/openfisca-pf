# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *

# class salaire(Variable):
#     value_type = float
#     entity = Personne
#     default_value = 0
#     definition_period = MONTH
#     set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
#     label = "Salaire"
#     reference = "https://law.gov.example/salary"  # Always use the most official source


class eligible_icra(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = MONTH
    # set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Eligible à demander l'ICRA"
    reference = ["https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument"]

    def formula(personne, period, parameters):
        nombre_annee_sans_icra = parameters(period).sefi.ICRA.nombre_annee_sans_icra
        nombre_mois_perte_emploi = parameters(period).sefi.ICRA.nombre_mois_perte_emploi
        age_minimum = parameters(period).sefi.ICRA.age_minimum
        est_demandeur_emploi = personne('est_demandeur_emploi', period)
        patente = personne('patente', period)
        perte_emploi = personne('perte_emploi', period.offset(-nombre_mois_perte_emploi, 'month').start.period('month', nombre_mois_perte_emploi), options = [ADD])
        age = personne('age', period)
        beneficiaire_icra = personne('beneficiaire_icra', period.offset(-nombre_annee_sans_icra, 'year').start.period('year', nombre_annee_sans_icra), options = [ADD])
        return (est_demandeur_emploi + perte_emploi) * (age >= age_minimum) * not_(beneficiaire_icra) * not_(patente)


class beneficiaire_icra(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "Bénéficiaire ICRA"
    reference = ["https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument"]


class montant_indemnite_icra(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "Bénéficiaire ICRA"
    reference = ["https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument"]

    def formula(personne, period, parameters):
        return parameters(period).sefi.ICRA.montant_indemnite * personne('eligible_icra', period)


class nombre_mois_indemnite_icra(Variable):
    value_type = int
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "Bénéficiaire ICRA"
    reference = ["https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument"]

    def formula(personne, period, parameters):
        return parameters(period).sefi.ICRA.nombre_mois_indemnite * personne('eligible_icra', period)


class montant_prime_demarrage_icra(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = "Bénéficiaire ICRA"
    reference = ["https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument"]

    def formula(personne, period, parameters):
        return parameters(period).sefi.ICRA.montant_prime_demarrage * personne('eligible_icra', period)
