# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies the same computation as type_1,
# but the parameters depends on a area.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

from numpy import datetime64, timedelta64
from openfisca_pf.variables.daf.redevance_domaniale.enums import *
from openfisca_pf.base import *


class date_fin_redevance_domaniale(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Date de fin de l'occupation"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        date_validation_redevance_domaniale_echeancier = personne('date_validation_redevance_domaniale_echeancier',period)

        date_deb_redevance = numpy.datetime64(date_validation_redevance_domaniale_echeancier) - 1


        date_fin = select([unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
                                    unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
                                    unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
                                    [ date_deb_redevance.replace(year = date_deb_redevance.year + duree_occupation_redevance_domaniale),
                                     date_deb_redevance.replace(year = date_deb_redevance.year + (date_deb_redevance.month + duree_occupation_redevance_domaniale) // 12, ## incrémentation de l'année quand la somme du mois du début et de la durée ajouté dépasse l'année
                                                                            month = (date_deb_redevance.month + duree_occupation_redevance_domaniale) % 12),
                                    date_deb_redevance + duree_occupation_redevance_domaniale,
                                    ])
        
        date_fin = numpy.array(date_fin)

        return date_fin


class duree_effective_occupation_redevance_domaniale_jour(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée d'occupation en jour"

    def formula(personne, period, parameters):
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        date_validation_redevance_domaniale_echeancier = personne('date_validation_redevance_domaniale_echeancier',period)

        date_deb_redevance = numpy.array(date_validation_redevance_domaniale_echeancier, dtype='datetime64') - 1
        print(date_deb_redevance.dtype)
        date_fin_redevance = select([unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
                                    unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
                                    unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
                                    [date_deb_redevance + numpy.array(1, dtype='timedelta64[Y]'),
                                    date_deb_redevance + numpy.array(duree_occupation_redevance_domaniale, dtype='timedelta64[M]'),
                                    date_deb_redevance + numpy.array(duree_occupation_redevance_domaniale, dtype='timedelta64[D]'),
                                    ])
        
        duree = date_fin_redevance - date_deb_redevance
        
        return duree.astype('timedelta64[D]').astype(int)

class duree_facturee_redevance_domaniale_jour(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "La durée de facturation. Pour des durées inférieure à 30 jours, le durée calendaire est utilisées. Pour des durées supérieurs, la durée est calcul pour être ramené à des mois sur 30 jours et donc des années de 360 jours)"

    def formula(personne, period, parameters):
        ##Déclaration des variables
        duree_occupation_redevance_domaniale = personne('duree_occupation_redevance_domaniale', period)
        unite_duree_occupation_redevance_domaniale = personne('unite_duree_occupation_redevance_domaniale', period)
        date_validation_redevance_domaniale_echeancier = personne('date_validation_redevance_domaniale_echeancier', period)
        
        date_deb_redevance = numpy.array(date_validation_redevance_domaniale_echeancier, dtype='datetime64') - 1
        date_fin_redevance = select([unite_duree_occupation_redevance_domaniale == UnitesDuree.Annees,
                                    unite_duree_occupation_redevance_domaniale == UnitesDuree.Mois,
                                    unite_duree_occupation_redevance_domaniale == UnitesDuree.Jours],
                                    [date_deb_redevance + numpy.array(duree_occupation_redevance_domaniale, dtype='timedelta64[Y]'),
                                    date_deb_redevance + numpy.array(duree_occupation_redevance_domaniale, dtype='timedelta64[M]'),
                                    date_deb_redevance + numpy.array(duree_occupation_redevance_domaniale, dtype='timedelta64[D]'),
                                    ])
        
        ##Conversion des jours pour ramener à des mois de 30 jours
        ##Il faut ramener à 30, les jours en 31 ou alors pour février ceux du 28 et du 29.
        date_calcul_deb = where(date_deb_redevance.day==31 + date_deb_redevance.month==2 * (date_deb_redevance.day==28 + date_deb_redevance.day==29),
                                date_deb_redevance.replace(day=30),
                                date_deb_redevance)
        date_calcul_fin = where(date_fin_redevance.day==31 + date_fin_redevance.month==2 * (date_fin_redevance.day==28 + date_fin_redevance.day==29),
                                date_deb_redevance.replace(day=30),
                                date_fin_redevance)
        end_year = date_calcul_fin.astype('datetime64[Y]').astype(int)
        end_month = date_calcul_fin.astype('datetime64[M]').astype(int)
        end_day = date_calcul_fin.astype('datetime64[D]').astype(int)
        
        beg_year = date_calcul_deb.astype('datetime64[Y]').astype(int)
        beg_month = date_calcul_deb.astype('datetime64[M]').astype(int)
        beg_day = date_calcul_deb.astype('datetime64[D]').astype(int)
        
        duree = (end_year-beg_year) * 360 +(end_month-beg_month) * 30 + (end_day-beg_day)

        return duree