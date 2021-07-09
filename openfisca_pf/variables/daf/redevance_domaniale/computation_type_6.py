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


class montant_redevance_domaniale_type_6(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)

        ##Récupération des paramètres
        init = parameters(period).daf.redevance_domaniale.type_6[nature_emprise_occupation_redevance_domaniale].init
        threshold_1 = parameters(period).daf.redevance_domaniale.type_6[nature_emprise_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_6[nature_emprise_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_6[nature_emprise_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_6[nature_emprise_occupation_redevance_domaniale].rate_2
        threshold_3 = parameters(period).daf.redevance_domaniale.type_6[nature_emprise_occupation_redevance_domaniale].threshold_3
        rate_3 = parameters(period).daf.redevance_domaniale.type_6[nature_emprise_occupation_redevance_domaniale].rate_3
        
        daily_rate_1 = rate_1 * variable_redevance_domaniale
        daily_rate_2 = rate_2 * variable_redevance_domaniale
        daily_rate_3 = rate_3 * variable_redevance_domaniale
        ## Calcul du montant
        #   les durées en jours inférieur à 1 n'ont pas de sens
        montant_global = arrondiSup(
                                    select( [duree_occupation_redevance_domaniale_jour < threshold_1,
                                            duree_occupation_redevance_domaniale_jour <= threshold_2,
                                            duree_occupation_redevance_domaniale_jour <= threshold_3,
                                            duree_occupation_redevance_domaniale_jour > threshold_3],
                                            [ init,
                                            init + daily_rate_1 * (duree_occupation_redevance_domaniale_jour - threshold_1),
                                            init + daily_rate_1 * (threshold_2 - threshold_1) + daily_rate_2 * (duree_occupation_redevance_domaniale_jour - threshold_2),
                                            init + daily_rate_1 * (threshold_2 - threshold_1) + daily_rate_2 * (threshold_3 - threshold_2) +daily_rate_3 * (duree_occupation_redevance_domaniale_jour - threshold_3)
                                            ])
                                    )


        return montant_global
