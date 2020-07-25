# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

class chiffre_affaire_total_prestations_apres_abattement_assiette(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des prestations après abattement"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.prestations]:
            value += entreprise('chiffre_affaire_' + nom, period) * (1 - parameters(period).dicp.it.abattements_it.prestations[nom].coeff_assiette) 
        return value

class chiffre_affaire_total_prestations_apres_abattement_assiette_sans_abattement_droits(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des prestations après abattement de l'assiette, mais qui ne beneficiement pas d'un abattement de droit"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.prestations]:
            pas_abattement_droits = parameters(period).dicp.it.abattements_it.prestations[nom].coeff_droits == 0
            pas_abattement_droits_charges = parameters(period).dicp.it.abattements_it.prestations[nom].coeff_droits_si_charge_sup_50_pourcents == 0
            charges_inferieures_50_pourcents = entreprise('charges_' + nom, period) < (entreprise('chiffre_affaire_' + nom, period) / 2)
            justificatif_depose = entreprise('justificatif_charges_depose', period)
            # Here we only take into account CA with no 'abattement'
            value += where(pas_abattement_droits & (not_(justificatif_depose) + pas_abattement_droits_charges + charges_inferieures_50_pourcents + entreprise('abattement_droits_applique', period)), 
                entreprise('chiffre_affaire_' + nom, period) * (1 - parameters(period).dicp.it.abattements_it.prestations[nom].coeff_assiette), 0)
        return value

class abattement_droits_applique(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des prestations après abattement de l'assiette, mais qui ne beneficiement pas d'un abattement de droit"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.it.abattements_it.prestations]:
            abattement_droits = parameters(period).dicp.it.abattements_it.prestations[nom].coeff_droits != 0
            # Here we only take into account CA with abattement 'abattement'
            value += where(abattement_droits, entreprise('chiffre_affaire_' + nom, period), 0)
        return value > 0

class justificatif_charges_depose(Variable):
    value_type = bool
    entity = Entreprise
    definition_period = YEAR
    label = u"Mettre a true si l'entreprise a deposé un justificatif de charges, afin de bénéficier de l'abattement correspondant"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source
