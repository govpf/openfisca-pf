# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    where,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne
from openfisca_pf.functions.currency import arrondi_inferieur


class montant_cstns_du(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Montant CST-NS total calculé'
    reference = [
        'https://www.impot-polynesie.gov.pf/essentiel/la-contribution-de-solidarite-territoriale-sur-les-professions-et-activites-non-salariees'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        cstns_ventes = personne('cstns_ventes', period)
        cstns_prestations = personne('cstns_prestations', period)
        return arrondi_inferieur(cstns_ventes + cstns_prestations)


class cstns_a_payer(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Montant cstns total à payer'
    reference = [
        'https://www.impot-polynesie.gov.pf/essentiel/la-contribution-de-solidarite-territoriale-sur-les-professions-et-activites-non-salariees'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        montant_cstns_du = personne('montant_cstns_du', period)
        return where(montant_cstns_du < 6000, 0, montant_cstns_du)


class montant_cstns_total_a_payer(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Montant IT total à payer, en prenant compte des déductions et des pénalités'
    reference = [
        'https://www.impot-polynesie.gov.pf/essentiel/la-contribution-de-solidarite-territoriale-sur-les-professions-et-activites-non-salariees'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('montant_cstns_du', period)


class redevable_cstns(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    label = "Défini si l'entreprise est éligible à la CST-NS"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/section-i-bases-et-personnes-imposables'
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('redevable_it', period)
