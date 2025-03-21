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
from openfisca_pf.functions.tranches import creer_bareme


class cstns_ventes_avant_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant cstns sur les ventes sans tenir compte de l'abattement de droits"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        total = 0.
        nombre_tranches = personne.pays('nombre_tranches_cstns_ventes', period, parameters)[0]
        for i in range(1, nombre_tranches + 1):
            total += personne(f'montant_cstns_ventes_du_tranche_{i}', period)
        return total


class cstns_ventes_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant cstns sur les ventes ne bénéficiant pas de l'abattement de droits"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        chiffre_d_affaire = personne('base_imposable_cstns_ventes_sans_abattement_droits', period)
        bareme = creer_bareme(personne.pays, period, parameters, 'cstns', 'ventes')
        return bareme.calc(chiffre_d_affaire)


class cstns_ventes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant cstns sur les ventes, suite à application de l'abattement sur les droits"
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        cstns_ventes_abattement_droits = personne('cstns_ventes_abattement_droits', period)
        cstns_ventes_avant_abattement_droits = personne('cstns_ventes_avant_abattement_droits', period)
        return cstns_ventes_avant_abattement_droits - cstns_ventes_abattement_droits


class cstns_ventes_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = 'Abattement de droit appliqué sur la CST NS des ventes'
    reference = []
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        cstns_ventes_avant_abattement_droits = personne('cstns_ventes_avant_abattement_droits', period)
        cstns_ventes_sans_abattement_droits = personne('cstns_ventes_sans_abattement_droits', period)
        return (cstns_ventes_avant_abattement_droits - cstns_ventes_sans_abattement_droits) / 2
