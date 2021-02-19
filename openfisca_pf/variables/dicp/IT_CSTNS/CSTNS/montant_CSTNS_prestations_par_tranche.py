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
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 1 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_1 = arrondiInf(#base_imposable_cstns_prestations_tranche_1 * #taux_cstns_prestations_tranche_1)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 1
        ca = entreprise(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_2(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 2 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_2 = arrondiInf(#base_imposable_cstns_prestations_tranche_2 * #taux_cstns_prestations_tranche_2)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 2
        ca = entreprise(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_3(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 3 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_3 = arrondiInf(#base_imposable_cstns_prestations_tranche_3 * #taux_cstns_prestations_tranche_3)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 3
        ca = entreprise(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_4(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 4 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_4 = arrondiInf(#base_imposable_cstns_prestations_tranche_4 * #taux_cstns_prestations_tranche_4)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 4
        ca = entreprise(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_5(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 5 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_5 = arrondiInf(#base_imposable_cstns_prestations_tranche_5 * #taux_cstns_prestations_tranche_5)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 5
        ca = entreprise(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)


class montant_cstns_prestations_du_tranche_6(Variable):
    value_type = float
    entity = Entreprise
    definition_period = YEAR
    label = u"Montant de CST-NS de la tranche 6 sur les prestations sans tenir compte de l'abattement de droits :\n\n#montant_cstns_prestations_du_tranche_6 = arrondiInf(#base_imposable_cstns_prestations_tranche_6 * #taux_cstns_prestations_tranche_6)"
    reference = "https://www.impot-polynesie.gov.pf/code/section-ii-taux"

    def formula(entreprise, period, parameters):
        tranche = 6
        ca = entreprise(f'base_imposable_cstns_prestations_tranche_{tranche}', period)
        taux = entreprise.pays(f'taux_cstns_prestations_tranche_{tranche}', period)
        return arrondiInf(ca * taux)
