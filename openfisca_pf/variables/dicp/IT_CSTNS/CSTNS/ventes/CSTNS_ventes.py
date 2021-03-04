# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefcstns system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class cstns_ventes_avant_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant cstns sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # def formula(entreprise, period, parameters):
    #     echelle = parameters(period).dicp.cst_ns.taux_ventes
    #     ca = entreprise('base_imposable_cstns_ventes', period)
    #     return round_(echelle.calc(ca))
    def formula(entreprise, period, parameters):
        value = 0
        nombre_tranches = entreprise.pays('nombre_tranches_cstns_ventes', period)[0]
        for i in range(1, nombre_tranches + 1):
            value += entreprise(f'montant_cstns_ventes_du_tranche_{i}', period)
        return value


class cstns_ventes_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant cstns sur les ventes ne bénéficiant pas de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        # echelle = parameters(period).dicp.cst_ns.taux_ventes
        ca = entreprise('base_imposable_cstns_ventes_sans_abattement_droits', period)
        bareme = creerBareme(entreprise, period, 'cstns', 'ventes')
        return bareme.calc(ca)


class cstns_ventes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant cstns sur les ventes, suite à application de l'abattement sur les droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        cstns_ventes_abattement_droits = entreprise('cstns_ventes_abattement_droits', period)
        cstns_ventes_avant_abattement_droits = entreprise('cstns_ventes_avant_abattement_droits', period)
        return cstns_ventes_avant_abattement_droits - cstns_ventes_abattement_droits


class cstns_ventes_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Abattement de droit applique sur la CST NS des ventes :\n\n#cstns_ventes_abattement_droits = ( #cstns_ventes_avant_abattement_droits - #cstns_ventes_sans_abattement_droits ) / 2"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        cstns_ventes_avant_abattement_droits = entreprise('cstns_ventes_avant_abattement_droits', period)
        cstns_ventes_sans_abattement_droits = entreprise('cstns_ventes_sans_abattement_droits', period)
        return (cstns_ventes_avant_abattement_droits - cstns_ventes_sans_abattement_droits) / 2
