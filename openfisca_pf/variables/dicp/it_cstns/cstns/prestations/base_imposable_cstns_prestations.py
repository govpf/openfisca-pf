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
from openfisca_pf.entities import Personne
from openfisca_pf.enums.common import OuiNon
from openfisca_pf.enums.impots import TypePersonne


class base_imposable_cstns_prestations(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire concernant des prestations après abattement d'assiette mais sans abattement de droit"
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        total = 0.
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:
            cca = str(parameters(period).dicp.abattements_it_cstns.activites_prestations[activite].cca)
            coeff_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].coeff_assiette
            seuil_abattement_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_d_assiette
            chiffre_d_affaire_activite = personne(f'chiffre_affaire_{activite}', period)
            chiffre_d_affaire_activite = floor(chiffre_d_affaire_activite / 1000.) * 1000.
            # Si le chiffre d'affaire ne dépasse pas un certain seuil, il n'y a pas de reduction,
            # sinon une réduction s'applique sur la partie du chiffre d'affaire supérieur au seuil
            total += where(
                (chiffre_d_affaire_activite <= seuil_abattement_assiette),
                chiffre_d_affaire_activite,
                seuil_abattement_assiette + (chiffre_d_affaire_activite - seuil_abattement_assiette) * (1 - coeff_assiette)
                )
        return round_(total)


class base_imposable_cstns_prestations_sans_abattement_droits(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = "Montant total du chiffre d'affaire concernant des prestations après abattement de l'assiette, mais qui ne beneficiement pas d'un abattement de droit"
    reference = []

    def formula(personne: Personne, period: Period, parameters: Parameters) -> ArrayLike:
        value = 0.
        total_charges_releve_detaille = personne('total_charges_releve_detaille', period, parameters)
        chiffre_affaire_total_prestations = personne('chiffre_affaire_total_prestations', period, parameters)
        releve_de_charges_fourni = personne('releve_de_charges_fourni', period, parameters) == OuiNon.O
        est_personne_physique = personne('type_personne', period, parameters) == TypePersonne.P
        annexes_it_fournies = personne('annexes_it_fournies', period, parameters) == OuiNon.O

        charges_superieures_50_pourcents = total_charges_releve_detaille >= (chiffre_affaire_total_prestations / 2.)
        for activite in [*parameters(period).dicp.abattements_it_cstns.activites_prestations]:

            cca = str(parameters(period).dicp.abattements_it_cstns.activites_prestations[activite].cca)
            ca_activite = floor(personne(f'chiffre_affaire_{activite}', period, parameters) / 1000.) * 1000.
            coeff_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].coeff_assiette
            abattement_droits = parameters(period).dicp.abattements_it_cstns.cca[cca].abattement_de_droit
            abattement_droits_charges = parameters(period).dicp.abattements_it_cstns.cca[cca].abattement_de_droit_avec_condition_de_charges
            seuils_abattement_de_droit_applicable_aux_personnes_physiques = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_de_droit_applicable_aux_personnes_physiques
            seuil_abattement_assiette = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_d_assiette
            seuil_annexe = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_justificatifs_a_fournir_abattement_de_droit_avec_condition_de_charges
            seuil_bascule_abattement_de_droit = parameters(period).dicp.abattements_it_cstns.cca[cca].seuil_abattement_de_droit

            ca_apres_abattement_assiette = where(
                ca_activite <= seuil_abattement_assiette,
                ca_activite,
                seuil_abattement_assiette + (ca_activite - seuil_abattement_assiette) * (1 - coeff_assiette)
                )

            # Ici nous ne prenons en compte que les chiffre d'affaire sans abattement de droits
            abattement_de_droit_applicable = abattement_droits * (
                not_(abattement_droits_charges) + (ca_activite <= seuil_bascule_abattement_de_droit) + (
                    est_personne_physique * not_(seuils_abattement_de_droit_applicable_aux_personnes_physiques)
                    )
                )
            abattement_de_droit_de_charge_applicable = (
                abattement_droits_charges
                * (ca_activite > seuil_bascule_abattement_de_droit)
                * charges_superieures_50_pourcents
                * releve_de_charges_fourni
                * (annexes_it_fournies + (ca_activite <= seuil_annexe) + (
                    est_personne_physique * not_(seuils_abattement_de_droit_applicable_aux_personnes_physiques)
                    ))
                )
            value += where(
                (abattement_de_droit_applicable + abattement_de_droit_de_charge_applicable),
                0,
                ca_apres_abattement_assiette
                )
        return round_(value)
