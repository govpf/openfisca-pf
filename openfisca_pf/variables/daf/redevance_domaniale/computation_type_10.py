# -*- coding: utf-8 -*-

# This file defines the computation for occupation on private domain using the market value defined for each area of each cities in the law DAF1620009AC-1.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.variables.daf.redevance_domaniale.enums_loc import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_10(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de annuel de la redevance domaniale sur les lotissements agricoles"
    reference = "Arrêté NOR DAF1620009AC-1"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '10', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ag_priv_06_lot_agri')
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        code_commune = personne('commune_redevance_domaniale', period)
        zone_lot_agri = personne('zone_lot_agri', period)

        # Parameters
        montant_minimum = parameters(period).daf.redevance_domaniale.type_10[nature_emprise_occupation_redevance_domaniale].montant_minimum
        part_variable = parameters(period).daf.redevance_domaniale.type_10[nature_emprise_occupation_redevance_domaniale].part_variable

        tempValue = []
        index = 0
        for item in code_commune.decode():
            value = parameters(period).daf.redevance_domaniale.lot_agricole[item.name][zone_lot_agri].loyer[index]
            index = index + 1
            tempValue.append(value)
        loyer = numpy.array(tempValue)

        # Price computation
        montant_intermediaire = part_variable / 100 * loyer * variable_redevance_domaniale
        # Minimum comparison
        montant_base = max_(arrondiSup(montant_intermediaire), montant_minimum)

        return where(type_calcul == '10', montant_base, 0)


class montant_total_redevance_domaniale_type_10(Variable):
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
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '10', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ag_priv_06_lot_agri')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)

        montant_base = personne('montant_base_redevance_domaniale_type_10', period)

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_10[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_10[nature_emprise_occupation_redevance_domaniale].montant_minimum

        # Price computation on the whole duration
        montant_intermediaire = max_(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour, montant_minimum)

        # Price discount for religious activites
        montant_total = arrondiSup(montant_intermediaire)
        return where(type_calcul == '10', montant_total, 0)


class temporalite_redevance_domaniale_type_10(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # multiple occupation can be asked with different type of computation.
        # In order to avoid misinterpretation for array input, only the element with the good type is computed
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '10', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'ag_priv_06_lot_agri')
        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_10[nature_emprise_occupation_redevance_domaniale].base_calcul_jour

        # Transformation
        temporalite = select([
            base_calcul_jour == 1,
            base_calcul_jour == 7,
            base_calcul_jour == 30,
            base_calcul_jour == 360
            ], [
                'Journalier',
                'Hebdomadaire',
                'Mensuel',
                'Annuel'
                ])

        return where(type_calcul == '10', temporalite, 'Not Applicable')
