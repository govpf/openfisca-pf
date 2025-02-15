# -*- coding: utf-8 -*-

from openfisca_pf.base import (
    ArrayLike,
    Enum,
    floor,
    not_,
    OuiNon,
    Parameters,
    Period,
    round_,
    TypePersonne,
    Variable,
    where,
    YEAR
    )
from openfisca_pf.constants.units import XPF, BOOLEAN
from openfisca_pf.entities import Personne


class releve_de_charges_fourni(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = "True si l'entreprise a deposé un justificatif de charges, afin de bénéficier de l'abattement correspondant"
    reference = []
    unit = BOOLEAN


class annexes_it_fournies(Variable):
    value_type = Enum
    entity = Personne
    possible_values = OuiNon
    default_value = OuiNon.N
    definition_period = YEAR
    label = "True si l'entreprise a deposé les annexes à l'impot sur les transactions"
    reference = []
    unit = BOOLEAN


class base_imposable_it_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire concernant des prestations après abattement d'assiette mais sans abattement de droit"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        total = 0.
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            cca = str(parameters(period).dicp.abattements_it_cstns.activites_prestations[activite].cca)
            coeff_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].coeff_assiette
            seuil_abattement_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_d_assiette
            chiffre_d_affaire = personne(f'chiffre_affaire_{activite}', period, parameters)
            chiffre_d_affaire = floor(chiffre_d_affaire / 1000.) * 1000.

            # Si le chiffre d'affaire est sous un certian seuil, il n'y a pas de réduction
            # Sinon il y a une réduction sur la partie au dessus du seui
            total += where(
                chiffre_d_affaire <= seuil_abattement_assiette,
                chiffre_d_affaire,
                seuil_abattement_assiette + (chiffre_d_affaire - seuil_abattement_assiette) * (1 - coeff_assiette)
                )
        return round_(total)


class base_imposable_it_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire concernant des prestations après abattement de l'assiette, mais qui ne beneficiement pas d'un abattement de droit"
    reference = []
    unit = XPF

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        total = 0.
        charges_superieures_50_pourcents = personne('total_charges_releve_detaille', period) >= (personne('chiffre_affaire_total_prestations', period) / 2)
        releve_de_charges_fourni = personne('releve_de_charges_fourni', period) == OuiNon.O
        est_personne_physique = personne('type_personne', period) == TypePersonne.P
        annexes_it_fournies = personne('annexes_it_fournies', period) == OuiNon.O

        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            cca = str(parameters(period).dicp.abattements_it_cstns.activites_prestations[activite].cca)
            chiffre_d_affaire = personne(f'chiffre_affaire_{activite}', period, parameters)
            chiffre_d_affaire = floor(chiffre_d_affaire / 1000.) * 1000.
            coeff_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].coeff_assiette
            seuil_abattement_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_d_assiette
            abattement_droits = parameters(period).dicp.abattements_it_cstns.cca[cca].abattement_de_droit
            seuil_bascule_abattement_de_droit = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_de_droit
            seuils_abattement_de_droit_applicable_aux_personnes_physiques = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_de_droit_applicable_aux_personnes_physiques
            abattement_droits_charges = parameters(period).dicp.abattements_it_cstns.cca[cca].abattement_de_droit_avec_condition_de_charges
            seuil_annexe = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_justificatifs_a_fournir_abattement_de_droit_avec_condition_de_charges

            ca_apres_abattement_assiette = where(
                chiffre_d_affaire <= seuil_abattement_assiette,
                chiffre_d_affaire,
                seuil_abattement_assiette + (chiffre_d_affaire - seuil_abattement_assiette) * (1 - coeff_assiette)
                )

            # Ici nous ne tenons compte que du chiffre d'affaire sans abattements de droit
            abattement_de_droit_applicable = abattement_droits * (
                not_(abattement_droits_charges)
                + (est_personne_physique * not_(seuils_abattement_de_droit_applicable_aux_personnes_physiques))
                + (chiffre_d_affaire <= seuil_bascule_abattement_de_droit)
                )

            abattement_de_droit_de_charge_applicable = (
                abattement_droits_charges
                * (chiffre_d_affaire > seuil_bascule_abattement_de_droit)
                * charges_superieures_50_pourcents
                * releve_de_charges_fourni
                * (annexes_it_fournies + (chiffre_d_affaire <= seuil_annexe) + (est_personne_physique * not_(seuils_abattement_de_droit_applicable_aux_personnes_physiques)))
                )

            total += where(
                abattement_de_droit_applicable + abattement_de_droit_de_charge_applicable,
                0,
                ca_apres_abattement_assiette
                )
        return round_(total)
