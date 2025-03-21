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


class it_prestations_avant_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transtactions de prestation sans tenir compte de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        total = 0.
        nombre_tranches_it_prestations = personne.pays('nombre_tranches_it_prestations', period)[0]
        for i in range(1, nombre_tranches_it_prestations + 1):
            total += personne(f'montant_it_prestations_du_tranche_{i}', period)
        return total


class it_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transtactions de prestations ne bénéficiant pas de l'abattement de droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_it_ventes = personne('base_imposable_it_ventes', period) / 4
        bareme = creer_bareme(personne.pays, period, 'it', 'prestations')
        ca = personne('base_imposable_it_prestations_sans_abattement_droits', period)
        return bareme.calc(base_imposable_it_ventes + ca) - bareme.calc(base_imposable_it_ventes)


class it_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Impôt sur les transtactions de prestations, suite à application de l'abattement sur les droits"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        it_prestations_avant_abattement_droits = personne('it_prestations_avant_abattement_droits', period)
        it_prestations_abattement_droits = personne('it_prestations_abattement_droits', period)
        return it_prestations_avant_abattement_droits - it_prestations_abattement_droits


class it_prestations_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Abattement de droit s'appliquant à l'impôt sur les transtactions de prestations"
    reference = [
        'https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot',
        'https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47'
        ]
    unit = XPF

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        it_prestations_avant_abattement_droits = personne('it_prestations_avant_abattement_droits', period)
        it_prestations_sans_abattement_droits = personne('it_prestations_sans_abattement_droits', period)
        return (it_prestations_avant_abattement_droits - it_prestations_sans_abattement_droits) / 2
