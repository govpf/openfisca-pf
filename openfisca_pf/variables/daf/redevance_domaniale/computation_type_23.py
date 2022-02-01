# -*- coding: utf-8 -*-

# This file defines the computation type_3 computation but with length expressed in hours.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_23(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe pour les occupations de moins d'une journée"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # There is no difference between montant_base and montant_total.
        # Then the too computation are set equal

        return personne('montant_total_redevance_domaniale_type_23', period)


class montant_total_redevance_domaniale_type_23(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe pour les occupations de moins d'une journée"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # multiple occupation can be asked with different type of computation.
        # In order to avoid misinterpretation for array input, only the element with the good type is computed
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '23', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'em_eco_01_espace_pelouse_ac_elec')
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)

        # Parameters
        tarif_horaire = parameters(period).daf.redevance_domaniale.type_23[nature_emprise_occupation_redevance_domaniale].tarif_horaire
        duree_demi_jour = parameters(period).daf.redevance_domaniale.type_23[nature_emprise_occupation_redevance_domaniale].duree_demi_jour
        tarif_demi_jour = parameters(period).daf.redevance_domaniale.type_23[nature_emprise_occupation_redevance_domaniale].tarif_demi_jour
        tarif_jour = parameters(period).daf.redevance_domaniale.type_23[nature_emprise_occupation_redevance_domaniale].tarif_jour

        # Price computation
        montant_intermediaire = select([
            duree_occupation_redevance_domaniale <= duree_demi_jour,
            duree_occupation_redevance_domaniale > duree_demi_jour
            ], [
                min_(tarif_horaire * duree_occupation_redevance_domaniale, tarif_demi_jour),
                min_(tarif_demi_jour + tarif_horaire * (duree_occupation_redevance_domaniale - 8), tarif_jour)
                ])

        montant_total = arrondiSup(montant_intermediaire) + majoration_redevance_domaniale

        return where(type_calcul == '23', montant_total, 0)


class temporalite_redevance_domaniale_type_23(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale dûe avec un calcul de type classique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Temporality is not applicable for this computation based on the duration of the occupation

        return 'Not Applicable'
