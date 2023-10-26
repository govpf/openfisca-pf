# -*- coding: utf-8 -*-
import numpy

from openfisca_pf.entities import Personne
from openfisca_pf.base import Enum, YEAR, Variable
from openfisca_pf.enums import *


class commune(Variable):
    value_type = Enum
    possible_values = Commune
    entity = Personne
    definition_period = YEAR
    default_value = Commune.PAPEETE
    label = "Cammune a laquelle le local est rataché"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class archipel(Variable):
    value_type = Enum
    possible_values = Archipel
    entity = Personne
    definition_period = YEAR
    default_value = Archipel.ILES_SOUS_LE_VENT
    label = "Archipel auquel le local appartient"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        commune = local('commune', period, parameters)
        return numpy.select(
            [
                numpy.isin(commune, COMMUNES_DES_AUSTRALES),
                numpy.isin(commune, COMMUNES_DES_ILES_DU_VENT),
                numpy.isin(commune, COMMUNES_DES_ILES_SOUS_LE_VENT),
                numpy.isin(commune, COMMUNES_DES_MARQUISES),
                numpy.isin(commune, COMMUNES_DES_TUAMOTUS_ET_DES_GAMBIERS)
            ],
            [
                Archipel.AUSTRALES,
                Archipel.ILES_DU_VENT,
                Archipel.ILES_SOUS_LE_VENT,
                Archipel.MARQUISES,
                Archipel.TUAMOTUS_ET_GAMBIERS
            ]
        )


class logement_social(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est utilisé comme logement social, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class loue(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class meuble(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si le local est loué en meublé, False sinon."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class valeur_venale(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur vénale d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class loyer(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Loyer annuel d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"


class valeur_locative_loyers(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative calculer grace aux loyers d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        loyer = local('loyer', period, parameters)
        return loyer


class valeur_locative_direct(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative direct d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        logement_social = local('logement_social', period, parameters)
        archipel = local('archipel', period, parameters)
        valeur_venale = local('valeur_venale', period, parameters)
        taux_archipel = parameters(period).dicp.impot_foncier.taux_valeur_venal_direct[archipel]
        taux = numpy.where(logement_social, 0.02, taux_archipel)
        return taux * valeur_venale


class valeur_locative(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Valeur locative d'un local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        loue = local('loue', period, parameters)
        valeur_locative_loyers = local('valeur_locative_loyers', period, parameters)
        valeur_locative_direct = local('valeur_locative_direct', period, parameters)
        return numpy.where(loue, valeur_locative_loyers, valeur_locative_direct)


class base_imposition(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "base de l'impot foncier utilisé pour calculer la part du territoire et la part comunale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        loue = local('loue', period, parameters)
        meuble = local('meuble', period, parameters)
        valeur_locative = local('valeur_locative', period, parameters)
        tmp = 0.75 * valeur_locative
        return numpy.where(
            loue,
            numpy.where(meuble, 0.70, 0.75) * tmp,
            tmp
        )


class contribution_fonciere_pays(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'impot foncier allant au territoire"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        base_imposition = local('base_imposition', period, parameters)
        return 0.1 * base_imposition


class contribution_fonciere_commune(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant de l'impot foncier allant à la commune"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        commune = local('commune', period, parameters)
        taux = parameters(period).dicp.impot_foncier.taux_centime_additionnel_communal[commune]
        contribution_fonciere_pays = local('contribution_fonciere_pays', period, parameters)
        return taux * contribution_fonciere_pays


class contribution_fonciere(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Montant total de l'impot foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        contribution_fonciere_pays = local('contribution_fonciere_pays', period, parameters)
        contribution_fonciere_commune = local('contribution_fonciere_commune', period, parameters)
        return contribution_fonciere_pays + contribution_fonciere_commune