# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.functions.currency import arrondi_inferieur


class montant_cstns_prestations_du_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 1 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_1', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_1', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 2 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_2', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_2', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 3 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_3', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_3', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 4 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_4', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_4', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 5 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_5', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_5', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 6 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_6', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_6', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 7 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_7', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_7', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 8 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_8', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_8', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 9 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_9', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_9', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 10 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_10', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_10', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 11 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_11', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_11', period, parameters)
        return arrondi_inferieur(base_imposable * taux)


class montant_cstns_prestations_du_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant de CST-NS de la tranche 12 sur les prestations sans tenir compte de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable = personne('base_imposable_cstns_prestations_tranche_12', period, parameters)
        taux = personne.pays('taux_cstns_prestations_tranche_12', period, parameters)
        return arrondi_inferieur(base_imposable * taux)
