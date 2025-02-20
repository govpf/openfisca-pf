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
from openfisca_pf.functions.tranches import creer_bareme


class it_ventes_avant_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions de ventes sans tenir compte de l'abattement de droits éventuel"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        total = 0.
        nombre_tranches_it_ventes = personne.pays('nombre_tranches_it_ventes', period, parameters)[0]
        for i in range(1, nombre_tranches_it_ventes + 1):
            total += personne(f'montant_it_ventes_du_tranche_{i}', period, parameters)
        return total


class it_ventes_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions de ventes ne bénéficiant pas de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        base_imposable_it_ventes_sans_abattement_droits = personne('base_imposable_it_ventes_sans_abattement_droits', period)
        bareme = creer_bareme(personne.pays, period, parameters, 'it', 'ventes')
        return bareme.calc(base_imposable_it_ventes_sans_abattement_droits)


class it_ventes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transactions de ventes suite à application de l'abattement sur les droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        it_ventes_abattement_droits = personne('it_ventes_abattement_droits', period, parameters)
        it_ventes_avant_abattement_droits = personne('it_ventes_avant_abattement_droits', period, parameters)
        return it_ventes_avant_abattement_droits - it_ventes_abattement_droits


class it_ventes_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Abattement de droit applique sur l'impôt sur les transactions de ventes"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        it_ventes_avant_abattement_droits = personne('it_ventes_avant_abattement_droits', period, parameters)
        it_ventes_sans_abattement_droits = personne('it_ventes_sans_abattement_droits', period, parameters)
        return (it_ventes_avant_abattement_droits - it_ventes_sans_abattement_droits) / 2
