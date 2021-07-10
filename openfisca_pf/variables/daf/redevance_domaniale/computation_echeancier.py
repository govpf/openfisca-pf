# -*- coding: utf-8 -*-

# This file defines the computation for occupation on public domain that relies the same computation as type_1,
# but the parameters depends on a area.
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *

from numpy import datetime64, timedelta64
# from openfisca_core import periods


class montant_redevance_domaniale_echeancier_jour(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY

    def formula(personne, period, parameters):
        date_validation_redevance_domaniale = personne('date_validation_redevance_domaniale', period)
        epsilon = timedelta64(1)
        # How many days since start of redevance
        nombre_jours_depuis_signature = (datetime64(period.start) - date_validation_redevance_domaniale + epsilon).astype('timedelta64[D]').astype(int)
        # print(nombre_jours_depuis_signature)
        part_fixe = parameters(period).daf.redevance_domaniale.type_1.bati_cas_general.part_fixe
        part_unitaire = parameters(period).daf.redevance_domaniale.type_1.bati_cas_general.part_unitaire
        premier_jour = nombre_jours_depuis_signature == 1
        duree_occupation_redevance_domaniale_echeancier = personne('duree_occupation_redevance_domaniale_echeancier', period)
        redevance_du = (nombre_jours_depuis_signature > 0) * (nombre_jours_depuis_signature <= duree_occupation_redevance_domaniale_echeancier)
        return redevance_du * (premier_jour * part_fixe + part_unitaire)


class montant_redevance_domaniale_echeancier_annee(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR

    def formula(personne, period, parameters):
        total = personne('montant_redevance_domaniale_echeancier_jour', period, options = [ADD])
        return total
