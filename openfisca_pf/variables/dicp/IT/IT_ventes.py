# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class it_ventes_regularisation_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT pour compenser le montant de l'IT des prestations"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.it.taux_prestations
        ca = entreprise('base_imposable_it_ventes', period) / 4
        return round_(echelle.calc(ca))


class it_ventes_avant_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.it.taux_ventes
        ca = entreprise('base_imposable_it_ventes', period)
        return round_(echelle.calc(ca))


class it_ventes_sans_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les ventes ne bénéficiant pas de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.it.taux_ventes
        ca = entreprise('base_imposable_it_ventes_sans_abattement_droits', period)
        return round_(echelle.calc(ca))


class it_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les ventes, suite à application de l'abattement sur les droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_avant_abattement_droits = entreprise('it_ventes_avant_abattement_droits', period)
        it_ventes_sans_abattement_droits = entreprise('it_ventes_sans_abattement_droits', period)
        it = (it_ventes_avant_abattement_droits - it_ventes_sans_abattement_droits) / 2 + it_ventes_sans_abattement_droits
        return round_(it)


class abattement_it_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Abattement de droit applique sur l'IT des ventes"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_avant_abattement_droits = entreprise('it_ventes_avant_abattement_droits', period)
        it_ventes = entreprise('it_ventes', period)
        it = (it_ventes_avant_abattement_droits - it_ventes)
        return round_(it)
