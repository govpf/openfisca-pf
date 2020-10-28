# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
import numpy


class eligible_tpe_1(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible TPE"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        est_personne_pysique = entreprise('entreprise_est_personne_physique', period)
        ca_total = entreprise('chiffre_affaire_total_prestations', period) + entreprise('chiffre_affaire_total_ventes', period)
        ca_inferieur_a_2000000 = ca_total < 2000000
        eligible_tpe = True
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            ca = numpy.floor(entreprise('chiffre_affaire_' + nom, period) / 1000) * 1000
            eligible_tpe = eligible_tpe * ((parameters(period).dicp.abattements_it_cstns.activites_prestations[nom].eligible_tpe == 1) + (ca == 0))
        return est_personne_pysique * eligible_tpe * ca_inferieur_a_2000000


class eligible_tpe_2(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible TPE"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(entreprise, period, parameters):
        est_personne_pysique = entreprise('entreprise_est_personne_physique', period)
        ca_total = entreprise('chiffre_affaire_total', period)
        ca_inferieur_a_5000000 = ca_total < 5000000
        ca_superieur_a_2000000 = ca_total >= 2000000
        eligible_tpe = True
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            eligible_tpe = eligible_tpe * ((parameters(period).dicp.abattements_it_cstns.activites_prestations[nom].eligible_tpe == 1) + (entreprise('chiffre_affaire_' + nom, period) == 0))
        return est_personne_pysique * eligible_tpe * ca_superieur_a_2000000 * ca_inferieur_a_5000000
