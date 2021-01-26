# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
import numpy


class montant_it_du(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT total calculé"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes = entreprise('it_ventes', period)
        it_prestations = entreprise('it_prestations', period)
        it_total = it_ventes + it_prestations
        it = select(
            [entreprise('eligible_tpe_1', period), entreprise('eligible_tpe_2', period), not_(entreprise('eligible_tpe_1', period)) * not_(entreprise('eligible_tpe_1', period))],
            [25000, 45000, it_total],
            )
        return numpy.floor(it)


class it_a_payer(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT total à payer"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        montant_it_du = numpy.floor(entreprise('montant_it_du', period))
        return where(montant_it_du < 6000, 0, montant_it_du)
