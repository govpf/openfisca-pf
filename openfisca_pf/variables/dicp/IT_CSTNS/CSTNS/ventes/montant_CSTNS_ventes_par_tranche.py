# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    arrondi_inferrieur,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne


class montant_cstns_ventes_du_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 1 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_1 = personne('base_imposable_cstns_ventes_tranche_1', period, parameters)
        taux_cstns_ventes_tranche_1 = personne.pays('taux_cstns_ventes_tranche_1', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_1 * taux_cstns_ventes_tranche_1)


class montant_cstns_ventes_du_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 2 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_2 = personne('base_imposable_cstns_ventes_tranche_2', period, parameters)
        taux_cstns_ventes_tranche_2 = personne.pays('taux_cstns_ventes_tranche_2', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_2 * taux_cstns_ventes_tranche_2)


class montant_cstns_ventes_du_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 3 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_3 = personne('base_imposable_cstns_ventes_tranche_3', period, parameters)
        taux_cstns_ventes_tranche_3 = personne.pays('taux_cstns_ventes_tranche_3', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_3 * taux_cstns_ventes_tranche_3)


class montant_cstns_ventes_du_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 4 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_4 = personne('base_imposable_cstns_ventes_tranche_4', period, parameters)
        taux_cstns_ventes_tranche_4 = personne.pays('taux_cstns_ventes_tranche_4', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_4 * taux_cstns_ventes_tranche_4)


class montant_cstns_ventes_du_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 5 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_5 = personne('base_imposable_cstns_ventes_tranche_5', period, parameters)
        taux_cstns_ventes_tranche_5 = personne.pays('taux_cstns_ventes_tranche_5', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_5 * taux_cstns_ventes_tranche_5)


class montant_cstns_ventes_du_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 6 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_6 = personne('base_imposable_cstns_ventes_tranche_6', period, parameters)
        taux_cstns_ventes_tranche_6 = personne.pays('taux_cstns_ventes_tranche_6', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_6 * taux_cstns_ventes_tranche_6)


class montant_cstns_ventes_du_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 7 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_7 = personne('base_imposable_cstns_ventes_tranche_7', period, parameters)
        taux_cstns_ventes_tranche_7 = personne.pays('taux_cstns_ventes_tranche_7', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_7 * taux_cstns_ventes_tranche_7)


class montant_cstns_ventes_du_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 8 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_8 = personne('base_imposable_cstns_ventes_tranche_8', period, parameters)
        taux_cstns_ventes_tranche_8 = personne.pays('taux_cstns_ventes_tranche_8', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_8 * taux_cstns_ventes_tranche_8)


class montant_cstns_ventes_du_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 9 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_9 = personne('base_imposable_cstns_ventes_tranche_9', period, parameters)
        taux_cstns_ventes_tranche_9 = personne.pays('taux_cstns_ventes_tranche_9', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_9 * taux_cstns_ventes_tranche_9)


class montant_cstns_ventes_du_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 10 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_10 = personne('base_imposable_cstns_ventes_tranche_10', period, parameters)
        taux_cstns_ventes_tranche_10 = personne.pays('taux_cstns_ventes_tranche_10', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_10 * taux_cstns_ventes_tranche_10)


class montant_cstns_ventes_du_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 11 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_11 = personne('base_imposable_cstns_ventes_tranche_11', period, parameters)
        taux_cstns_ventes_tranche_11 = personne.pays('taux_cstns_ventes_tranche_11', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_11 * taux_cstns_ventes_tranche_11)


class montant_cstns_ventes_du_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 12 sur les ventes sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-ii-taux'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_cstns_ventes_tranche_12 = personne('base_imposable_cstns_ventes_tranche_12', period, parameters)
        taux_cstns_ventes_tranche_12 = personne.pays('taux_cstns_ventes_tranche_12', period, parameters)
        return arrondi_inferrieur(base_imposable_cstns_ventes_tranche_12 * taux_cstns_ventes_tranche_12)
