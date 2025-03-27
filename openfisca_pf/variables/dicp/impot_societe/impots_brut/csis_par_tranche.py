# -*- coding: utf-8 -*-

from openfisca_pf.base import (ArrayLike, Period, DAY, Variable, where, isin, min_, ParameterNode, Population)
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activity import ACTIVITE_ABATTEMENT_CSIS, ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_CSIS


class csis_brut_base(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Csis base"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        resultat_fiscal = personne('is_resultat_fiscal_benefice_apres_report_deficitaire', period)
        return resultat_fiscal


class csis_brut_possede_abattement(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité possède un abattement CSIS ?"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_ABATTEMENT_CSIS)


class csis_brut_abattement_taux_saisie(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Abattement CSIS Saisie"


class csis_brut_abattement_taux_est_a_saisir(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Taux Abattement CSIS doit être saisie"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_CSIS)


class csis_brut_abattement_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Abattement CSIS"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return 0.0


class csis_brut_base_imposable(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Base CSIS Brut Imposable"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base = personne('csis_brut_base', period)
        abattement = personne('csis_brut_abattement_taux', period)
        return base * (1 - abattement)


# TRANCHE 0
class csis_brut_plancher_tranche_0(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plancher tranche 0"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.thresholds[0] + 1


class csis_brut_plafond_tranche_0(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plafond tranche 0"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.thresholds[1]


class csis_brut_taux_tranche_0(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "CSIS taux tranche 0"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.rates[0]


class csis_brut_base_imposable_tranche_0(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS base tranche 0"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base = personne('csis_brut_base_imposable', period)
        plancher = personne('csis_brut_plancher_tranche_0', period) - 1
        plafond = personne('csis_brut_plafond_tranche_0', period)
        tranche = min_(base, plafond) - plancher
        return where(tranche > 0, tranche, 0)


class csis_brut_due_tranche_0(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS montant due tranche 0"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        tranche = personne('csis_brut_base_imposable_tranche_0', period)
        taux = personne('csis_brut_taux_tranche_0', period)
        return tranche * taux


# TRANCHE 1
class csis_brut_plancher_tranche_1(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plancher tranche 1"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        plafond_precedent = personne('csis_brut_plafond_tranche_0', period)
        return plafond_precedent + 1


class csis_brut_plafond_tranche_1(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plafond tranche 1"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.thresholds[2]


class csis_brut_taux_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "CSIS taux tranche 1"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.rates[1]


class csis_brut_base_imposable_tranche_1(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS base tranche 1"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base = personne('csis_brut_base_imposable', period)
        plancher = personne('csis_brut_plancher_tranche_1', period) - 1
        plafond = personne('csis_brut_plafond_tranche_1', period)
        tranche = min_(base, plafond) - plancher
        return where(tranche > 0, tranche, 0)


class csis_brut_due_tranche_1(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS montant due tranche 1"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        tranche = personne('csis_brut_base_imposable_tranche_1', period)
        taux = personne('csis_brut_taux_tranche_1', period)
        return tranche * taux


# TRANCHE 2
class csis_brut_plancher_tranche_2(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plancher tranche 2"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        plafond_precedent = personne('csis_brut_plafond_tranche_1', period)
        return plafond_precedent + 1


class csis_brut_plafond_tranche_2(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plafond tranche 2"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.thresholds[3]


class csis_brut_taux_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "CSIS taux tranche 2"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.rates[2]


class csis_brut_base_imposable_tranche_2(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS base tranche 2"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base = personne('csis_brut_base_imposable', period)
        plancher = personne('csis_brut_plancher_tranche_2', period) - 1
        plafond = personne('csis_brut_plafond_tranche_2', period)
        tranche = min_(base, plafond) - plancher
        return where(tranche > 0, tranche, 0)


class csis_brut_due_tranche_2(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS montant due tranche 2"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        tranche = personne('csis_brut_base_imposable_tranche_2', period)
        taux = personne('csis_brut_taux_tranche_2', period)
        return tranche * taux


# TRANCHE 3
class csis_brut_plancher_tranche_3(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plancher tranche 3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        plafond_precedent = personne('csis_brut_plafond_tranche_2', period)
        return plafond_precedent + 1


class csis_brut_plafond_tranche_3(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plafond tranche 3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.thresholds[4]


class csis_brut_taux_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "CSIS taux tranche 3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.rates[3]


class csis_brut_base_imposable_tranche_3(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS base tranche 3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base = personne('csis_brut_base_imposable', period)
        plancher = personne('csis_brut_plancher_tranche_3', period) - 1
        plafond = personne('csis_brut_plafond_tranche_3', period)
        tranche = min_(base, plafond) - plancher
        return where(tranche > 0, tranche, 0)


class csis_brut_due_tranche_3(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS montant tranche 3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        tranche = personne('csis_brut_base_imposable_tranche_3', period)
        taux = personne('csis_brut_taux_tranche_3', period)
        return tranche * taux


# TRANCHE 4
class csis_brut_plancher_tranche_4(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS plancher tranche 3"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        plafond_precedent = personne('csis_brut_plafond_tranche_3', period)
        return plafond_precedent + 1


class csis_brut_taux_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "CSIS taux tranche 4"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return parameters(period).dicp.impot_societe.taux.csis.rates[4]


class csis_brut_base_imposable_tranche_4(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS base tranche 4"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base = personne('csis_brut_base_imposable', period)
        plancher = personne('csis_brut_plancher_tranche_4', period) - 1
        tranche = base - plancher
        return where(tranche > 0, tranche, 0)


class csis_brut_due_tranche_4(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS montant due tranche 4"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        tranche = personne('csis_brut_base_imposable_tranche_4', period)
        taux = personne('csis_brut_taux_tranche_4', period)
        return tranche * taux


class csis_brut_due(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "CSIS montant due"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        csis0 = personne('csis_brut_due_tranche_0', period)
        csis1 = personne('csis_brut_due_tranche_1', period)
        csis2 = personne('csis_brut_due_tranche_2', period)
        csis3 = personne('csis_brut_due_tranche_3', period)
        csis4 = personne('csis_brut_due_tranche_4', period)
        return csis0 + csis1 + csis2 + csis3 + csis4
