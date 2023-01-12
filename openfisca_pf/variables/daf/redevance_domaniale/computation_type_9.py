# -*- coding: utf-8 -*-

# This file defines the computation for occupation on private domain using the market value defined for each area of each cities in the law DAF1620009AC-1.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums.enums import *
from openfisca_pf.variables.daf.redevance_domaniale.enums.enums_localisations import *
from openfisca_pf.base import *


class montant_base_redevance_domaniale_type_9(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de base (journalier, annuel, mensuel) de la redevance domaniale sur le domaine privé"
    reference = "Arrêté NOR DAF1620009AC-1"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '9', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'priv_09_autres')
        variable_redevance_domaniale = personne('variable_redevance_domaniale', period)
        code_commune = personne('commune_redevance_domaniale', period)
        zone_domaine_prive = personne('zone_domaine_prive', period)

        # Parametres
        montant_minimum = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].montant_minimum
        part_variable = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].part_variable

        tempValue = []
        index = 0
        for item in code_commune.decode():
            value = parameters(period).daf.redevance_domaniale.commune_prive[item.name][zone_domaine_prive.decode()[index].name].valeur_venale
            index = index + 1
            tempValue.append(value)
        valeur_venale = numpy.array(tempValue)

        # Calcul du montant
        montant_intermediaire = part_variable / 100 * valeur_venale * variable_redevance_domaniale
        # Comparaison avec le minimum
        montant_base = max_(arrondiSup(montant_intermediaire), montant_minimum)

        return where(type_calcul == '9', montant_base, 0)


class montant_total_redevance_domaniale_type_9(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant total de la redevance domaniale dûe sur le domaine privé"
    reference = "Arrêté NOR DAF2120267AC-3"
    unit = 'currency-XPF'

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '9', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'priv_09_autres')
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)

        montant_base = personne('montant_base_redevance_domaniale_type_9', period)

        # Parameters
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        montant_minimum = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].montant_minimum

        # Calcul du montant total
        montant_intermediaire = max_(montant_base * duree_occupation_redevance_domaniale_jour / base_calcul_jour, montant_minimum)
        montant_total = arrondiSup(montant_intermediaire)
        return where(type_calcul == '9', montant_total, 0)


class temporalite_redevance_domaniale_type_9(Variable):
    value_type = str
    entity = Personne
    definition_period = DAY
    label = "Temporalité (journalier, annuel, mensuel) pour la redevance domaniale"
    reference = "Arrêté NOR DAF2120267AC-3"

    def formula(personne, period, parameters):
        # Variables
        type_calcul = personne('type_calcul_redevance_domaniale', period)
        # Lors de demandes multiples avec des types de calculs différents, il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        nature_emprise_occupation_redevance_domaniale = where(type_calcul == '9', nature_emprise_occupation_redevance_domaniale.decode_to_str(), 'priv_09_autres')
        # Parametres
        base_calcul_jour = parameters(period).daf.redevance_domaniale.type_9[nature_emprise_occupation_redevance_domaniale].base_calcul_jour
        # Constantes
        nombre_jour_par_an = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_an_rd
        nombre_jour_par_mois = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_mois_rd
        nombre_jour_par_semaine = parameters(period).daf.redevance_domaniale.constantes.nombre_jour_par_semaine_rd
        # Transformation
        temporalite = select([
            base_calcul_jour == 1,
            base_calcul_jour == nombre_jour_par_semaine,
            base_calcul_jour == nombre_jour_par_mois,
            base_calcul_jour == nombre_jour_par_an
            ], [
                Temporalite.Journalier,
                Temporalite.Hebdomadaire,
                Temporalite.Mensuel,
                Temporalite.Annuel
                ])

        return where(type_calcul == '9', temporalite, Temporalite.Non_Applicable)
