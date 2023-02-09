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
    entity = Personne
    definition_period = YEAR
    label = u"Montant IT sur les prestations sans tenir compte de l'abattement de droits éventuel :\n\n#it_prestations_avant_abattement_droits = SOMME(#montant_it_prestations_du_tranche_1, #montant_it_prestations_du_tranche_2...)"
    label = u"Montant IT sur les prestation sans tenir compte de l'abattement de droits"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    # Old formula, more sexy, but not consistent with the fact we display the calculation by tranche because of rounding... snirf...
    # def formula(personne, period, parameters):
    #     base_imposable_it_ventes = personne('base_imposable_it_ventes', period) / 4
    #     echelle = parameters(period).dicp.it.taux_prestations
    #     ca = personne('base_imposable_it_prestations', period)
    #     return echelle.calc(base_imposable_it_ventes + ca) - echelle.calc(base_imposable_it_ventes)
    def formula(personne, period, parameters):
        value = 0
        nombre_tranches_it_prestations = personne.pays('nombre_tranches_it_prestations', period)[0]
        for i in range(1, nombre_tranches_it_prestations + 1):
            value += personne(f'montant_it_prestations_du_tranche_{i}', period)
        return value


class it_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant IT sur les prestation ne bénéficiant pas de l'abattement de droits"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(personne, period, parameters):
        base_imposable_it_ventes = personne('base_imposable_it_ventes', period) / 4
        bareme = creerBareme(personne, period, 'it', 'prestations')
        ca = personne('base_imposable_it_prestations_sans_abattement_droits', period)
        return bareme.calc(base_imposable_it_ventes + ca) - bareme.calc(base_imposable_it_ventes)


class it_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant IT sur les prestations, suite à application de l'abattement sur les droits\n\n#it_prestations = #it_prestations_avant_abattement_droits - #it_prestations_abattement_droits"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(personne, period, parameters):
        it_prestations_avant_abattement_droits = personne('it_prestations_avant_abattement_droits', period)
        it_prestations_abattement_droits = personne('it_prestations_abattement_droits', period)
        return it_prestations_avant_abattement_droits - it_prestations_abattement_droits


class it_prestations_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Abattement de droit applique sur l'IT des prestations :\n\n#it_prestations_abattement_droits = ( #it_prestations_avant_abattement_droits - #it_prestations_sans_abattement_droits ) / 2"
    # reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        it_prestations_avant_abattement_droits = personne('it_prestations_avant_abattement_droits', period)
        it_prestations_sans_abattement_droits = personne('it_prestations_sans_abattement_droits', period)
        return (it_prestations_avant_abattement_droits - it_prestations_sans_abattement_droits) / 2
