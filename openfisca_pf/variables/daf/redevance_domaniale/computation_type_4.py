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

class montant_base_redevance_domaniale_type_4(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier et les paramètres dépendant de la zone géographique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        ##Pour ce type de calcul il n'y a pas de différences entre le montant de base et le montant total
        ##Du coup, les deux montants sont égaux


        return  personne('montant_total_redevance_domaniale_type_4',period)

class montant_total_redevance_domaniale_type_4(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier et les paramètres dépendant de la zone géographique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)

        ##Récupération des paramètres
        init = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].init
        threshold_1 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_2
        threshold_3 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_3
        rate_3 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_3

        ## Calcul du montant
        #   les durées en jours inférieur à 1 vont passer dans le type_23, donc ne seront pas calculées ici.
        #   Si jamais, les durées inférieures à 1 jours suivent un calcul simples (linéaire, vis à vis du temps en jours), il faudra rajouter le terme rate_0 * duree pour avoir des calculs cohérents
        montant_intermediaire = select( [duree_occupation_redevance_domaniale_jour < threshold_1,
                                            duree_occupation_redevance_domaniale_jour <= threshold_2,
                                            duree_occupation_redevance_domaniale_jour <= threshold_3,
                                            duree_occupation_redevance_domaniale_jour > threshold_3],
                                            [ init ,
                                            init + rate_1 * (duree_occupation_redevance_domaniale_jour - threshold_1),
                                            init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (duree_occupation_redevance_domaniale_jour - threshold_2),
                                            init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (threshold_3 - threshold_2) +rate_3 * (duree_occupation_redevance_domaniale_jour - threshold_3)
                                            ])

        montant_global = arrondiSup( montant_intermediaire) + majoration_redevance_domaniale

        return montant_global
