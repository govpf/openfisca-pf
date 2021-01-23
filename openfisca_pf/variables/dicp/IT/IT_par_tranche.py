# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
from openfisca_core.taxscales import MarginalRateTaxScale
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
import numpy


class it_ventes_avant_abattement_droits_tranche_0(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_ventes_tranche_0_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[0])


class it_ventes_avant_abattement_droits_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 1 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        # bareme = MarginalRateTaxScale(name = 'IT tranche 1')
        # tranche = 1
        # bareme.add_bracket(parameters(period).dicp.it.taux_ventes.thresholds[tranche - 1], 0)
        # bareme.add_bracket(parameters(period).dicp.it.taux_ventes.thresholds[tranche], parameters(period).dicp.it.taux_ventes.rates[tranche])
        # bareme.add_bracket(parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1], 0)
        # ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        # return round_(bareme.calc(ca))
        ca = entreprise('chiffre_affaire_ventes_tranche_1_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[1])

class it_ventes_avant_abattement_droits_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 2 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_ventes_tranche_2_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[2])


class it_ventes_avant_abattement_droits_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 3 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_ventes_tranche_3_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[3])


class it_ventes_avant_abattement_droits_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 4 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_ventes_tranche_4_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[4])


class it_ventes_avant_abattement_droits_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 5 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_ventes_tranche_5_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[5])


class it_ventes_avant_abattement_droits_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 6 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_ventes_tranche_6_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[6])


class it_ventes_avant_abattement_droits_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 7 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_ventes_tranche_7_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[7])


class it_ventes_avant_abattement_droits_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 8 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_ventes_tranche_8_it', period)
        return round_(ca * parameters(period).dicp.it.taux_ventes.rates[8])


class it_prestations_avant_abattement_droits_tranche_0(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_prestations_tranche_0_it', period)
        return round_(ca * parameters(period).dicp.it.taux_prestations.rates[0])


class it_prestations_avant_abattement_droits_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 1 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_prestations_tranche_1_it', period)
        return round_(ca * parameters(period).dicp.it.taux_prestations.rates[1])


class it_prestations_avant_abattement_droits_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 2 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_prestations_tranche_2_it', period)
        return round_(ca * parameters(period).dicp.it.taux_prestations.rates[2])


class it_prestations_avant_abattement_droits_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 3 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_prestations_tranche_3_it', period)
        return round_(ca * parameters(period).dicp.it.taux_prestations.rates[3])


class it_prestations_avant_abattement_droits_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 4 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_prestations_tranche_4_it', period)
        return round_(ca * parameters(period).dicp.it.taux_prestations.rates[4])


class it_prestations_avant_abattement_droits_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 5 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('chiffre_affaire_prestations_tranche_5_it', period)
        return round_(ca * parameters(period).dicp.it.taux_prestations.rates[5])


class it_avant_abattement_droits_tranche_0(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('it_prestations_avant_abattement_droits_tranche_0', period)
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_0', period)
        return round_(it_prestations_tranche + it_ventes_tranche)


class it_avant_abattement_droits_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 1 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('it_prestations_avant_abattement_droits_tranche_1', period)
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_1', period)
        return round_(it_prestations_tranche + it_ventes_tranche)


class it_avant_abattement_droits_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 2 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('it_prestations_avant_abattement_droits_tranche_2', period)
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_2', period)
        return round_(it_prestations_tranche + it_ventes_tranche)


class it_avant_abattement_droits_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 3 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('it_prestations_avant_abattement_droits_tranche_3', period)
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_3', period)
        return round_(it_prestations_tranche + it_ventes_tranche)


class it_avant_abattement_droits_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 4 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('it_prestations_avant_abattement_droits_tranche_4', period)
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_4', period)
        return round_(it_prestations_tranche + it_ventes_tranche)


class it_avant_abattement_droits_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 5 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('it_prestations_avant_abattement_droits_tranche_5', period)
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_5', period)
        return round_(it_prestations_tranche + it_ventes_tranche)


class it_avant_abattement_droits_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 6 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_6', period)
        return round_(it_ventes_tranche)


class it_avant_abattement_droits_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 7 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_7', period)
        return round_(it_ventes_tranche)


class it_avant_abattement_droits_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 8 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_tranche = entreprise('it_ventes_avant_abattement_droits_tranche_8', period)
        return round_(it_ventes_tranche)
