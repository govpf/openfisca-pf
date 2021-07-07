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

class montant_redevance_domaniale_type_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dépendant de la zone géographique de la demande"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        
        ##Récupération des paramètres
        part_fixe = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum
        unite_insecable = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].unite_insecable
        nb_periode_mini =  numpy.ceil(duree_occupation_redevance_domaniale_jour/unite_insecable) ##Use of ceil aims at taking into account that a started period has to be counted in the price
        
        ##Calcul du montant
        montant_intermediaire = (part_fixe +
                        part_unitaire * nombre_unite_redevance_domaniale +
                        part_variable * variable_redevance_domaniale) * nb_periode_mini

        ##Comparaison avec le minimum
        montant_global= max_(arrondiSup(montant_intermediaire), nb_periode_mini * montant_minimum )

        return montant_global

