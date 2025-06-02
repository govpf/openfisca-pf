# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class montant_du_it_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 1 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_1 = personne('montant_it_prestations_du_tranche_1', period, parameters)
        montant_it_ventes_du_tranche_1 = personne('montant_it_ventes_du_tranche_1', period, parameters)
        return montant_it_prestations_du_tranche_1 + montant_it_ventes_du_tranche_1


class montant_du_it_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 2 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_2 = personne('montant_it_prestations_du_tranche_2', period, parameters)
        montant_it_ventes_du_tranche_2 = personne('montant_it_ventes_du_tranche_2', period, parameters)
        return montant_it_prestations_du_tranche_2 + montant_it_ventes_du_tranche_2


class montant_du_it_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 3 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_3 = personne('montant_it_prestations_du_tranche_3', period, parameters)
        montant_it_ventes_du_tranche_3 = personne('montant_it_ventes_du_tranche_3', period, parameters)
        return montant_it_prestations_du_tranche_3 + montant_it_ventes_du_tranche_3


class montant_du_it_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 4 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_4 = personne('montant_it_prestations_du_tranche_4', period, parameters)
        montant_it_ventes_du_tranche_4 = personne('montant_it_ventes_du_tranche_4', period, parameters)
        return montant_it_prestations_du_tranche_4 + montant_it_ventes_du_tranche_4


class montant_du_it_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 5 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_5 = personne('montant_it_prestations_du_tranche_5', period, parameters)
        montant_it_ventes_du_tranche_5 = personne('montant_it_ventes_du_tranche_5', period, parameters)
        return montant_it_prestations_du_tranche_5 + montant_it_ventes_du_tranche_5


class montant_du_it_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 6 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_6 = personne('montant_it_prestations_du_tranche_6', period, parameters)
        montant_it_ventes_du_tranche_6 = personne('montant_it_ventes_du_tranche_6', period, parameters)
        return montant_it_prestations_du_tranche_6 + montant_it_ventes_du_tranche_6


class montant_du_it_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 7 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_7 = personne('montant_it_prestations_du_tranche_7', period, parameters)
        montant_it_ventes_du_tranche_7 = personne('montant_it_ventes_du_tranche_7', period, parameters)
        return montant_it_prestations_du_tranche_7 + montant_it_ventes_du_tranche_7


class montant_du_it_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 8 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_8 = personne('montant_it_prestations_du_tranche_8', period, parameters)
        montant_it_ventes_du_tranche_8 = personne('montant_it_ventes_du_tranche_8', period, parameters)
        return montant_it_prestations_du_tranche_8 + montant_it_ventes_du_tranche_8


class montant_du_it_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 9 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_9 = personne('montant_it_prestations_du_tranche_9', period, parameters)
        montant_it_ventes_du_tranche_9 = personne('montant_it_ventes_du_tranche_9', period, parameters)
        return montant_it_prestations_du_tranche_9 + montant_it_ventes_du_tranche_9


class montant_du_it_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 10 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_10 = personne('montant_it_prestations_du_tranche_10', period, parameters)
        montant_it_ventes_du_tranche_10 = personne('montant_it_ventes_du_tranche_10', period, parameters)
        return montant_it_prestations_du_tranche_10 + montant_it_ventes_du_tranche_10


class montant_du_it_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 11 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_11 = personne('montant_it_prestations_du_tranche_11', period, parameters)
        montant_it_ventes_du_tranche_11 = personne('montant_it_ventes_du_tranche_11', period, parameters)
        return montant_it_prestations_du_tranche_11 + montant_it_ventes_du_tranche_11


class montant_du_it_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions sur la tranche 12 sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        montant_it_prestations_du_tranche_12 = personne('montant_it_prestations_du_tranche_12', period, parameters)
        montant_it_ventes_du_tranche_12 = personne('montant_it_ventes_du_tranche_12', period, parameters)
        return montant_it_prestations_du_tranche_12 + montant_it_ventes_du_tranche_12
