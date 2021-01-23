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


class chiffre_affaire_ventes_tranche_0_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 0 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 0
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class chiffre_affaire_ventes_tranche_1_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 1 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class chiffre_affaire_ventes_tranche_2_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 2 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class chiffre_affaire_ventes_tranche_3_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 3 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class chiffre_affaire_ventes_tranche_4_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 4 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class chiffre_affaire_ventes_tranche_5_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 5 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class chiffre_affaire_ventes_tranche_6_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 6 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 6
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class chiffre_affaire_ventes_tranche_7_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 7 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 7
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            ))


class chiffre_affaire_ventes_tranche_8_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de ventes sur la tranche 8 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 8
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_ventes.thresholds[tranche]
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca > seuil_tranche_inferieure],
            [0, ca - seuil_tranche_inferieure],
            ))


class chiffre_affaire_prestations_tranche_0_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de prestations sur la tranche 0 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 0
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette', period) + entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        caVenteTranche = entreprise('chiffre_affaire_ventes_tranche_0_it', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class chiffre_affaire_prestations_tranche_1_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de prestations sur la tranche 1 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette', period) + entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        caVenteTranche = entreprise('chiffre_affaire_ventes_tranche_1_it', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class chiffre_affaire_prestations_tranche_2_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de prestations sur la tranche 2 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette', period) + entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        caVenteTranche = entreprise('chiffre_affaire_ventes_tranche_2_it', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class chiffre_affaire_prestations_tranche_3_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de prestations sur la tranche 3 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette', period) + entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        caVenteTranche = entreprise('chiffre_affaire_ventes_tranche_3_it', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class chiffre_affaire_prestations_tranche_4_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de prestations sur la tranche 4 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche]
        seuil_tranche_superieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche + 1]
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette', period) + entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        caVenteTranche = entreprise('chiffre_affaire_ventes_tranche_4_it', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca < seuil_tranche_superieure, ca >= seuil_tranche_superieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche, seuil_tranche_superieure - seuil_tranche_inferieure - caVenteTranche],
            ))


class chiffre_affaire_prestations_tranche_5_it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Chiffre d'affaire de prestations sur la tranche 5 de l'IT"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        seuil_tranche_inferieure = parameters(period).dicp.it.taux_prestations.thresholds[tranche]
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette', period) + entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        caVenteTranche = entreprise('chiffre_affaire_ventes_tranche_5_it', period) / 4
        return round_(select(
            [ca <= seuil_tranche_inferieure, ca > seuil_tranche_inferieure],
            [0, ca - seuil_tranche_inferieure - caVenteTranche],
            ))
