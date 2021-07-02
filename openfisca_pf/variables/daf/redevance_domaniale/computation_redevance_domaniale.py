# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class duree_occupation_redevance_domaniale_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en année"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Heures],
            [duree_occupation_redevance_domaniale,
            duree_occupation_redevance_domaniale / 12,
            duree_occupation_redevance_domaniale / 360,
            duree_occupation_redevance_domaniale / (360 * 8)],
            )
        return value


class duree_occupation_redevance_domaniale_jour(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en jour"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
            [duree_occupation_redevance_domaniale*360,
            duree_occupation_redevance_domaniale*30,
            duree_occupation_redevance_domaniale],
            )
        return value


class duree_occupation_redevance_domaniale_mois(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en mois"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        value = select(
            [unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
            unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
            [duree_occupation_redevance_domaniale/12,
            duree_occupation_redevance_domaniale,
            duree_occupation_redevance_domaniale/30],
            )
        return value


class montant_redevance_domaniale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        type_calcul = int(parameters(period).daf.redevance_domaniale.type_calcul[nature_emprise_occupation_redevance_domaniale])
        return personne('montant_redevance_domaniale_type_' + str(type_calcul), period)


class montant_redevance_domaniale_type_1(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 1"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        surface_redevance_domaniale = personne('surface_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_unitaire
        part_surfacique = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_surfacique
        # montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].montant_minimum
        facteur_prorata = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].facteur_prorata

        return arrondiSup((part_fixe + part_unitaire * nombre_unite_redevance_domaniale + part_surfacique * surface_redevance_domaniale) * duree_occupation_redevance_domaniale_jour / facteur_prorata)


class montant_test_scale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        scale = parameters(period).daf.redevance_domaniale.type_3.test_scale
        return arrondiSup(scale.calc(duree_occupation_redevance_domaniale_jour))


# class montant_test_redevance_annuelle(Variable):
#     value_type = float
#     entity = Personne
#     definition_period = YEAR
#     label = "test pour calcul redevance annuelle"

#     def formula(personne, period, parameters):
#         nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
#         surface_redevance_domaniale = personne('surface_redevance_domaniale', period)
#         nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
#         duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
#         part_fixe = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_fixe
#         part_unitaire = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_unitaire
#         part_surfacique = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].part_surfacique
#         montant_minimum = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].montant_minimum
#         facteur_prorata = parameters(period).daf.redevance_domaniale.type_1[nature_emprise_occupation_redevance_domaniale].facteur_prorata

#         return max_(part_fixe + part_unitaire * nombre_unite_redevance_domaniale + part_surfacique * surface_redevance_domaniale , montant_minimum) * duree_occupation_redevance_domaniale_annee


class montant_redevance_domaniale_type_2(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 2"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        surface_redevance_domaniale = personne('surface_redevance_domaniale', period)
        nombre_unite_redevance_domaniale = personne('nombre_unite_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        zone_occupation_redevance_domaniale = personne('zone_occupation_redevance_domaniale', period)
        part_fixe = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_unitaire
        part_surfacique = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].part_surfacique
        # montant_minimum = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].montant_minimum
        facteur_prorata = parameters(period).daf.redevance_domaniale.type_2[nature_emprise_occupation_redevance_domaniale][zone_occupation_redevance_domaniale].facteur_prorata

        return arrondiInf((part_fixe + part_unitaire * nombre_unite_redevance_domaniale + part_surfacique * surface_redevance_domaniale) * duree_occupation_redevance_domaniale_jour / facteur_prorata)


class montant_redevance_domaniale_type_3(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 3"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        # init = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].init
        # threshold_1 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].threshold_1
        # rate_1 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].rate_1
        # threshold_2 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].threshold_2
        # rate_2 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].rate_2
        # threshold_3 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].threshold_3
        # rate_3 = parameters(period).daf.redevance_domaniale.type_3[nature_emprise_occupation_redevance_domaniale].rate_3
        
        # return arrondiSup(
        #     select( [duree_occupation_redevance_domaniale_jour < threshold_1,
        # duree_occupation_redevance_domaniale_jour <= threshold_2,
        # duree_occupation_redevance_domaniale_jour > threshold_2],
        # [ init ,
        # init + rate_1 * (duree_occupation_redevance_domaniale_jour - threshold_1),
        # init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (duree_occupation_redevance_domaniale_jour - threshold_2)]))
        return 3

class montant_redevance_domaniale_type_4(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Montant de la redevance domaniale dûe calcul type 4"

    def formula(personne, period, parameters):
        nature_emprise_occupation_redevance_domaniale = personne('nature_emprise_occupation_redevance_domaniale', period)
        duree_occupation_redevance_domaniale_jour = personne('duree_occupation_redevance_domaniale_jour', period)
        init = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale].init
        threshold_1 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale].threshold_1
        rate_1 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale].rate_1
        threshold_2 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale].threshold_2
        rate_2 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale].rate_2
        threshold_3 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale].threshold_3
        rate_3 = parameters(period).daf.redevance_domaniale.type_4[nature_emprise_occupation_redevance_domaniale].rate_3
        
        return arrondiSup(
            select( [duree_occupation_redevance_domaniale_jour < threshold_1,
        duree_occupation_redevance_domaniale_jour <= threshold_2,
        duree_occupation_redevance_domaniale_jour > threshold_2],
        [ init ,
        init + rate_1 * (duree_occupation_redevance_domaniale_jour - threshold_1),
        init + rate_1 * (threshold_2 - threshold_1) + rate_2 * (duree_occupation_redevance_domaniale_jour - threshold_2)]))

