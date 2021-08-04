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


class montant_base_redevance_domaniale_type_5(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, mensuel, annuel) de la redevance domaniale dûe avec un calcul dont le montant annuel évolue par palier de surface"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)

        ##Récupération des paramètres
        init = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].init
        rate_0 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_0
        threshold_1 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_2
        
        montant_minimum = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].montant_minimum

        ## Calcul du montant
        montant_intermediaire = select( [variable_redevance_domaniale < threshold_1,
                                            variable_redevance_domaniale <= threshold_2,
                                            variable_redevance_domaniale > threshold_2],
                                            [ init + rate_0 * variable_redevance_domaniale,
                                            init + rate_0 * threshold_1 + rate_1 * (variable_redevance_domaniale - threshold_1),
                                            init + rate_0 * threshold_1 + rate_1 * (threshold_2 - threshold_1) + rate_2 * (variable_redevance_domaniale - threshold_2)
                                            ]
                                    )

        montant_base= max_(arrondiSup(montant_intermediaire), montant_minimum )
        
        return montant_base

class montant_total_redevance_domaniale_type_5(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de total de la redevance domaniale dûe avec un calcul dont le montant annuel évolue par palier de surface"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        montant_base = personne('montant_base_redevance_domaniale_type_5',period)

        ##Récupération des paramètres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].montant_minimum

        ##Calcul du montant total sur toute la durée de l'occupation
        montant_total = max_(arrondiSup(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour), montant_minimum) + majoration_redevance_domaniale
            ##Le fait de metttre deux fois le minimum permet de palier aussi le fait que la durée soit inférieure à l'unité de basse de calcul

        return montant_total