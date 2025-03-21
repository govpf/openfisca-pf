# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne
from openfisca_pf.functions.currency import arrondi_inferieur


class montant_cstns_ventes_du_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 1 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_1 = personne('base_imposable_cstns_ventes_tranche_1', period)
        taux_cstns_ventes_tranche_1 = personne.pays('taux_cstns_ventes_tranche_1', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_1 * taux_cstns_ventes_tranche_1)


class montant_cstns_ventes_du_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 2 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_2 = personne('base_imposable_cstns_ventes_tranche_2', period)
        taux_cstns_ventes_tranche_2 = personne.pays('taux_cstns_ventes_tranche_2', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_2 * taux_cstns_ventes_tranche_2)


class montant_cstns_ventes_du_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 3 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_3 = personne('base_imposable_cstns_ventes_tranche_3', period)
        taux_cstns_ventes_tranche_3 = personne.pays('taux_cstns_ventes_tranche_3', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_3 * taux_cstns_ventes_tranche_3)


class montant_cstns_ventes_du_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 4 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_4 = personne('base_imposable_cstns_ventes_tranche_4', period)
        taux_cstns_ventes_tranche_4 = personne.pays('taux_cstns_ventes_tranche_4', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_4 * taux_cstns_ventes_tranche_4)


class montant_cstns_ventes_du_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 5 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_5 = personne('base_imposable_cstns_ventes_tranche_5', period)
        taux_cstns_ventes_tranche_5 = personne.pays('taux_cstns_ventes_tranche_5', period, parameters)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_5 * taux_cstns_ventes_tranche_5)


class montant_cstns_ventes_du_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 6 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_6 = personne('base_imposable_cstns_ventes_tranche_6', period)
        taux_cstns_ventes_tranche_6 = personne.pays('taux_cstns_ventes_tranche_6', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_6 * taux_cstns_ventes_tranche_6)


class montant_cstns_ventes_du_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 7 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_7 = personne('base_imposable_cstns_ventes_tranche_7', period)
        taux_cstns_ventes_tranche_7 = personne.pays('taux_cstns_ventes_tranche_7', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_7 * taux_cstns_ventes_tranche_7)


class montant_cstns_ventes_du_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 8 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_8 = personne('base_imposable_cstns_ventes_tranche_8', period)
        taux_cstns_ventes_tranche_8 = personne.pays('taux_cstns_ventes_tranche_8', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_8 * taux_cstns_ventes_tranche_8)


class montant_cstns_ventes_du_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 9 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_9 = personne('base_imposable_cstns_ventes_tranche_9', period)
        taux_cstns_ventes_tranche_9 = personne.pays('taux_cstns_ventes_tranche_9', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_9 * taux_cstns_ventes_tranche_9)


class montant_cstns_ventes_du_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 10 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_10 = personne('base_imposable_cstns_ventes_tranche_10', period)
        taux_cstns_ventes_tranche_10 = personne.pays('taux_cstns_ventes_tranche_10', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_10 * taux_cstns_ventes_tranche_10)


class montant_cstns_ventes_du_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 11 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_11 = personne('base_imposable_cstns_ventes_tranche_11', period)
        taux_cstns_ventes_tranche_11 = personne.pays('taux_cstns_ventes_tranche_11', period, parameters)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_11 * taux_cstns_ventes_tranche_11)


class montant_cstns_ventes_du_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 12 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_12 = personne('base_imposable_cstns_ventes_tranche_12', period)
        taux_cstns_ventes_tranche_12 = personne.pays('taux_cstns_ventes_tranche_12', period)
        return arrondi_inferieur(base_imposable_cstns_ventes_tranche_12 * taux_cstns_ventes_tranche_12)
