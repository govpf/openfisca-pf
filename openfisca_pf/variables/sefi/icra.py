# -*- coding: utf-8 -*-

"""
Le dispositif ICRA (Insertion par la Création ou la Reprise d'Activité) en Polynésie Française
vise à favoriser l'insertion professionnelle d'un demandeur d'emploi en soutenant son projet de création ou de reprise d'entreprise
par l'accompagnement d'un tuteur et le versement d'aides financières.
Pour bénéficier de ce dispositif, il faut être âgé de 18 à 55 ans inclus, sans activité professionnelle et en recherche d'emploi depuis au moins six mois en Polynésie française.
Les projets peuvent s'effectuer sous la forme d'une entreprise individuelle ou d'une société, à condition d'en exercer effectivement le contrôle.
"""


from openfisca_pf.base import (
    ADD,
    ArrayLike,
    MONTH,
    not_,
    ParameterNode,
    Period,
    Population,
    set_input_dispatch_by_period,
    Variable
    )
from openfisca_pf.constants.units import BOOLEAN, XPF_PER_MONTH
from openfisca_pf.entities import Personne


class beneficiaire_icra(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    set_input = set_input_dispatch_by_period
    unit = BOOLEAN
    label = "Est ce que la personne bénéficie de l'indemnité à l'Insertion par la Création ou la Reprise d'Activité ce mois ci ?"
    reference = [
        'https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument'
        ]


class eligible_icra(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Determine si la personne est eligible à demander l'indemnité à l'Insertion par la Création ou la Reprise d'Activité ce mois ci"
    reference = [
        'https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument'
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        nombre_annee_sans_icra = parameters(period).sefi.icra.nombre_annee_sans_icra
        nombre_mois_perte_emploi = parameters(period).sefi.icra.nombre_mois_perte_emploi
        age_minimum = parameters(period).sefi.icra.age_minimum
        age = personne('age', period)
        est_demandeur_emploi = personne('est_demandeur_emploi', period)
        patente = personne('patente', period)
        perte_emploi = personne('perte_emploi', period.offset(-nombre_mois_perte_emploi, 'month').start.period('month', nombre_mois_perte_emploi), options = [ADD])
        beneficiaire_icra = personne('beneficiaire_icra', period.offset(-nombre_annee_sans_icra, 'year').start.period('year', nombre_annee_sans_icra), options = [ADD])

        return (est_demandeur_emploi + perte_emploi) \
            * (age >= age_minimum) \
            * not_(beneficiaire_icra) \
            * not_(patente)


class montant_indemnite_icra(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = float
    default_value = 0.
    unit = XPF_PER_MONTH
    set_input = set_input_dispatch_by_period
    label = "Montant de l'indemnité à l'Insertion par la Création ou la Reprise d'Activité ce mois ci"
    reference = [
        'https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument'
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        eligible_icra = personne('eligible_icra', period)
        return parameters(period).sefi.icra.montant_indemnite * eligible_icra


class nombre_mois_indemnite_icra(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = int
    default_value = 0
    set_input = set_input_dispatch_by_period
    label = "Nombre de mois pendant lequels la personne bénéficiera de l'indemnité à l'Insertion par la Création ou la Reprise d'Activité après ce mois ci"
    reference = [
        'https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument'
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        eligible_icra = personne('eligible_icra', period)
        return parameters(period).sefi.icra.nombre_mois_indemnite * eligible_icra


class montant_prime_demarrage_icra(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = float
    default_value = 0.
    unit = XPF_PER_MONTH
    set_input = set_input_dispatch_by_period
    label = "Montant de la prime de demmarage de l'indemnité à l'Insertion par la Création ou la Reprise d'Activité ce mois ci"
    reference = [
        'https://www.sefi.pf/SefiWeb/SefiPublic.nsf/Mesures/ICRA?OpenDocument'
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        eligible_icra = personne('eligible_icra', period)
        return parameters(period).sefi.icra.montant_prime_demarrage * eligible_icra
