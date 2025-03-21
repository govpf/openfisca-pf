# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Enum,
    GroupPopulation,
    not_,
    ParameterNode,
    Period,
    Population,
    Variable,
    where,
    YEAR
    )
from openfisca_pf.constants.units import XPF, BOOLEAN
from openfisca_pf.entities import Pays, Personne
from openfisca_pf.enums.common import OuiNon
from openfisca_pf.enums.impots import TypeSociete
from openfisca_pf.functions.currency import arrondi_inferieur


class montant_it_du(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Impôt sur les transactions dû'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        it_ventes = personne('it_ventes', period)
        it_prestations = personne('it_prestations', period)
        return arrondi_inferieur(it_ventes + it_prestations)


class it_a_payer(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Impôt sur les transactions à payer'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_it_du = personne('montant_it_du', period)
        return where(montant_it_du < 6000, 0, montant_it_du)


class montant_it_total_a_payer(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Impôt sur les transactions à payer, en prenant compte des déductions et des pénalités'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_it_du = personne('montant_it_du', period)
        montant_total_deductions_it = personne('montant_total_deductions_it', period)
        montant_total_penalites_it = personne('montant_total_penalites_it', period)
        return montant_it_du - montant_total_deductions_it + montant_total_penalites_it


class montant_it_total_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = 'Impôt sur les transactions du par les entreprises du pays'
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(pays: GroupPopulation, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_it_du = pays.members('montant_it_du', period)
        return pays.sum(montant_it_du)


class redevable_it(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à l'impôt sur les transactions"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = BOOLEAN

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        redevable_tpe = personne('redevable_tpe', period)
        type_societe = personne('type_societe', period)
        option_is = personne('option_is', period) == OuiNon.O
        option_it = personne('option_it', period) == OuiNon.O
        snc_sans_option_is = (type_societe == TypeSociete.SNC) * not_(option_is)
        ei_non_redevable_tpe = not_(redevable_tpe) * (type_societe == TypeSociete.EI)
        eurl_avec_option_it = (type_societe == TypeSociete.EURL) * option_it
        return snc_sans_option_is + ei_non_redevable_tpe + eurl_avec_option_it


class option_it(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = """
    Défini si l'entreprise à opté pour l'impôt sur les transactions plutot que l'impôt sur les sociétés
    (applicable aux Entreprise Unipersonnelle à Responsabilité Limitée)
    """
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = BOOLEAN


class option_it_possible(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Indique que l'entreprise peut opter pour l'impôt sur les transactions plutot que l'impôt sur les sociétés"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        type_societe = personne('type_societe', period)
        return type_societe == TypeSociete.EURL
