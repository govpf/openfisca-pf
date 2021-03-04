# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class montant_du_it_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 1 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_1 = #montant_it_prestations_du_tranche_1 + #montant_it_ventes_du_tranche_1"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 2 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_2 = #montant_it_prestations_du_tranche_2 + #montant_it_ventes_du_tranche_2"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 3 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_3 = #montant_it_prestations_du_tranche_3 + #montant_it_ventes_du_tranche_3"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 4 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_4 = #montant_it_prestations_du_tranche_4 + #montant_it_ventes_du_tranche_4"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 5 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_5 = #montant_it_prestations_du_tranche_5 + #montant_it_ventes_du_tranche_5"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 6 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_6 = #montant_it_prestations_du_tranche_6 + #montant_it_ventes_du_tranche_6"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 6
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 7 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_7 = #montant_it_prestations_du_tranche_7 + #montant_it_ventes_du_tranche_7"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 7
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 8 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_8 = #montant_it_prestations_du_tranche_8 + #montant_it_ventes_du_tranche_8"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 8
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 9 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_9 = #montant_it_prestations_du_tranche_9 + #montant_it_ventes_du_tranche_9"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 9
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 10 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_10 = #montant_it_prestations_du_tranche_10 + #montant_it_ventes_du_tranche_10"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 10
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 11 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_11 = #montant_it_prestations_du_tranche_11 + #montant_it_ventes_du_tranche_11"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 11
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche


class montant_du_it_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 12 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_12 = #montant_it_prestations_du_tranche_12 + #montant_it_ventes_du_tranche_12"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 12
        it_prestations_tranche = entreprise(f'montant_it_prestations_du_tranche_{tranche}', period)
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_prestations_tranche + it_ventes_tranche
