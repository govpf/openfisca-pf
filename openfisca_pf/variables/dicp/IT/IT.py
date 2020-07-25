# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

class it_ventes(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les ventes"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.it.taux_ventes
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period)
        return echelle.calc(ca)

class it(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT total"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        it_ventes = entreprise('it_ventes', period)
        it_prestations = entreprise('it_prestations', period)
        it_total = it_ventes + it_prestations
        return where(it_total < 6000, 0, it_total)

class it_ventes_regularisation_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT pour compenser le montant de l'IT des prestations"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.it.taux_prestations
        ca = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        return echelle.calc(ca)

class it_prestations_avant_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les prestation sans tenir compte de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        chiffre_affaire_total_ventes_apres_abattement_assiette = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        echelle = parameters(period).dicp.it.taux_prestations
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette', period)
        return echelle.calc(chiffre_affaire_total_ventes_apres_abattement_assiette + ca)

class it_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les prestation ne bénéficiant pas de l'abattement de droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        chiffre_affaire_total_ventes_apres_abattement_assiette = entreprise('chiffre_affaire_total_ventes_apres_abattement_assiette', period) / 4
        echelle = parameters(period).dicp.it.taux_prestations
        ca = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette_sans_abattement_droits', period)
        return echelle.calc(chiffre_affaire_total_ventes_apres_abattement_assiette + ca)

class it_prestations(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant IT sur les prestations, suite à application de l'abattement sur les droits"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        echelle = parameters(period).dicp.it.taux_prestations
        it_ventes_regularisation_prestations = entreprise('it_ventes_regularisation_prestations', period)
        it_prestations_avant_abattement_droits = entreprise('it_prestations_avant_abattement_droits', period)
        it_prestations_sans_abattement_droits = entreprise('it_prestations_sans_abattement_droits', period)
        ca_abattements = entreprise('chiffre_affaire_total_prestations_apres_abattement_assiette_sans_abattement_droits', period)
        it = (it_prestations_avant_abattement_droits - it_prestations_sans_abattement_droits) / 2 + it_prestations_sans_abattement_droits - it_ventes_regularisation_prestations
        return select(
        [entreprise('eligible_tpe_1', period), entreprise('eligible_tpe_2', period), not_(entreprise('eligible_tpe_1', period)) * not_(entreprise('eligible_tpe_1', period))],
        [25000, 45000, it],
        )

class eligible_tpe_1(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible TPE"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        est_personne_pysique = entreprise('personne_physique', period)
        ca_total = entreprise('chiffre_affaire_total_prestations', period) + entreprise('chiffre_affaire_total_ventes', period)
        ca_inferieur_a_2000000 = ca_total < 2000000
        eligible_tpe = True
        for nom in [*parameters(period).dicp.it.abattements_it.prestations]:
            eligible_tpe = eligible_tpe * ((parameters(period).dicp.it.abattements_it.prestations[nom].eligible_tpe == 1) + (entreprise('chiffre_affaire_' + nom, period) == 0))
        return est_personne_pysique * eligible_tpe * ca_inferieur_a_2000000

class eligible_tpe_2(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible TPE"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        est_personne_pysique = entreprise('personne_physique', period)
        ca_total = entreprise('chiffre_affaire_total', period)
        ca_inferieur_a_5000000 = ca_total < 5000000
        ca_superieur_a_2000000 = ca_total >= 2000000
        eligible_tpe = True
        for nom in [*parameters(period).dicp.it.abattements_it.prestations]:
            eligible_tpe = eligible_tpe * ((parameters(period).dicp.it.abattements_it.prestations[nom].eligible_tpe == 1) + (entreprise('chiffre_affaire_' + nom, period) == 0))
        return est_personne_pysique * eligible_tpe * ca_superieur_a_2000000 * ca_inferieur_a_5000000
