# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class it_prestations_avant_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les prestations sans tenir compte de l'abattement de droits éventuel :\n\n#it_prestations_avant_abattement_droits = SOMME(#montant_it_prestations_du_tranche_1, #montant_it_prestations_du_tranche_2...)"
    label = u"Montant IT sur les prestation sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # Old formula, more sexy, but not consistent with the fact we display the calculation by tranche because of rounding... snirf...
    # def formula(entreprise, period, parameters):
    #     base_imposable_it_ventes = entreprise('base_imposable_it_ventes', period) / 4
    #     echelle = parameters(period).dicp.it.taux_prestations
    #     ca = entreprise('base_imposable_it_prestations', period)
    #     return echelle.calc(base_imposable_it_ventes + ca) - echelle.calc(base_imposable_it_ventes)
    def formula(entreprise, period, parameters):
        value = 0
        for i, taux in enumerate(parameters(period).dicp.it.taux_prestations.rates):
            value += entreprise('montant_it_prestations_du_tranche_' + str(i + 1), period)
        return value


class it_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les prestation ne bénéficiant pas de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        base_imposable_it_ventes = entreprise('base_imposable_it_ventes', period) / 4
        echelle = parameters(period).dicp.it.taux_prestations
        ca = entreprise('base_imposable_it_prestations_sans_abattement_droits', period)
        return echelle.calc(base_imposable_it_ventes + ca) - echelle.calc(base_imposable_it_ventes)


class it_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les prestations, suite à application de l'abattement sur les droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_avant_abattement_droits = entreprise('it_prestations_avant_abattement_droits', period)
        it_prestations_sans_abattement_droits = entreprise('it_prestations_sans_abattement_droits', period)
        it = (it_prestations_avant_abattement_droits - it_prestations_sans_abattement_droits) / 2 + it_prestations_sans_abattement_droits
        return it


class abattement_it_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Abattement de droit applique sur l'IT des prestations"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_prestations_avant_abattement_droits = entreprise('it_prestations_avant_abattement_droits', period)
        it_prestations = entreprise('it_prestations', period)
        it = it_prestations_avant_abattement_droits - it_prestations
        return it
