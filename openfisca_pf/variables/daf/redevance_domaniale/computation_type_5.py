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
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # multiple occupation can be asked with different type of computation.
        # In order to avoid misinterpretation for array input, only the element with the good type is computed
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '5', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'test_fonction_palier_surface')
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)

        # Parameters
        init = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].init
        rate_0 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_0
        threshold_1 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].rate_2

        montant_minimum = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].montant_minimum

        #  Price computation
        montant_intermediaire = select([variable_redevance_domaniale < threshold_1,
                                        variable_redevance_domaniale <= threshold_2,
                                        variable_redevance_domaniale > threshold_2],
                                        [init + rate_0 * variable_redevance_domaniale,
                                        init + rate_0 * threshold_1 + rate_1 * (variable_redevance_domaniale - threshold_1),
                                        init + rate_0 * threshold_1 + rate_1 * (threshold_2 - threshold_1) + rate_2 * (variable_redevance_domaniale - threshold_2)
                                        ])

        montant_base = max_(arrondiSup(montant_intermediaire), montant_minimum)

        return where(type_calcul == '5', montant_base, 0)


class montant_total_redevance_domaniale_type_5(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de total de la redevance domaniale dûe avec un calcul dont le montant annuel évolue par palier de surface"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'
    
    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # multiple occupation can be asked with different type of computation.
        # In order to avoid misinterpretation for array input, only the element with the good type is computed
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '5', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'test_fonction_palier_surface')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        montant_base = personne('montant_base_redevance_domaniale_type_5', period)

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_5[nature_emprise_occupation_redevance_domaniale].montant_minimum

        # Price computation on the whole duration
        montant_total = max_(arrondiSup(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour), montant_minimum) + majoration_redevance_domaniale
            # making two minimum comparison on basis price and on total price aims at including this minimum even if the duration is lower than the basic time.

        return where(type_calcul == '5', montant_total, 0)
