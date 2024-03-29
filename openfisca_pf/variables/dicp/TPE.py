# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class redevable_tpe(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = u"Défini si l'entreprise est éligible TPE"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        est_personne_physique = personne('type_personne', period) == TypePersonne.P
        ca_total = personne('chiffre_affaire_total', period)
        ca_inferieur_a_5000000 = ca_total < 5000000
        eligible_tpe = True
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            eligible_tpe = eligible_tpe * ((parameters(period).dicp.abattements_it_cstns.activites_prestations[nom].eligible_tpe == 1) + (personne('chiffre_affaire_' + nom, period) == 0))
        return est_personne_physique * eligible_tpe * ca_inferieur_a_5000000


class montant_tpe_du(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant TPE dû par l'entreprise"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    def formula(personne, period, parameters):
        redevable_tpe = personne('redevable_tpe', period)
        ca_total = personne('chiffre_affaire_total', period)
        ca_inferieur_a_2000000 = ca_total < 2000000
        ca_superieur_a_2000000 = ca_total >= 2000000
        return select(
            [redevable_tpe * ca_inferieur_a_2000000, redevable_tpe * ca_superieur_a_2000000, not_(redevable_tpe)],
            [25000, 45000, 0]
            )


class nombre_entreprises_redevables_TPE_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre d'entreprises du pays redevables de la TPE"

    def formula(pays, period, parameters):
        redevable_tpe = pays.members('redevable_tpe', period)
        return pays.sum(redevable_tpe * 1)
