# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class nombre_tranches_it_ventes(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    label = u"Nombre de tranches applicables sur l'IT des ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nSa modification n'est possible que pour les simulations, et dans ce cas seule la première valeur de la simulation sera prise en compte. A modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        return len(parameters(period).dicp.it.taux_ventes.rates)


class taux_it_ventes_tranche_1(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 1 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 0
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_2(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 2 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 1
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_3(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 3 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 2
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_4(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 4 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 3
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_5(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 5 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 4
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_6(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 6 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 5
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_7(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 7 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 6
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_8(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 8 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 7
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_9(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 9 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 8
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_10(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 10 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 9
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_11(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 11 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 10
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)


class taux_it_ventes_tranche_12(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    label = u"Taux de tranche 12 de l'IT sur les ventes\n\nAttention, ce paramètre ne DOIT PAS être modifié pour un calcul.\nD'autre part s'il est modifié dans une simulation pour une pays, il faut le définir pour toutes les payss, sinon sa valeur sera de 0.\nEnfin, sa modification n'est souhaitable que pour les simulations\nA modifier avec une extrème précaution !"
    reference = ["https://www.impot-polynesie.gov.pf/code/40-section-iv-calcul-de-limpot", "https://www.impot-polynesie.gov.pf/sites/default/files/2018-03/20180315%20CDI%20v%20num%20SGG-DICP.pdf#page=47"]  # Always use the most official source

    def formula(pays, period, parameters):
        nombre_tranches_it_ventes = pays(f'nombre_tranches_it_ventes', period)
        tranche = 11
        rate = parameters(period).dicp.it.taux_ventes.rates[tranche] if len(parameters(period).dicp.it.taux_ventes.rates) > tranche else 0
        return where(nombre_tranches_it_ventes > tranche, rate, 0)
