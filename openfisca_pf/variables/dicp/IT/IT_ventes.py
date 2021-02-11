# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class it_ventes_avant_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les ventes sans tenir compte de l'abattement de droits éventuel :\n\n#it_ventes_avant_abattement_droits = SOMME(#montant_it_ventes_du_tranche_1, #montant_it_ventes_du_tranche_2...)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    # Old formula, more sexy, but not consistent with the fact we display the calculation by tranche because of rounding... snirf...
    # def formula(entreprise, period, parameters):
    #     echelle = parameters(period).dicp.it.taux_ventes
    #     ca = entreprise('base_imposable_it_ventes', period)
    #     return echelle.calc(ca)
    def formula(entreprise, period, parameters):
        value = 0
        for i, taux in enumerate(parameters(period).dicp.it.taux_ventes.rates):
            value += entreprise('montant_it_ventes_du_tranche_' + str(i + 1), period)
        return value


class it_ventes_sans_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les ventes ne bénéficiant pas de l'abattement de droits :\n\n#it_ventes_sans_abattement_droits = IT(#base_imposable_it_ventes_sans_abattement_droits)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.it.taux_ventes
        ca = entreprise('base_imposable_it_ventes_sans_abattement_droits', period)
        return echelle.calc(ca)


class it_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les ventes, suite à application de l'abattement sur les droits :\n\n#it_ventes = (#it_ventes_avant_abattement_droits - #it_ventes_sans_abattement_droits) / 2 + #it_ventes_sans_abattement_droits"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_avant_abattement_droits = entreprise('it_ventes_avant_abattement_droits', period)
        it_ventes_sans_abattement_droits = entreprise('it_ventes_sans_abattement_droits', period)
        it = (it_ventes_avant_abattement_droits - it_ventes_sans_abattement_droits) / 2 + it_ventes_sans_abattement_droits
        return it


class abattement_it_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Abattement de droit applique sur l'IT des ventes :\n\n#abattement_it_ventes = #it_ventes_avant_abattement_droits - #it_ventes"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes_avant_abattement_droits = entreprise('it_ventes_avant_abattement_droits', period)
        it_ventes = entreprise('it_ventes', period)
        it = (it_ventes_avant_abattement_droits - it_ventes)
        return it
