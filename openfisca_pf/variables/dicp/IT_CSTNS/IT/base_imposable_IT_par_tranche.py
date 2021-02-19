# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class base_imposable_it_ventes_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 1 de l'IT : \n\n"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_ventes_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 2 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_ventes_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 3 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_ventes_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 4 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_ventes_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 5 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_ventes_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 6 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 6
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_ventes_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 7 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 7
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_ventes_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 8 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 8
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_ventes_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 9 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 9
        return calculerBaseImposableVentesTranche(entreprise, period, tranche, 'it')


class base_imposable_it_prestations_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 1 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        return calculerBaseImposablePrestationsTranche(entreprise, period, tranche, 'it')


class base_imposable_it_prestations_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 2 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        return calculerBaseImposablePrestationsTranche(entreprise, period, tranche, 'it')


class base_imposable_it_prestations_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 3 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        return calculerBaseImposablePrestationsTranche(entreprise, period, tranche, 'it')


class base_imposable_it_prestations_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 4 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        return calculerBaseImposablePrestationsTranche(entreprise, period, tranche, 'it')


class base_imposable_it_prestations_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 5 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        return calculerBaseImposablePrestationsTranche(entreprise, period, tranche, 'it')


class base_imposable_it_prestations_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 6 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 6
        return calculerBaseImposablePrestationsTranche(entreprise, period, tranche, 'it')
