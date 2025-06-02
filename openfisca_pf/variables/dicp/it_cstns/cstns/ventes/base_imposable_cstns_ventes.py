# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    floor,
    not_,
    Parameters,
    Period,
    round_,
    Variable,
    where,
    YEAR
    )
from openfisca_pf.constants.units import XPF
from openfisca_pf.entities import Personne
from openfisca_pf.enums.common import OuiNon
from openfisca_pf.enums.impots import TypePersonne


class base_imposable_cstns_ventes(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire concernant des ventes après abattement d'assiette mais sans abattement de droit"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        total = 0.
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_ventes]:
            cca = str(parameters(period).dicp.abattements_it_cstns.activites_ventes[activite].cca)
            coeff_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].coeff_assiette
            seuil_abattement_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_d_assiette
            chiffre_d_affaire = personne(f'chiffre_affaire_{activite}', period, parameters)
            chiffre_d_affaire = floor(chiffre_d_affaire / 1000.) * 1000.

            # Si le chiffre d'affaire est sous un certain seuil d'assiette, alors il n'y a pas de réduction
            # Sinon une réduction s'applique sur la partie qui dépasse le suille
            total += where(
                (chiffre_d_affaire <= seuil_abattement_assiette),
                chiffre_d_affaire,
                seuil_abattement_assiette + (chiffre_d_affaire - seuil_abattement_assiette) * (1 - coeff_assiette)
                )
        return round_(total)


class base_imposable_cstns_ventes_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire concernant des ventes après abattement de l'assiette, mais qui ne beneficiement pas d'un abattement de droit"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        charges_superieures_50_pourcents = personne('total_charges_releve_detaille', period, parameters) >= (personne('chiffre_affaire_total_ventes', period, parameters) / 2)
        releve_de_charges_fourni = personne('releve_de_charges_fourni', period, parameters) == OuiNon.O
        est_personne_physique = personne('type_personne', period, parameters) == TypePersonne.P
        annexes_it_fournies = personne('annexes_it_fournies', period, parameters) == OuiNon.O

        total = 0.
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_ventes]:
            cca = str(parameters(period).dicp.abattements_it_cstns.activites_ventes[activite].cca)
            coeff_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].coeff_assiette
            seuil_abattement_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_d_assiette
            abattement_droits = parameters(period).dicp.abattements_it_cstns.cca[cca].abattement_de_droit
            seuil_bascule_abattement_de_droit = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_de_droit
            seuils_abattement_de_droit_applicable_aux_personnes_physiques = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_de_droit_applicable_aux_personnes_physiques
            abattement_droits_charges = parameters(period).dicp.abattements_it_cstns.cca[cca].abattement_de_droit_avec_condition_de_charges
            seuil_annexe = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_justificatifs_a_fournir_abattement_de_droit_avec_condition_de_charges

            chiffre_d_affaire = personne(f'chiffre_affaire_{activite}', period, parameters)
            chiffre_d_affaire = floor(chiffre_d_affaire / 1000.) * 1000.

            # Si le chiffre d'affaire est sous un certain seuil d'assiette, alors il n'y a pas de réduction
            # Sinon une réduction s'applique sur la partie qui dépasse le suille
            ca_apres_abattement_assiette = where(
                chiffre_d_affaire <= seuil_abattement_assiette,
                chiffre_d_affaire,
                seuil_abattement_assiette + (chiffre_d_affaire - seuil_abattement_assiette) * (1 - coeff_assiette)
                )

            # Ici on ne tient compte que du chiffre d'affaire sans les abattement de droits
            abattement_de_droit_applicable = (
                abattement_droits * (
                    not_(abattement_droits_charges) + (
                        est_personne_physique * not_(seuils_abattement_de_droit_applicable_aux_personnes_physiques)
                        )
                    + (chiffre_d_affaire <= seuil_bascule_abattement_de_droit)
                    )
                )
            abattement_de_droit_de_charge_applicable = (
                abattement_droits_charges
                * (chiffre_d_affaire > seuil_bascule_abattement_de_droit)
                * charges_superieures_50_pourcents
                * releve_de_charges_fourni
                * (annexes_it_fournies
                   + (chiffre_d_affaire <= seuil_annexe)
                   + (est_personne_physique * not_(seuils_abattement_de_droit_applicable_aux_personnes_physiques))
                   )
                )

            total += where(
                abattement_de_droit_applicable + abattement_de_droit_de_charge_applicable,
                0,
                ca_apres_abattement_assiette
                )
        return round_(total)
