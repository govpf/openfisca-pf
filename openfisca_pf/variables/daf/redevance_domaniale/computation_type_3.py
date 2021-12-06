# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies on a daily rating. The daily rate decreases after a week and after a month.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_3(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, pararameters):
        # There is no difference between montant_base and montant_total.
        # Then the too computation are set equal

        return personne('montant_total_redevance_domaniale_type_3', period)


class montant_total_redevance_domaniale_type_3(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # multiple occupation can be asked with different type of computation.
        # In order to avoid misinterpretation for array input, only the element with the good type is computed
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '3', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ip_eco_06_infra_restauration_aero')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        activite_cultuelle = personne('activite_cultuelle', period)

        # Parameters
        init = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].init
        threshold_1 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].rate_2
        threshold_3 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].threshold_3
        rate_3 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].rate_3

        # Price computation
        # For duration in hours and less than 1 day, the computation is set to type_23
        # If, the computation for hours is modified and become linear, the computation could be used adding a rate_0 in parameters
        montant_intermediaire = select([
            duree_occupation_redevance_domaniale_jour < threshold_1,
            duree_occupation_redevance_domaniale_jour <= threshold_2,
            duree_occupation_redevance_domaniale_jour <= threshold_3,
            duree_occupation_redevance_domaniale_jour > threshold_3
            ], [
                init,
                init + rate_1 * (duree_occupation_redevance_domaniale_jour - threshold_1),
                init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (duree_occupation_redevance_domaniale_jour - threshold_2),
                init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (threshold_3 - threshold_2) + rate_3 * (duree_occupation_redevance_domaniale_jour - threshold_3)
                ])

        montant_total = arrondiSup((montant_intermediaire + majoration_redevance_domaniale) * (1 - 0.8 * activite_cultuelle))

        return where(type_calcul == '3', montant_total, 0)


class temporalite_redevance_domaniale_type_3(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Temporality is not applicable for this computation based on the duration of the occupation

        return 'Not Applicable'