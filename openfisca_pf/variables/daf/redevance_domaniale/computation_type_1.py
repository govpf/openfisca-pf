# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies on a affin computation
#  with a constant part, a unitary part and a surfacic part
# See https://openfisca.org/doc/key-concepts/variables.html

# La formule de calcul de type 1 est une fonction du type montant = part_fixe + part_unitaire* nombre_unité + part_variable* quantité
# La variable peut être une surface, une longueur ou un volume.
# Il peut exister un montant minimum à payer
# Pour le moment certains tarifs sont évoqués à la semaine, à la journée ou à d'autre unité de temps, d'où l'idée du prorata


# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_pf.variables.daf.redevance_domaniale.input_parameters import activite_cultuelle
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *

class montant_base_redevance_domaniale_type_1(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, annuel, mensuel) pour la redevance domaniale dûe avec un calcul de type classique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)

        ##Récupération des paramètres
        part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].montant_minimum
        
        ##Calcul du montant
        montant_intermediaire = (part_fixe +
                        part_unitaire * nombre_unite_redevance_domaniale +
                        part_variable * variable_redevance_domaniale)

        ##Comparaison avec le minimum
        montant_base= max_(arrondiSup(montant_intermediaire), montant_minimum )

        return montant_base


class montant_total_redevance_domaniale_type_1(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant total de la redevance domaniale dûe avec un calcul de type classique"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        montant_base = personne('montant_base_redevance_domaniale_type_1',period)
        activite_cultuelle = personne('activite_cultuelle',period)

        ##Récupération des paramètres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].montant_minimum
        
        ##Calcul du montant total sur toute la durée de l'occupation
        montant_intermediaire = max_(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour + majoration_redevance_domaniale, montant_minimum)

        montant_total = arrondiSup(montant_intermediaire * (1 - 0.8 * activite_cultuelle))

        return montant_total