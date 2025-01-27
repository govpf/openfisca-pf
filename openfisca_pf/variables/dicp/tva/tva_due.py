# -*- coding: utf-8 -*-

from openfisca_pf.constants import units
from openfisca_pf.entities import *
from openfisca_pf.base import *


class tva_due_taux_reduit(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux réduit: \n\n#tva_due_taux_reduit = #base_imposable_tva_taux_reduit * #taux_tva_reduit"
    set_input = set_input_dispatch_by_period
    unit = units.XPF

    def formula(personne, period, parameters):
        base_imposable = personne('base_imposable_tva_taux_reduit', period)
        taux = personne.pays('taux_tva_reduit', period)
        return arrondiSup(base_imposable * taux)


class tva_due_taux_intermediaire(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux intermédiaire"
    set_input = set_input_dispatch_by_period
    unit = units.XPF

    def formula(personne, period, parameters):
        base_imposable = personne('base_imposable_tva_taux_intermediaire', period)
        taux = personne.pays('taux_tva_intermediaire', period)
        return arrondiSup(base_imposable * taux)


class tva_due_taux_normal(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux normal"
    set_input = set_input_dispatch_by_period
    unit = units.XPF

    def formula(personne, period, parameters):
        base_imposable = personne('base_imposable_tva_taux_normal', period)
        taux = personne.pays('taux_tva_normal', period)
        return arrondiSup(base_imposable * taux)


class tva_due_taux_livraisons_immeubles_et_cession_parts(Variable):
    value_type = float
    entity = Personne
    definition_period = MONTH
    label = u"Montant de TVA dûe au taux livraisons d'immeubles et cession de parts"
    set_input = set_input_dispatch_by_period
    unit = units.XPF

    def formula(personne, period, parameters):
        base_imposable = personne('base_imposable_tva_taux_livraisons_immeubles_et_cession_parts', period)
        taux = personne.pays('taux_tva_livraisons_immeubles_et_cession_parts', period)
        return arrondiSup(base_imposable * taux)
