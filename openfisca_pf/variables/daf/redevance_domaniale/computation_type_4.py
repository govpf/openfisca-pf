# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies the same computation as type_3,
# with daily rates depending on the area.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums.enums import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_4(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier et les paramètres dépendant de la zone géographique"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Il n'y a pas de différence entre montant de basse et montant total pour ce type de calcul.

        return personne('montant_total_redevance_domaniale_type_4', period)


class montant_total_redevance_domaniale_type_4(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe avec un calcul dont le taux journalier évolue par palier et les paramètres dépendant de la zone géographique"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '4', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'im_eco_02_foire_produit_locaux')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        majoration_redevance_domaniale = personne('majoration_redevance_domaniale', period)
        activite_cultuelle = personne('activite_cultuelle', period)
        exoneration = parameters(period).daf.redevance_domaniale.exoneration.discount_rate

        # Parametres
        init = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].init
        threshold_1 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_2
        threshold_3 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].threshold_3
        rate_3 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].rate_3

        # Calcul du montant
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

        montant_total = arrondiSup((montant_intermediaire + majoration_redevance_domaniale) * (1 - exoneration * activite_cultuelle))

        return where(type_calcul == '4', montant_total, 0)


class temporalite_redevance_domaniale_type_4(Variable):
    value_type = Enum
    possible_values = Temporalite
    default_value = Temporalite.Non_Applicable
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"
