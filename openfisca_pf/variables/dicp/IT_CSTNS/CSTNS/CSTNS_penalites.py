# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class montant_amendes_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant des amendes appliquées a l'avis CST NS"


class taux_majoration_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Taux de majoration appliqué a la CST NS"


class montant_majoration_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de la majoration appliquée a la CST NS"

    def formula(personne, period, parameters):
        taux_majoration_cstns = personne('taux_majoration_cstns', period)
        it_a_payer = personne('it_a_payer', period)
        return round_(it_a_payer * taux_majoration_cstns / 100)


class montant_penalites_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant des penalites appliquées a la CST NS"


class montant_total_penalites_cstns(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant total des penalités CST NS"

    def formula(personne, period, parameters):
        montant_amendes_cstns = personne('montant_amendes_cstns', period)
        montant_majoration_cstns = personne('montant_majoration_cstns', period)
        montant_penalites_cstns = personne('montant_penalites_cstns', period)
        return round_(montant_amendes_cstns + montant_majoration_cstns + montant_penalites_cstns)
