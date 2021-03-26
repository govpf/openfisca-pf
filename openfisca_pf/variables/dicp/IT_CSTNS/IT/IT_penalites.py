# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class montant_amendes_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant des amendes appliquées a l'avis IT"


class taux_majoration_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Taux de majoration appliqué a l'IT"


class montant_majoration_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de la majoration appliquée a l'IT"

    def formula(personne, period, parameters):
        taux_majoration_it = personne('taux_majoration_it', period)
        it_a_payer = personne('it_a_payer', period)
        return round_(it_a_payer * taux_majoration_it / 100)


class montant_penalites_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant des penalites appliquées a l'IT"


class montant_total_penalites_it(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant total des penalités IT"

    def formula(personne, period, parameters):
        montant_amendes_it = personne('montant_amendes_it', period)
        montant_majoration_it = personne('montant_majoration_it', period)
        montant_penalites_it = personne('montant_penalites_it', period)
        return round_(montant_amendes_it + montant_majoration_it + montant_penalites_it)
