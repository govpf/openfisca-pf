# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class montant_du_cstns_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 1 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_1 = #montant_cstns_prestations_du_tranche_1 + #montant_cstns_ventes_du_tranche_1"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 1
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 2 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_2 = #montant_cstns_prestations_du_tranche_2 + #montant_cstns_ventes_du_tranche_2"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 2
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 3 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_3 = #montant_cstns_prestations_du_tranche_3 + #montant_cstns_ventes_du_tranche_3"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 3
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 4 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_4 = #montant_cstns_prestations_du_tranche_4 + #montant_cstns_ventes_du_tranche_4"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 4
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 5 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_5 = #montant_cstns_prestations_du_tranche_5 + #montant_cstns_ventes_du_tranche_5"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 5
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 6 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_6 = #montant_cstns_prestations_du_tranche_6 + #montant_cstns_ventes_du_tranche_6"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 6
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 7 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_7 = #montant_cstns_prestations_du_tranche_7 + #montant_cstns_ventes_du_tranche_7"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 7
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 8 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_8 = #montant_cstns_prestations_du_tranche_8 + #montant_cstns_ventes_du_tranche_8"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 8
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 9 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_9 = #montant_cstns_prestations_du_tranche_9 + #montant_cstns_ventes_du_tranche_9"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 9
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 10 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_10 = #montant_cstns_prestations_du_tranche_10 + #montant_cstns_ventes_du_tranche_10"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 10
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 11 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_11 = #montant_cstns_prestations_du_tranche_11 + #montant_cstns_ventes_du_tranche_11"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 11
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche


class montant_du_cstns_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS sur la tranche 12 sans tenir compte de l'abattement de droits : \n\n#montant_du_cstns_tranche_12 = #montant_cstns_prestations_du_tranche_12 + #montant_cstns_ventes_du_tranche_12"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 12
        cstns_prestations_tranche = entreprise(f'montant_cstns_prestations_du_tranche_{tranche}', period)
        cstns_ventes_tranche = entreprise(f'montant_cstns_ventes_du_tranche_{tranche}', period)
        return cstns_prestations_tranche + cstns_ventes_tranche
