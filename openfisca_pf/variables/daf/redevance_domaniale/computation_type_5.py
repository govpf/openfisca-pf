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


class montant_redevance_domaniale_type_5(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier et les paramètres dépendant de la zone géographique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        
        init = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].init
        threshold_1 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_2
        threshold_3 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_3
        rate_3 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_3
        
        return arrondiSup(
            select( [duree_occupation_redevance_domaniale_jour < threshold_1,
                    duree_occupation_redevance_domaniale_jour <= threshold_2,
                    duree_occupation_redevance_domaniale_jour > threshold_2],
                    [ init ,
                    init + rate_1 * (duree_occupation_redevance_domaniale_jour - threshold_1),
                    init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (duree_occupation_redevance_domaniale_jour - threshold_2)]))


