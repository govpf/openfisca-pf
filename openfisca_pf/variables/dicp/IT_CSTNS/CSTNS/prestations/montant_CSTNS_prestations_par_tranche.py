# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *


class montant_cstns_prestations_du_tranche_1(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 1 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_1 = arrondiInf(#base_imposable_cstns_prestations_tranche_1 * #taux_cstns_prestations_tranche_1)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 1
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_2(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 2 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_2 = arrondiInf(#base_imposable_cstns_prestations_tranche_2 * #taux_cstns_prestations_tranche_2)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 2
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_3(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 3 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_3 = arrondiInf(#base_imposable_cstns_prestations_tranche_3 * #taux_cstns_prestations_tranche_3)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 3
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_4(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 4 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_4 = arrondiInf(#base_imposable_cstns_prestations_tranche_4 * #taux_cstns_prestations_tranche_4)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 4
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_5(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 5 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_5 = arrondiInf(#base_imposable_cstns_prestations_tranche_5 * #taux_cstns_prestations_tranche_5)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 5
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_6(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 6 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_6 = arrondiInf(#base_imposable_cstns_prestations_tranche_6 * #taux_cstns_prestations_tranche_6)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 6
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_7(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 7 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_7 = arrondiInf(#base_imposable_cstns_prestations_tranche_7 * #taux_cstns_prestations_tranche_7)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 7
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_8(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 8 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_8 = arrondiInf(#base_imposable_cstns_prestations_tranche_8 * #taux_cstns_prestations_tranche_8)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 8
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_9(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 9 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_9 = arrondiInf(#base_imposable_cstns_prestations_tranche_9 * #taux_cstns_prestations_tranche_9)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 9
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_10(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 10 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_10 = arrondiInf(#base_imposable_cstns_prestations_tranche_10 * #taux_cstns_prestations_tranche_10)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 10
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_11(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 11 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_11 = arrondiInf(#base_imposable_cstns_prestations_tranche_11 * #taux_cstns_prestations_tranche_11)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 11
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_12(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 12 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_12 = arrondiInf(#base_imposable_cstns_prestations_tranche_12 * #taux_cstns_prestations_tranche_12)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(personne, period, parameters):
        tranche = 12
        ca = personne(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = personne.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)
