# -*- coding: utf-8 -*-


from numpy import where
from openfisca_pf.base import (
    ArrayLike,
    MONTH,
    ParameterNode,
    Period,
    Population,
    set_input_dispatch_by_period,
    Variable
    )
from openfisca_pf.constants import units
from openfisca_pf.entities import Personne


class rib_renseigne(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    set_input = set_input_dispatch_by_period
    label = """
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
    label = "Montant requis au mois de la déclaration nécésaire pour prétendre à un remboursement de crédit de TVA"
    unit = units.XPF_PER_MONTH
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        minimum_par_mois = parameters(period).dicp.tva.seuils.credit_tva.minimum_par_mois
        return minimum_par_mois["{:02d}".format(period.start.month)]


class remboursement_credit_tva_possible_car_rib_rensigne(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = """
    Boolean indiquant si une personne physique a renseigné son relevé d'identité banquaire
    sur son profil adhérent aux téléservice de la Direction de l'Impot et des Contributions Publiques
    et peut donc demander un remboursement de crédit de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('rib_renseigne', period)


class remboursement_credit_tva_possible_ce_mois(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = """
    Boolean indiquant si une personne peut demander un remboursement de crédit de TVA
    pour le mois de la déclaration de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        remboursement_possible_par_mois = parameters(period).dicp.tva.seuils.credit_tva.remboursement_possible_par_mois
        return remboursement_possible_par_mois["{:02d}".format(period.start.month)]


class remboursement_credit_tva_possible_car_montant_suffisant(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = """
    Boolean indiquant si une personne peut demander un remboursement de crédit de TVA
    en fonction du montant de credit de tva dont elle bénéficie le mois de la déclaration de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        credit_tva = personne('credit_tva', period)
        credit_tva_minimum_ce_mois = personne('credit_tva_minimum_ce_mois', period)
        return credit_tva >= credit_tva_minimum_ce_mois


class remboursement_credit_tva_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = MONTH
    label = """
    Boolean indiquant si une personne peut demander un remboursement de crédit de TVA
    en fonction du mois de la déclaration, du montant de credit de tva dont elle bénéficie, et de si son rib est reseigné.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        remboursement_credit_tva_possible_car_rib_rensigne = personne('remboursement_credit_tva_possible_car_rib_rensigne', period)
        remboursement_credit_tva_possible_ce_mois = personne('remboursement_credit_tva_possible_ce_mois', period)
        remboursement_credit_tva_possible_car_montant_suffisant = personne('remboursement_credit_tva_possible_car_montant_suffisant', period)
        return remboursement_credit_tva_possible_car_rib_rensigne\
            and remboursement_credit_tva_possible_ce_mois\
            and remboursement_credit_tva_possible_car_montant_suffisant


class demande_remboursement_credit_tva(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = """
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
    label = """
    Boolean indiquant si une la demande de remboursement de crédit de TVA est valide.
    La demande est valide lorsqu'elle est possible (celon le mois de la déclaration et celon le montant de montant du crédit de TVA)
    et lorque le montant de remboursement demandé n'exède pas le montant du crédit de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        remboursement_credit_tva_possible = personne('remboursement_credit_tva_possible', period)
        credit_tva = personne('credit_tva', period)
        demande_remboursement_credit_tva = personne('demande_remboursement_credit_tva', period)
        credit_tva_minimum_ce_mois = personne('credit_tva_minimum_ce_mois', period)
        return remboursement_credit_tva_possible\
            and credit_tva_minimum_ce_mois <= demande_remboursement_credit_tva <= credit_tva


class remboursement_credit_tva(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = "Montant du remboursement de credit de TVA."
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = units.XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        demande_remboursement_credit_tva = personne('demande_remboursement_credit_tva', period)
        demande_rembousement_credit_tva_valide = personne('demande_rembousement_credit_tva_valide', period)
        return where(demande_rembousement_credit_tva_valide, demande_remboursement_credit_tva, 0)


class credit_tva_a_reporter(Variable):
    value_type = int
    entity = Personne
    definition_period = MONTH
    label = """
    Montant de credit de TVA retant après remboursement et qui peut être repporter sur la prochaine déclaration de TVA.
    """
    reference = [
        "https://www.impot-polynesie.gov.pf/code/4-section-iv-remboursement-de-credit-de-taxe-deductible"
        ]
    unit = "Currency-XPF"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        credit_tva = personne('credit_tva', period)
        remboursement_credit_tva = personne('remboursement_credit_tva', period)
        return credit_tva - remboursement_credit_tva
