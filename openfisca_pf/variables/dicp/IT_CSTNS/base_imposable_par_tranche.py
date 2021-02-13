# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class base_imposable_it_ventes_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 1 de l'IT : \n\n"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_ventes_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class base_imposable_it_ventes_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 2 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_ventes_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class base_imposable_it_ventes_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 3 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_ventes_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class base_imposable_it_ventes_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 4 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_ventes_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class base_imposable_it_ventes_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 5 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_ventes_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class base_imposable_it_ventes_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 6 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 6
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_ventes_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class base_imposable_it_ventes_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 7 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 7
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_ventes_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class base_imposable_it_ventes_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 8 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 8
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_ventes_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class base_imposable_it_ventes_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de ventes sur la tranche 9 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 9
        seuil_tranche_inferieure = entreprise(f'seuil_it_ventes_tranche_{tranche}', period)
        ca = entreprise('base_imposable_it_ventes', period)
        return (select(
            [ca <= seuil_tranche_inferieure, ca > seuil_tranche_inferieure],
            [0, ca - seuil_tranche_inferieure],
            ))


class base_imposable_it_prestations_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 1 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        seuil_tranche_inferieure = entreprise(f'seuil_it_prestations_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_prestations_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_prestations', period) + entreprise('base_imposable_it_ventes', period) / 4
        caVenteTranche = entreprise('base_imposable_it_ventes_tranche_1', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class base_imposable_it_prestations_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 2 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        seuil_tranche_inferieure = entreprise(f'seuil_it_prestations_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_prestations_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_prestations', period) + entreprise('base_imposable_it_ventes', period) / 4
        caVenteTranche = entreprise('base_imposable_it_ventes_tranche_2', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class base_imposable_it_prestations_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 3 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        seuil_tranche_inferieure = entreprise(f'seuil_it_prestations_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_prestations_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_prestations', period) + entreprise('base_imposable_it_ventes', period) / 4
        caVenteTranche = entreprise('base_imposable_it_ventes_tranche_3', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class base_imposable_it_prestations_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 4 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        seuil_tranche_inferieure = entreprise(f'seuil_it_prestations_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_prestations_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_prestations', period) + entreprise('base_imposable_it_ventes', period) / 4
        caVenteTranche = entreprise('base_imposable_it_ventes_tranche_4', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class base_imposable_it_prestations_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 5 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        seuil_tranche_inferieure = entreprise(f'seuil_it_prestations_tranche_{tranche}', period)
        seuil_tranche_superieure = entreprise(f'seuil_it_prestations_tranche_{tranche + 1}', period)
        ca = entreprise('base_imposable_it_prestations', period) + entreprise('base_imposable_it_ventes', period) / 4
        caVenteTranche = entreprise('base_imposable_it_ventes_tranche_5', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class base_imposable_it_prestations_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Base imposable de prestations sur la tranche 6 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 6
        seuil_tranche_inferieure = entreprise(f'seuil_it_prestations_tranche_{tranche}', period)
        ca = entreprise('base_imposable_it_prestations', period) + entreprise('base_imposable_it_ventes', period) / 4
        caVenteTranche = (entreprise('base_imposable_it_ventes_tranche_6', period) + entreprise('base_imposable_it_ventes_tranche_7', period) + entreprise('base_imposable_it_ventes_tranche_8', period) + entreprise('base_imposable_it_ventes_tranche_9', period)) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca > seuil_tranche_inferieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche],
            ))
