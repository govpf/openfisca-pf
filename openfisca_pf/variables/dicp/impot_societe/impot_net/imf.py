# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    DAY,
    isin,
    where,
    select,
    ParameterNode,
    Period,
    Population,
    Variable,
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impot_societe.activity import (
    Activite,
    ACTIVITE_REDUCTION_IMF,
    ACTIVITE_REDUCTION_TAUX_A_SAISIR_IMF
    )


class imf_net_possede_reduction(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    default_value = False
    label = "Activité possède une réduction IMF ?"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_REDUCTION_IMF)


class imf_net_reduction_taux_est_a_saisir(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Taux Reduction IMF doit être saisie"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period, parameters)
        return isin(activite_principale, ACTIVITE_REDUCTION_TAUX_A_SAISIR_IMF)


class imf_net_reduction_taux_saisie(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Net Reduction IMF Saisie"


class imf_net_reduction_taux(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux Net Reduction IMF"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        activite_principale = personne('is_activite_principale', period)
        possede_reduction = personne('imf_net_possede_reduction', period)
        reduction_taux_est_a_saisir = personne('imf_net_reduction_taux_est_a_saisir', period)
        reduction_saisie = personne('imf_net_reduction_taux_saisie', period)

        nombre_exercices = personne('is_nombre_exercices', period)
        nombre_exercices = where(nombre_exercices > 0, nombre_exercices, 999)

        # NotImplementedError returned by "parameters(period).dicp.impot_societe.taux.activite_exoneration_is[activite_principale]"
        activites_croisieres = parameters(period).dicp.impot_societe.taux.imf_reduction.ACTIVITES_CROISIERE
        concessions_minieres = parameters(period).dicp.impot_societe.taux.imf_reduction.CONCESSIONS_MINIERES
        membre_groupe_fiscal = parameters(period).dicp.impot_societe.taux.imf_reduction.MEMBRE_GROUPE_FISCAL
        gie = parameters(period).dicp.impot_societe.taux.imf_reduction.GIE
        scpr = parameters(period).dicp.impot_societe.taux.imf_reduction.SCPR
        scm = parameters(period).dicp.impot_societe.taux.imf_reduction.SCM
        obnl = parameters(period).dicp.impot_societe.taux.imf_reduction.OBNL

        reduction = select([
            activite_principale == Activite.ACTIVITES_CROISIERE,
            activite_principale == Activite.CONCESSIONS_MINIERES,
            activite_principale == Activite.MEMBRE_GROUPE_FISCAL,
            activite_principale == Activite.GIE,
            activite_principale == Activite.SCPR,
            activite_principale == Activite.SCM,
            activite_principale == Activite.OBNL,
            True
            ], [
            activites_croisieres.calc(nombre_exercices),
            concessions_minieres.calc(nombre_exercices),
            membre_groupe_fiscal.calc(nombre_exercices),
            gie.calc(nombre_exercices),
            scpr.calc(nombre_exercices),
            scm.calc(nombre_exercices),
            obnl.calc(nombre_exercices),
            0.0
            ])

        reduction = where(reduction_taux_est_a_saisir, reduction_saisie, reduction)
        reduction = where(possede_reduction, reduction, 0)

        return reduction
