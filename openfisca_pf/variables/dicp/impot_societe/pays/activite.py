from openfisca_pf.base import *
from openfisca_pf.entities import Pays
from openfisca_pf.enums.impot_societe.activite import *


# TODO demander au PO la reference
class taux_is_activite_normale_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = DAY
    default_value = 0.25
    label = "Taux permettant de calculer l'IS pour une activité normale"
    reference = "TODO"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_societe.taux.activite[ActiviteTauxIS.NORMALE.name]


# TODO demander au PO la reference
class taux_is_activite_societes_minieres_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = DAY
    default_value = 0.25
    label = "Taux permettant de calculer l'IS pour une activité de sociétés minières"
    reference = "TODO"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_societe.taux.activite[ActiviteTauxIS.SOCIETES_MINIERES.name]


# TODO demander au PO la reference
class taux_is_activite_etablissement_financiers_credit_bail_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = DAY
    default_value = 0.35
    label = "Taux permettant de calculer l'IS pour une activité d'établissement financiers et de crédit, sociétés de crédit-bail"
    reference = "TODO"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_societe.taux.activite[
            ActiviteTauxIS.ETABLISSEMENTS_FINANCIERS_CREDIT_BAIL.name]


# TODO demander au PO la reference
class taux_is_activite_energies_renouvelables_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = DAY
    default_value = 0.20
    label = "Taux permettant de calculer l'IS pour une activité d'énergies renouvelables"
    reference = "TODO"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_societe.taux.activite[ActiviteTauxIS.ENERGIES_RENOUVELABLES.name]


# TODO demander au PO la reference
class taux_is_activite_secteur_numerique_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = DAY
    default_value = 0.20
    label = "Taux permettant de calculer l'IS pour une activité du secteur numérique"
    reference = "TODO"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_societe.taux.activite[ActiviteTauxIS.SECTEUR_NUMERIQUE.name]


# TODO demander au PO la reference
class taux_is_activite_secteur_recherche_developpement_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = DAY
    default_value = 0.20
    label = "Taux permettant de calculer l'IS pour une activité du secteur recherche et développement"
    reference = "TODO"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_societe.taux.activite[ActiviteTauxIS.SECTEUR_RECHERCHE_DEVELOPPEMENT.name]


# TODO demander au PO la reference
class taux_is_activite_zone_revitalisation_zrae_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = DAY
    default_value = 0.15
    label = "Taux permettant de calculer l'IS pour une activité d'une zone de revitalisation des activités économiques (ZRAE)"
    reference = "TODO"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_societe.taux.activite[ActiviteTauxIS.ZONE_REVITALISATION_ZRAE.name]
