# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefcstns system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class cstns_prestations_avant_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant cstns sur les prestation sans tenir compte de l'abattement de droits\n\n#cstns_prestations_avant_abattement_droits = SOMME(#montant_cstns_prestations_du_tranche_1, #montant_cstns_prestations_du_tranche_2...)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"  # Always use the most official source

    # def formula(personne, period, parameters):
    #     base_imposable_cstns_ventes = personne('base_imposable_cstns_ventes', period) / 4
    #     echelle = parameters(period).dicp.cstns.taux_prestations
    #     ca = personne('base_imposable_cstns_prestations', period)
    #     return round_(echelle.calc(base_imposable_cstns_ventes + ca))
    def formula(personne, period, parameters):
        value = 0
        nombre_tranches_cstns_prestations = personne.pays('nombre_tranches_cstns_prestations', period)[0]
        for i in range(1, nombre_tranches_cstns_prestations + 1):
            value += personne(f'montant_cstns_prestations_du_tranche_{i}', period)
        return value


class cstns_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant cstns sur les prestation ne bénéficiant pas de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-i-bases-et-personnes-imposables"

    def formula(personne, period, parameters):
        base_imposable_cstns_ventes = personne('base_imposable_cstns_ventes', period) / 4
        bareme = creerBareme(personne, period, 'cstns', 'prestations')
        ca = personne('base_imposable_cstns_prestations_sans_abattement_droits', period)
        return bareme.calc(base_imposable_cstns_ventes + ca) - bareme.calc(base_imposable_cstns_ventes)


class cstns_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant cstns sur les prestations, suite à application de l'abattement sur les droits\n\n#cstns_prestations = #cstns_prestations_avant_abattement_droits - #cstns_prestations_abattement_droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"  # Always use the most official source

    def formula(personne, period, parameters):
        cstns_prestations_avant_abattement_droits = personne('cstns_prestations_avant_abattement_droits', period)
        cstns_prestations_abattement_droits = personne('cstns_prestations_abattement_droits', period)
        cstns = cstns_prestations_avant_abattement_droits - cstns_prestations_abattement_droits
        return cstns


class cstns_prestations_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Abattement de droit applique sur la CST-NS des prestations :\n\n#cstns_prestations_abattement_droits = ( #cstns_prestations_avant_abattement_droits - #cstns_prestations_sans_abattement_droits ) / 2"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        cstns_prestations_avant_abattement_droits = personne('cstns_prestations_avant_abattement_droits', period)
        cstns_prestations_sans_abattement_droits = personne('cstns_prestations_sans_abattement_droits', period)
        return (cstns_prestations_avant_abattement_droits - cstns_prestations_sans_abattement_droits) / 2
