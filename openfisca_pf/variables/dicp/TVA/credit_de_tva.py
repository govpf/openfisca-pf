# -*- coding: utf-8 -*-

from openfisca_pf.entities import *
from openfisca_pf.base import *


class mois_de_la_declaration_de_tva(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = """
    Mois sur lequel porte la déclaration de TVA
    """
    unit = "Month"


class rib_renseigne(Variable):
    value_type = Enum
    possible_values = OuiNon
    unit = "Oui ou Non"
    default_value = OuiNon.N
    entity = Personne
    definition_period = DAY
    label = u"""
    Boolean indiquant si une personne physique a renseigné son relevé d'identité banquaire
    sur son profil adhérent aux téléservice de la Direction de l'Impot et des Contributions Publiques.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
    ]

class montant_miminum_de_credit_de_tva_au_mois_de_la_declaration_de_tva(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = u"""
    Montant requis au mois de la déclaration nécésaire pour prétendre à un remboursement de crédit de TVA
    """
    unit = 'Currency-XPF/Month'
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
    ]

    def formula(personne, period, parameters):
        mois_de_la_declaration_de_tva = personne(f'mois_de_la_declaration_de_tva', period, parameters)
        montant_miminum_de_credit_de_tva_minimum_par_mois = parameters(period).dicp.tva.seuils.montant_minimum_de_credit_de_tva_par_mois
        return (montant_miminum_de_credit_de_tva_minimum_par_mois[mois_de_la_declaration_de_tva])


class remboursement_de_credit_de_tva_possible_car_rib_rensigne(Variable):
    value_type = Enum
    possible_values = OuiNon
    default_value = OuiNon.N
    unit = "Oui ou Non"
    entity = Personne
    definition_period = DAY
    label = u"""
    Boolean indiquant si une personne physique a renseigné son relevé d'identité banquaire
    sur son profil adhérent aux téléservice de la Direction de l'Impot et des Contributions Publiques
    et peut donc demander un remboursement de crédit de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
    ]

    def formula(personne, period, parameters):
        return personne(f'rib_renseigne', period, parameters)

class remboursement_de_credit_de_tva_possible_au_mois_de_la_declaration_de_tva(Variable):
    value_type = Enum
    possible_values = OuiNon
    default_value = OuiNon.N
    entity = Personne
    definition_period = DAY
    label = u"""
    Boolean indiquant si une personne peut demander un remboursement de crédit de TVA
    pour le mois de la déclaration de TVA.
    """
    unit = "Oui ou Non"
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
    ]

    def formula(personne, period, parameters):
        mois_de_la_declaration_de_tva = personne(f'mois_de_la_declaration_de_tva', period, parameters)
        mois_auquels_un_remboursement_de_credit_de_tva_est_possible = parameters(period).dicp.tva.seuils.mois_auquels_un_remboursement_de_credit_de_tva_est_possible
        print("mois_de_la_declaration_de_tva")
        print(mois_de_la_declaration_de_tva)
        print("mois_auquels_un_remboursement_de_credit_de_tva_est_possible")
        print(mois_auquels_un_remboursement_de_credit_de_tva_est_possible)
        return where(mois_auquels_un_remboursement_de_credit_de_tva_est_possible[mois_de_la_declaration_de_tva], OuiNon.O, OuiNon.N)