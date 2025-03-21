# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne
from openfisca_pf.functions.tranches import creer_bareme


class cstns_prestations_avant_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant cstns sur les prestation sans tenir compte de l'abattement de droits"
    reference = 'https://www.impot-polynesie.gov.pf/code/section-ii-taux'

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        total = 0.
        nombre_tranches_cstns_prestations = personne.pays('nombre_tranches_cstns_prestations', period, parameters)[0]
        for i in range(1, nombre_tranches_cstns_prestations + 1):
            total += personne(f'montant_cstns_prestations_du_tranche_{i}', period)
        return total


class cstns_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant cstns sur les prestation ne bénéficiant pas de l'abattement de droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-i-bases-et-personnes-imposables"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        base_imposable_cstns_ventes = personne('base_imposable_cstns_ventes', period) / 4
        chiffre_d_affaire = personne('base_imposable_cstns_prestations_sans_abattement_droits', period)
        bareme = creer_bareme(personne.pays, period, parameters, 'cstns', 'prestations')
        return bareme.calc(base_imposable_cstns_ventes + chiffre_d_affaire) - bareme.calc(base_imposable_cstns_ventes)


class cstns_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant cstns sur les prestations, suite à application de l'abattement sur les droits"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        cstns_prestations_avant_abattement_droits = personne('cstns_prestations_avant_abattement_droits', period)
        cstns_prestations_abattement_droits = personne('cstns_prestations_abattement_droits', period)
        cstns = cstns_prestations_avant_abattement_droits - cstns_prestations_abattement_droits
        return cstns


class cstns_prestations_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Abattement de droit applique sur la CST-NS des prestations"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        cstns_prestations_avant_abattement_droits = personne('cstns_prestations_avant_abattement_droits', period)
        cstns_prestations_sans_abattement_droits = personne('cstns_prestations_sans_abattement_droits', period)
        return (cstns_prestations_avant_abattement_droits - cstns_prestations_sans_abattement_droits) / 2
