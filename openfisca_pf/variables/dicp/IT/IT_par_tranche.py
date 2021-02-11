# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class taux_it_ventes_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[0])


class taux_it_ventes_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[1])


class taux_it_ventes_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[2])


class taux_it_ventes_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[3])


class taux_it_ventes_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[4])


class taux_it_ventes_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[5])


class taux_it_ventes_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[6])


class taux_it_ventes_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[7])


class taux_it_ventes_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_ventes.rates[8])


class taux_it_prestations_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_prestations.rates[0])


class taux_it_prestations_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_prestations.rates[1])


class taux_it_prestations_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_prestations.rates[2])


class taux_it_prestations_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_prestations.rates[3])


class taux_it_prestations_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_prestations.rates[4])


class taux_it_prestations_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        return (parameters(period).dicp.it.taux_prestations.rates[5])


class montant_it_ventes_du_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_ventes_tranche_1', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[0])


class montant_it_ventes_du_tranche_2(Variable):
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
        # ca = entreprise('base_imposable_it_ventes', period)
        # return round_(bareme.calc(ca))
        ca = entreprise('base_imposable_it_ventes_tranche_2', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[1])


class montant_it_ventes_du_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 2 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_ventes_tranche_3', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[2])


class montant_it_ventes_du_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 3 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_ventes_tranche_4', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[3])


class montant_it_ventes_du_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 4 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_ventes_tranche_5', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[4])


class montant_it_ventes_du_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 5 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_ventes_tranche_6', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[5])


class montant_it_ventes_du_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 6 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_ventes_tranche_7', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[6])


class montant_it_ventes_du_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 7 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_ventes_tranche_8', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[7])


class montant_it_ventes_du_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 8 sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_ventes_tranche_9', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_ventes.rates[8])


class montant_it_prestations_du_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_prestations_tranche_1', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_prestations.rates[0])


class montant_it_prestations_du_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 1 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_prestations_tranche_2', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_prestations.rates[1])


class montant_it_prestations_du_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 2 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_prestations_tranche_3', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_prestations.rates[2])


class montant_it_prestations_du_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 3 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_prestations_tranche_4', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_prestations.rates[3])


class montant_it_prestations_du_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 4 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_prestations_tranche_5', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_prestations.rates[4])


class montant_it_prestations_du_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 5 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        ca = entreprise('base_imposable_it_prestations_tranche_6', period)
        return arrondiInf(ca * parameters(period).dicp.it.taux_prestations.rates[5])


class montant_du_it_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 0 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('montant_it_prestations_du_tranche_1', period)
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_1', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 1 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('montant_it_prestations_du_tranche_2', period)
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_2', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 2 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('montant_it_prestations_du_tranche_3', period)
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_3', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 3 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('montant_it_prestations_du_tranche_4', period)
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_4', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 4 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('montant_it_prestations_du_tranche_5', period)
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_5', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 5 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_tranche = entreprise('montant_it_prestations_du_tranche_6', period)
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_6', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 6 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_7', period)
        return it_ventes_tranche


class montant_du_it_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 7 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_8', period)
        return it_ventes_tranche


class montant_du_it_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT tranche 8 sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_tranche = entreprise('montant_it_ventes_du_tranche_9', period)
        return it_ventes_tranche
