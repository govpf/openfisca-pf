# -*- coding: utf-8 -*-

# This file defines the computation for occupation on private domain using the market value defined for each area of each cities in the law DAF1620009AC-1.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_9(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, annuel, mensuel) de la redevance domaniale sur le domaine privée"
    reference = "Arrêté NOR DAF1620009AC-1"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '9', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'test_dom_priv')

        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        # zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)

        # Parameters
        montant_minimum = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].montant_minimum
        part_variable = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].part_variable
        valeur_venale = 100
        # valuer_venale = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_variable

        # Price computation
        montant_intermediaire = part_variable / 100 * valeur_venale * variable_redevance_domaniale

        # Minimum comparison
        montant_base = max_(arrondiSup(montant_intermediaire), montant_minimum)
        return where(type_calcul == '9', montant_base, 0)


class montant_total_redevance_domaniale_type_9(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant total de la redevance domaniale dûe sur le domùaine privé"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # multiple occupation can be asked with different type of computation.
        # In order to avoid misinterpretation for array input, only the element with the good type is computed
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '9', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'test_zone_archi')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)

        montant_base = personne('montant_base_redevance_domaniale_type_9', period)
        # zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].montant_minimum

        # Price computation on the whole duration
        montant_intermediaire = max_(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour, montant_minimum)

        # Price discount for religious activites
        montant_total = arrondiSup(montant_intermediaire)
        return where(type_calcul == '9', montant_total, 0)
