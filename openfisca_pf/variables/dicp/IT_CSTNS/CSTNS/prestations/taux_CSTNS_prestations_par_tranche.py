# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class nombre_tranches_cstns_prestations(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre de tranches applicables sur la CST-NS des prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nSa modification n'est possible que pour les simulations, et dans ce cas seule la première valeur de la simulation sera prise en compte. A modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return len(parameters(period).dicp.cst_ns.taux_prestations.rates)


class taux_cstns_prestations_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 1 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[0] if nombre_tranches_cstns_prestations > 0 else 0)


class taux_cstns_prestations_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 2 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[1] if nombre_tranches_cstns_prestations > 1 else 0)


class taux_cstns_prestations_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 3 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[2] if nombre_tranches_cstns_prestations > 2 else 0)


class taux_cstns_prestations_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 4 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[3] if nombre_tranches_cstns_prestations > 3 else 0)


class taux_cstns_prestations_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 5 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[4] if nombre_tranches_cstns_prestations > 4 else 0)


class taux_cstns_prestations_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 6 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[5] if nombre_tranches_cstns_prestations > 5 else 0)


class taux_cstns_prestations_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 7 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[6] if nombre_tranches_cstns_prestations > 6 else 0)


class taux_cstns_prestations_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 8 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[7] if nombre_tranches_cstns_prestations > 7 else 0)


class taux_cstns_prestations_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 9 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[8] if nombre_tranches_cstns_prestations > 8 else 0)


class taux_cstns_prestations_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 10 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[9] if nombre_tranches_cstns_prestations > 9 else 0)


class taux_cstns_prestations_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 11 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[10] if nombre_tranches_cstns_prestations > 10 else 0)


class taux_cstns_prestations_tranche_12(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 12 de la CST-NS sur les prestations\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_cstns_prestations = pays(f'nombre_tranches_cstns_prestations', period)
        return (parameters(period).dicp.cst_ns.taux_prestations.rates[11] if nombre_tranches_cstns_prestations > 11 else 0)
