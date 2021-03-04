# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *
import numpy


class base_imposable_cstns_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des prestations après abattement d'assiette mais sans abattement de droit"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            cca = str(parameters(period).dicp.abattements_it_cstns.activites_prestations[nom].cca)
            coeff_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].coeff_assiette
            seuil_abattement_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_d_assiette
            ca = numpy.floor(entreprise('chiffre_affaire_' + nom, period) / 1000) * 1000
            # If ca is below seuil_abattement_assiette there is no reduction, otherwise the reduction is on the part above seuil_abattement_assiette
            value += where(ca <= seuil_abattement_assiette, ca, seuil_abattement_assiette + (ca - seuil_abattement_assiette) * (1 - coeff_assiette))
        return round_(value)


class base_imposable_cstns_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant total du chiffre d'affaire concernant des prestations après abattement de l'assiette, mais qui ne beneficiement pas d'un abattement de droit"
    reference = "https://law.gov.example/income_tax"  # Always use the most official source

    # The formula to compute the income tax for a given person at a given period
    def formula(entreprise, period, parameters):
        value = 0
        charges_superieures_50_pourcents = entreprise('total_charges_releve_detaille', period) >= (entreprise('chiffre_affaire_total_prestations', period) / 2)
        releve_de_charges_fourni = entreprise('releve_de_charges_fourni', period) == OuiNon.O
        est_personne_physique = entreprise('type_personne', period) == TypePersonne.P
        annexes_IT_fournies = entreprise('annexes_IT_fournies', period) == OuiNon.O
        for nom in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            cca = str(parameters(period).dicp.abattements_it_cstns.activites_prestations[nom].cca)
            ca = numpy.floor(entreprise('chiffre_affaire_' + nom, period) / 1000) * 1000
            coeff_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].coeff_assiette
            seuil_abattement_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_d_assiette
            ca_apres_abattement_assiette = where(ca <= seuil_abattement_assiette, ca, seuil_abattement_assiette + (ca - seuil_abattement_assiette) * (1 - coeff_assiette))
            abattement_droits = parameters(period).dicp.abattements_it_cstns.cca[cca].abattement_de_droit
            seuil_bascule_abattement_de_droit = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_de_droit
            seuils_abattement_de_droit_applicable_aux_personnes_physiques = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_de_droit_applicable_aux_personnes_physiques
            abattement_droits_charges = parameters(period).dicp.abattements_it_cstns.cca[cca].abattement_de_droit_avec_condition_de_charges
            seuil_annexe = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_justificatifs_a_fournir_abattement_de_droit_avec_condition_de_charges
            # Here we only take into account CA with no 'abattement de droit'
            abattement_de_droit_applicable = abattement_droits & (not_(abattement_droits_charges) + (est_personne_physique & not_(seuils_abattement_de_droit_applicable_aux_personnes_physiques)) + (ca <= seuil_bascule_abattement_de_droit))
            abattement_de_droit_de_charge_applicable = abattement_droits_charges & (ca > seuil_bascule_abattement_de_droit) & charges_superieures_50_pourcents & releve_de_charges_fourni & (annexes_IT_fournies + (ca <= seuil_annexe) + (est_personne_physique & not_(seuils_abattement_de_droit_applicable_aux_personnes_physiques)))
            value += where(abattement_de_droit_applicable + abattement_de_droit_de_charge_applicable, 0, ca_apres_abattement_assiette)
        return round_(value)
