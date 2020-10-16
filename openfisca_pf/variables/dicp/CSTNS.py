# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefcstns system
from openfisca_pf.entities import *
import numpy

class cstns_calcule(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant CST-NS total calculé"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        cstns_ventes = entreprise('cstns_ventes', period)
        cstns_prestations = entreprise('cstns_prestations', period)
        cstns_total = cstns_ventes + cstns_prestations
        cstns = select(
        [entreprise('eligible_tpe_1', period), entreprise('eligible_tpe_2', period), not_(entreprise('eligible_tpe_1', period)) * not_(entreprise('eligible_tpe_1', period))],
        [0, 0, cstns_total],
        )
        return numpy.floor(cstns)

class cstns_a_payer(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns total à payer"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        cstns_calcule = numpy.floor(entreprise('cstns_calcule', period))
        return where(cstns_calcule < 6000, 0, cstns_calcule)

class cstns_ventes_regularisation_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns pour compenser le montant de l'cstns des prestations"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.cst_ns.taux_prestations
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        return round_(echelle.calc(ca))

class cstns_ventes_avant_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns sur les ventes sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.cst_ns.taux_ventes
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return round_(echelle.calc(ca))

class cstns_ventes_sans_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns sur les ventes ne bénéficiant pas de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.cst_ns.taux_ventes
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette_sans_abattement_droits', period)
        return round_(echelle.calc(ca))

class cstns_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns sur les ventes, suite à application de l'abattement sur les droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.cst_ns.taux_ventes
        cstns_ventes_avant_abattement_droits = entreprise('cstns_ventes_avant_abattement_droits', period)
        cstns_ventes_sans_abattement_droits = entreprise('cstns_ventes_sans_abattement_droits', period)
        cstns = (cstns_ventes_avant_abattement_droits - cstns_ventes_sans_abattement_droits) / 2 + cstns_ventes_sans_abattement_droits
        return cstns

class cstns_prestations_avant_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns sur les prestation sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        chiffre_affaire_total_ventes_apres_abattement_assiette = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        echelle = parameters(period).dicp.cst_ns.taux_prestations
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette', period)
        return round_(echelle.calc(chiffre_affaire_total_ventes_apres_abattement_assiette + ca))

class cstns_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns sur les prestation ne bénéficiant pas de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        chiffre_affaire_total_ventes_apres_abattement_assiette = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        echelle = parameters(period).dicp.cst_ns.taux_prestations
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette_sans_abattement_droits', period)
        return round_(echelle.calc(chiffre_affaire_total_ventes_apres_abattement_assiette + ca))

class cstns_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant cstns sur les prestations, suite à application de l'abattement sur les droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.cst_ns.taux_prestations
        cstns_ventes_regularisation_prestations = entreprise('cstns_ventes_regularisation_prestations', period)
        cstns_prestations_avant_abattement_droits = entreprise('cstns_prestations_avant_abattement_droits', period)
        cstns_prestations_sans_abattement_droits = entreprise('cstns_prestations_sans_abattement_droits', period)
        cstns = (cstns_prestations_avant_abattement_droits - cstns_prestations_sans_abattement_droits) / 2 + cstns_prestations_sans_abattement_droits - cstns_ventes_regularisation_prestations
        return cstns