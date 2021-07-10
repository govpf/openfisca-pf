# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies the same computation as type_1,
# but the parameters depends on a area.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class montant_redevance_domaniale_type_23(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe pour les occupations de moins d'une journée"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)

        ##Récupération des paramètres
        tarif_horaire = parameters(period).daf.redevance_domaniale.type_23[nature_emprise_occupation_redevance_domaniale].tarif_horaire
        duree_demi_jour = parameters(period).daf.redevance_domaniale.type_23[nature_emprise_occupation_redevance_domaniale].duree_demi_jour
        tarif_demi_jour = parameters(period).daf.redevance_domaniale.type_23[nature_emprise_occupation_redevance_domaniale].tarif_demi_jour
        tarif_jour = parameters(period).daf.redevance_domaniale.type_23[nature_emprise_occupation_redevance_domaniale].tarif_jour

        ##Calcul du montant
        montant_intermediaire  = select( [duree_occupation_redevance_domaniale <= duree_demi_jour,
                                            duree_occupation_redevance_domaniale > duree_demi_jour],
                                         [ min_(tarif_horaire*duree_occupation_redevance_domaniale, tarif_demi_jour) ,
                                            tarif_jour]
                                        )
        
        montant_global= arrondiSup(montant_intermediaire) + majoration_redevance_domaniale

        return montant_global





