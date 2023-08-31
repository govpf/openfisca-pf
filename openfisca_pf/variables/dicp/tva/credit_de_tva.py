# -*- coding: utf-8 -*-

from openfisca_pf.constants import units
from openfisca_pf.base import *
from openfisca_pf.entities import *


class rib_renseigne(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = u"""
    Boolean indiquant si une personne physique a renseigné son relevé d'identité banquaire
    sur son profil adhérent aux téléservice de la Direction de l'Impot et des Contributions Publiques.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN
    default_value = False


class credit_tva_minimum_ce_mois(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"""
    Montant requis au mois de la déclaration nécésaire pour prétendre à un remboursement de crédit de TVA
    """
    unit = units.XPF_PER_MONTH
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]

    def formula(personne, period, parameters):
        minimum_par_mois = parameters(period).dicp.tva.seuils.credit_tva.minimum_par_mois
        return minimum_par_mois["{:02d}".format(period.start.month)]


class remboursement_credit_tva_possible_car_rib_rensigne(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = u"""
    Boolean indiquant si une personne physique a renseigné son relevé d'identité banquaire
    sur son profil adhérent aux téléservice de la Direction de l'Impot et des Contributions Publiques
    et peut donc demander un remboursement de crédit de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne, period, parameters):
        return personne('rib_renseigne', period, parameters)


class remboursement_credit_tva_possible_ce_mois(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = u"""
    Boolean indiquant si une personne peut demander un remboursement de crédit de TVA
    pour le mois de la déclaration de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne, period, parameters):
        remboursement_possible_par_mois = parameters(period).dicp.tva.seuils.credit_tva.remboursement_possible_par_mois
        return remboursement_possible_par_mois["{:02d}".format(period.start.month)]


class remboursement_credit_tva_possible_car_montant_suffisant(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = u"""
    Boolean indiquant si une personne peut demander un remboursement de crédit de TVA
    en fonction du montant de credit de tva dont elle bénéficie le mois de la déclaration de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne, period, parameters):
        credit_tva = personne('credit_tva', period, parameters)
        credit_tva_minimum_ce_mois = personne('credit_tva_minimum_ce_mois', period, parameters)
        return numpy.greater_equal(credit_tva, credit_tva_minimum_ce_mois)


class remboursement_credit_tva_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = u"""
    Boolean indiquant si une personne peut demander un remboursement de crédit de TVA
    en fonction du mois de la déclaration, du montant de credit de tva dont elle bénéficie, et de si son rib est reseigné.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne, period, parameters):
        remboursement_credit_tva_possible_car_rib_rensigne = personne('remboursement_credit_tva_possible_car_rib_rensigne', period, parameters)
        remboursement_credit_tva_possible_ce_mois = personne('remboursement_credit_tva_possible_ce_mois', period, parameters)
        remboursement_credit_tva_possible_car_montant_suffisant = personne('remboursement_credit_tva_possible_car_montant_suffisant', period, parameters)
        return numpy.logical_and.reduce([
            remboursement_credit_tva_possible_car_rib_rensigne,
            remboursement_credit_tva_possible_ce_mois,
            remboursement_credit_tva_possible_car_montant_suffisant
            ])


class demande_remboursement_credit_tva(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"""
    Montant demandé de remboursement de credit de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.XPF
    default_value = 0


class demande_rembousement_credit_tva_valide(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = u"""
    Boolean indiquant si une la demande de remboursement de crédit de TVA est valide.
    La demande est valide lorsqu'elle est possible (celon le mois de la déclaration et celon le montant de montant du crédit de TVA)
    et lorque le montant de remboursement demandé n'exède pas le montant du crédit de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne, period, parameters):
        remboursement_credit_tva_possible = personne('remboursement_credit_tva_possible', period, parameters)
        credit_tva = personne('credit_tva', period, parameters)
        demande_remboursement_credit_tva = personne('demande_remboursement_credit_tva', period, parameters)
        return numpy.logical_and(
            remboursement_credit_tva_possible,
            numpy.less_equal(demande_remboursement_credit_tva, credit_tva)
            )


class remboursement_credit_tva(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant du remboursement de credit de TVA."
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.XPF

    def formula(personne, period, parameters):
        demande_remboursement_credit_tva = personne('demande_remboursement_credit_tva', period, parameters)
        demande_rembousement_credit_tva_valide = personne('demande_rembousement_credit_tva_valide', period, parameters)
        return numpy.where(demande_rembousement_credit_tva_valide, demande_remboursement_credit_tva, 0)


class credit_tva_a_reporter(Variable):
    value_type = int
    entity = Personne
    definition_period = MONTH
    label = u"""
    Montant de credit de TVA retant après remboursement et qui peut être repporter sur la prochaine déclaration de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = "Currency-XPF"

    def formula(personne, period, parameters):
        credit_tva = personne('credit_tva', period, parameters)
        remboursement_credit_tva = personne('remboursement_credit_tva', period, parameters)
        return numpy.subtract(credit_tva, remboursement_credit_tva)
