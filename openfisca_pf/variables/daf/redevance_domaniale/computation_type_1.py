# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies on a affin computation
#  with a constant part, a unitary part and a surfacic part
# See https://openfisca.org/doc/key-concepts/variables.html

# La formule de calcul de type 1 est une fonction du type montant = part_fixe + part_unitaire* nombre_unité + part_variable* quantité
# La variable peut être une surface, une longueur ou un volume.
# Il peut exister un montant minimum à payer
# Pour le moment certains tarifs sont évoqués à la semaine, à la journée ou à d'autre unité de temps, d'où l'idée du prorata


# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *

class montant_redevance_domaniale_type_1(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul de type classique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
    
        ##Récupération des paramètres
        part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_unitaire
        part_variable = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_variable
        montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].montant_minimum
        facteur_prorata = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].facteur_prorata

        ##Calcul du montant
        montant_intermediaire = (part_fixe +
                        part_unitaire * nombre_unite_redevance_domaniale +
                        part_variable * variable_redevance_domaniale) * duree_occupation_redevance_domaniale_jour / facteur_prorata

        ##Comparaison avec le minimum
        nb_periode_mini =  numpy.trunc(duree_occupation_redevance_domaniale_jour/facteur_prorata)

        montant_global= select(
                                [nb_periode_mini<=1, nb_periode_mini>1],
                                [max_(arrondiSup(montant_intermediaire), montant_minimum)  , max_(arrondiSup(montant_intermediaire), nb_periode_mini * montant_minimum )]
                                )

        return montant_global
