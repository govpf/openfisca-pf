# -*- coding: utf-8 -*-


"""
La Convention d'Insertion Sociale (CIS) est une aide financière pour les demandeurs d'emploi
en échange de travaux d'intérêt général versée par la Caisse de Prévoyance Sociale (CPS).
Elle est gérée par le Service de l'Emploi, de la Formation et de l'Insertion Professionnelle (SEFI) en Pilynésie Française.
"""


from openfisca_pf.base import (
    ADD,
    ArrayLike,
    MONTH,
    not_,
    ParameterNode,
    Period,
    Population,
    select,
    set_input_dispatch_by_period,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import BOOLEAN, HOURS_PER_MONTH, XPF_PER_MONTH
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impots import RegimeCPS


class nombre_heures_interet_general(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = int
    default_value = 0
    label = "Nombre d'heure d'intérêt général effectué par la personne au mois dans le cadre d'une convention Convesion d'Insertion Sociale"
    set_input = set_input_dispatch_by_period
    reference = [
        'https://www.actusefi.org/ie2021',
        'https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6037ef878dd5025a32e053bc/1614278537716/Loi+du+Pays+n%C2%B0+2021-12+du+24_02_2021.pdf',
        'https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6039c23be06ce403c29735d2/1614398021087/Arr%C3%AAt%C3%A9+n%C2%B0+210+CM+du+24_02_2021.pdf'
        ]
    unit = HOURS_PER_MONTH


class convention_cis_signee(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    label = "Indique si une convention Convesion d'Insertion Sociale à été signée par la personne ce mois ci"


class eligible_cis(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    label = "Eligibilité de la personne au Convesion d'Insertion Sociale au mois"
    reference = [
        'https://www.actusefi.org/ie2021',
        'https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6037ef878dd5025a32e053bc/1614278537716/Loi+du+Pays+n%C2%B0+2021-12+du+24_02_2021.pdf',
        'https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6039c23be06ce403c29735d2/1614398021087/Arr%C3%AAt%C3%A9+n%C2%B0+210+CM+du+24_02_2021.pdf'
        ]
    unit = BOOLEAN

    def formula_2021_02(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        regime_cps_valide = personne('regime_cps', period) == RegimeCPS.RSPF
        age = personne('age', period)
        age_min = parameters(period).sefi.cis.age_minimum
        age_max = parameters(period).sefi.cis.age_maximum
        return regime_cps_valide * (age <= age_max) * (age >= age_min)


class eligible_cis_annee(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = YEAR
    label = "Eligibilité de la personne au Convesion d'Insertion Sociale a l'année"
    reference = [
        'https://www.actusefi.org/ie2021',
        'https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6037ef878dd5025a32e053bc/1614278537716/Loi+du+Pays+n%C2%B0+2021-12+du+24_02_2021.pdf',
        'https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6039c23be06ce403c29735d2/1614398021087/Arr%C3%AAt%C3%A9+n%C2%B0+210+CM+du+24_02_2021.pdf'
        ]
    unit = BOOLEAN

    def formula_2021_02(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('eligible_cis', period, options = [ADD])

    def formula(personne: Population) -> ArrayLike:
        return False


class montant_cis(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = float
    default_value = 0.
    label = "Montant de Convention d'Insertion Sociale à verser à la Personne"
    reference = [
        'https://www.actusefi.org/ie2021',
        'https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6037ef878dd5025a32e053bc/1614278537716/Loi+du+Pays+n%C2%B0+2021-12+du+24_02_2021.pdf',
        'https://static1.squarespace.com/static/5e975fac2e07f80c8bf30dfb/t/6039c23be06ce403c29735d2/1614398021087/Arr%C3%AAt%C3%A9+n%C2%B0+210+CM+du+24_02_2021.pdf'
        ]
    unit = XPF_PER_MONTH

    def formula_2021_02(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        eligible_cis = personne('eligible_cis', period)
        nombre_heures_interet_general = personne('nombre_heures_interet_general', period.last_month)
        signature_convention_1_mois = personne('convention_cis_signee', period.last_month)
        signature_convention_2_mois = personne('convention_cis_signee', period.last_month.last_month)
        signature_convention_3_mois = personne('convention_cis_signee', period.last_month.last_month.last_month)
        montant_cis_maximal = parameters(period).sefi.cis.montant

        ratio = nombre_heures_interet_general / 20
        return eligible_cis * select(
            [
                signature_convention_1_mois,
                (signature_convention_2_mois + signature_convention_3_mois) * (ratio >= 1),
                (signature_convention_2_mois + signature_convention_3_mois) * (ratio < 1),
                not_(signature_convention_1_mois + signature_convention_2_mois + signature_convention_3_mois)
                ],
            [
                montant_cis_maximal,
                montant_cis_maximal,
                montant_cis_maximal * ratio,
                0
                ]
            )
