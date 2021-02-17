# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class montant_it_ventes_du_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 1 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_1 = arrondiInf(#base_imposable_it_ventes_tranche_1 * #taux_it_ventes_tranche_1)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_ventes_du_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 2 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_2 = arrondiInf(#base_imposable_it_ventes_tranche_2 * #taux_it_ventes_tranche_2)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_ventes_du_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 3 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_3 = arrondiInf(#base_imposable_it_ventes_tranche_3 * #taux_it_ventes_tranche_3)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_ventes_du_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 4 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_4 = arrondiInf(#base_imposable_it_ventes_tranche_4 * #taux_it_ventes_tranche_4)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_ventes_du_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 5 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_5 = arrondiInf(#base_imposable_it_ventes_tranche_5 * #taux_it_ventes_tranche_5)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_ventes_du_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 6 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_6 = arrondiInf(#base_imposable_it_ventes_tranche_6 * #taux_it_ventes_tranche_6)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 6
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_ventes_du_tranche_7(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 7 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_7 = arrondiInf(#base_imposable_it_ventes_tranche_7 * #taux_it_ventes_tranche_7)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 7
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_ventes_du_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 8 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_8 = arrondiInf(#base_imposable_it_ventes_tranche_8 * #taux_it_ventes_tranche_8)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 8
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_ventes_du_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 9 sur les ventes sans tenir compte de l'abattement de droits :\n\n#montant_it_ventes_du_tranche_9 = arrondiInf(#base_imposable_it_ventes_tranche_9 * #taux_it_ventes_tranche_9)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 9
        ca = entreprise(f'base_imposable_it_ventes_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_ventes_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_prestations_du_tranche_1(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 1 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_it_prestations_du_tranche_1 = arrondiInf(#base_imposable_it_prestations_tranche_1 * #taux_it_prestations_tranche_1)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 1
        ca = entreprise(f'base_imposable_it_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_prestations_du_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 2 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_it_prestations_du_tranche_2 = arrondiInf(#base_imposable_it_prestations_tranche_2 * #taux_it_prestations_tranche_2)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 2
        ca = entreprise(f'base_imposable_it_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_prestations_du_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 3 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_it_prestations_du_tranche_3 = arrondiInf(#base_imposable_it_prestations_tranche_3 * #taux_it_prestations_tranche_3)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 3
        ca = entreprise(f'base_imposable_it_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_prestations_du_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 4 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_it_prestations_du_tranche_4 = arrondiInf(#base_imposable_it_prestations_tranche_4 * #taux_it_prestations_tranche_4)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 4
        ca = entreprise(f'base_imposable_it_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_prestations_du_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 5 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_it_prestations_du_tranche_5 = arrondiInf(#base_imposable_it_prestations_tranche_5 * #taux_it_prestations_tranche_5)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 5
        ca = entreprise(f'base_imposable_it_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_it_prestations_du_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT de la tranche 6 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_it_prestations_du_tranche_6 = arrondiInf(#base_imposable_it_prestations_tranche_6 * #taux_it_prestations_tranche_6)"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 6
        ca = entreprise(f'base_imposable_it_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_it_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_du_it_tranche_1(Variable):
    value_type = float
    entity = Entreprise
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
    entity = Entreprise
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
    entity = Entreprise
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
    entity = Entreprise
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
    entity = Entreprise
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
    entity = Entreprise
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
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 7 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_7 = #montant_it_ventes_du_tranche_7"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 7
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_ventes_tranche


class montant_du_it_tranche_8(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 8 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_8 = #montant_it_ventes_du_tranche_8"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 8
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_ventes_tranche


class montant_du_it_tranche_9(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant d'IT sur la tranche 9 sans tenir compte de l'abattement de droits : \n\n#montant_du_it_tranche_9 = #montant_it_ventes_du_tranche_9"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(entreprise, period, parameters):
        tranche = 9
        it_ventes_tranche = entreprise(f'montant_it_ventes_du_tranche_{tranche}', period)
        return it_ventes_tranche
