# -*- coding: utf-8 -*-

__all__ = [
    # datetime
    "date",
    # numpy
    "asarray",
    "ceil",
    "floor",
    "isin",
    "max_",
    "min_",
    "not_",
    "round_",
    "select",
    "where",
    # numpy.typing
    "ArrayLike",
    # openfisca_core.holders
    "set_input_dispatch_by_period",
    "set_input_divide_by_period",
    # openfisca_core.indexed_enums
    "Enum",
    # openfisca_core.periods
    "ETERNITY",
    "Period",
    "YEAR",
    "MONTH",
    "DAY",
    "period",
    # openfisca_core.types
    "Parameters",
    # openfisca_core.variables
    "Variable",
    # enums
    "OuiNon",
    "RegimeCPS",
    "TypeContrat",
    "TypePersonne",
    "TypeSociete",
    # functions
    "aggreger_variables",
    "arrondi_inferrieur",
    "arrondi_superrieur",
    "calculer_base_imposable_ventes_tranche",
    "calculer_base_imposable_prestations_tranche",
    "creer_bareme"
    ]

from datetime import date
from numpy import (
    array,
    asarray,
    ceil,
    floor,
    isin,
    logical_not as not_,
    maximum as max_,
    minimum as min_,
    nextafter,
    rint,
    round as round_,
    select,
    where
    )
from typing import List
from numpy.typing import ArrayLike
from openfisca_core.holders import (
    set_input_dispatch_by_period,
    set_input_divide_by_period
    )
from openfisca_core.indexed_enums import Enum
from openfisca_core.periods import Period, YEAR, MONTH, DAY, ETERNITY, period
from openfisca_core.taxscales import MarginalRateTaxScale
from openfisca_core.types import Entity, Params as Parameters
from openfisca_core.variables import Variable
from openfisca_pf.entities import Pays, Personne


class OuiNon(Enum):
    """
    Oui ou non
    """
    O = "Oui"
    N = "Non"


class RegimeCPS(Enum):
    """
    Différents regimes d'affiliation à la contribution pour la santée.
    """
    NonAffilie = "La personne n'est pas affiliée"
    RSPF = "Régime de solidarité"
    RNS = "Régime des non salariés"
    RS = "Régime des salariés"


class TypeContrat(Enum):
    """
    Différents contrat de travails.
    """
    Aucun = "Aucun contrat"
    CDI = "Contrat à durée indéterminée"
    CDD = "Contrat à durée déterminée"
    Extras = "Contrat d'extras"


class TypePersonne(Enum):
    """
    Types de personnes: physique ou morale.
    """
    P = "Personne physique"
    M = "Personne morale"


class TypeSociete(Enum):
    """
    Différents types de sociétées.
    """
    EI = "Entreprise Individuelle"
    EURL = "Entreprise Unipersonnelle à Responsabilité Limitée"
    SARL = "Société à Responsabilité Limitée"
    SNC = "Société en Nom Collectif"
    SA = "Société Anonyme"
    SAS = "Société par Action Simplifiée"
    SCI = "Société Civile Immobilière"


def aggreger_variables(entitee: Entity, period: Period, prefix: str, variables: List[str]) -> ArrayLike:
    """
    Calcule et aggrège les valeurs des variables demandés dans un vecteur.
    Par exemple étant donné les variables `['x', 'y', 'z']`, le préfix `'a_'` la fonction calcule `[entitee('a_x', period)[0], entitee('a_y', period)[1], entitee('a_z', period)[2]]`

    :param entitee:   Entitée sur laquelle réaliser l'aggrégation des variables.
    :param period:    Periode durant laquelle réaliser les calculs.
    :param prefix:    Prefix à ajouter devant les noms des variables.
    :param variables: Noms des variables à aggréger.
    :return:          Vecteur contenant les valeurs aggrégées des variables.
    """
    result = []
    index = 0
    for identifiant in variables:
        value = entitee(prefix + identifiant, period)[index]
        result.append(value)
        index = index + 1
    return array(result)


def arrondi_inferrieur(valeur: ArrayLike) -> ArrayLike:
    """
    Arrondi a l'entier inférieur la value donnée en entrée. Par exemple `1.5` est arrondit à `1`, et `1.6` to `2`.

    :param valeur: Valeur ou vecteur de valeur à arrondir.
    :return:       Valeur ou vecteur de valeurs arrondis à l'entier inférieur.
    """
    return rint(nextafter(valeur, valeur - 1))


def arrondi_superrieur(valeur: ArrayLike) -> ArrayLike:
    """
    Arrondi a l'entier supérieur la value donnée en entrée. Par exemple `1.4` est arrondit à `1`, et `1.5` to `2`.

    :param valeur: Valeur ou vecteur de valeur à arrondir.
    :return:       Valeur ou vecteur de valeurs arrondis à l'entier supérieur.
    """
    return rint(nextafter(valeur, valeur + 1))


def calculer_base_imposable_ventes_tranche(personne: Personne, period: Period, parameters: Parameters, tranche: int, impot: str) -> ArrayLike:
    """
    Calcule le montant de la base imposable des ventes pour la tranche donnée.

    :param personne:   Personne pour laquelle on souhaite calculer le montant de la base imposable.
    :param period:     Period durant laquelle on souhaite réaliser les calculs.
    :param parameters: Parametres utilisés pour réaliser les calculs.
    :param tranche:    Tranche pour laquelle on souhaite calculer la base.
    :param impot:      Type de l'impot que l'on souhaite calculer.
    :return:           Montant de la base imposable sur les ventes pour la tranche donnée.
    """
    # On recupère le nombre de tranche pour cet impot et le type ventes.
    nombre_de_tranches = personne.pays(f'nombre_tranches_{impot}_ventes', period, parameters)[0]

    # Si la tanche est supérieur au nombre de tranche,
    # ce qui ne devrait pas se produire,
    # on retourne zero.
    if tranche > nombre_de_tranches:
        return 0

    # On recupère le seuil de la tranche
    seuil_tranche_inferieure = personne.pays(f'seuil_{impot}_ventes_tranche_{tranche}', period, parameters)

    # On recupère l'assiette (les ventes)
    assiette = personne(f'base_imposable_{impot}_ventes', period, parameters)

    # Si il s'agit de la dernière tranche on est soit avant le seuil de la tranche, soit au dela
    if tranche == nombre_de_tranches:
        return (select(
            [assiette <= seuil_tranche_inferieure, seuil_tranche_inferieure < assiette],
            [0, assiette - seuil_tranche_inferieure],
            ))

    # Sinon on est soit avant le seuil, soit avant le prochain seuil, ou alors après le prochain seuil
    else:
        seuil_tranche_superieure = personne.pays(f'seuil_{impot}_ventes_tranche_{tranche + 1}', period, parameters)
        return select(
            [assiette <= seuil_tranche_inferieure, assiette < seuil_tranche_superieure, seuil_tranche_superieure <= assiette],
            [0, assiette - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
            )


def calculer_base_imposable_prestations_tranche(personne: Personne, period: Period, parameters: Parameters, tranche: int, impot: str) -> ArrayLike:
    """
    Calcule le montant de la base imposable de l'impôt sur les transactions de prestations pour la tranche donnée.

    :param personne:   Personne pour laquelle on souhaite calculer le montant de la base imposable.
    :param period:     Period durant laquelle on souhaite réaliser les calculs.
    :param parameters: Parametres utilisés pour réaliser les calculs.
    :param tranche:    Tranche pour laquelle on souhaite calculer la base.
    :param impot:      Type de l'impot que l'on souhaite calculer.
    :return:           Montant de la base imposable sur les prestations pour la tranche donnée.
    """
    # On recupère le nombre de tranche pour cet impot et le type prestations.
    nombre_de_tranches = personne.pays(f'nombre_tranches_{impot}_prestations', period)[0]

    # Si la tanche est supérieur au nombre de tranche,
    # ce qui ne devrait pas se produire,
    # on retourne zero.
    if tranche > nombre_de_tranches:
        return 0

    # On recupère le seuil de la tranche
    seuil_tranche_inferieure = personne.pays(f'seuil_{impot}_prestations_tranche_{tranche}', period, parameters)

    # On recupère l'assiette (les prestations)
    assiette = personne(f'base_imposable_{impot}_prestations', period, parameters) + personne(f'base_imposable_{impot}_ventes', period, parameters) / 4

    # Si il s'agit de la dernière tranche on est soit avant le seuil de la tranche, soit au dela
    if tranche == nombre_de_tranches:
        base_totale = 0
        for i in range(tranche, personne.pays(f'nombre_tranches_{impot}_ventes', period, parameters)[0] + 1):
            base_totale += personne(f'base_imposable_{impot}_ventes_tranche_{i}', period, parameters) / 4
        return (select(
            [assiette <= seuil_tranche_inferieure, assiette > seuil_tranche_inferieure],
            [0, assiette - seuil_tranche_inferieure - base_totale],
            ))

    # Sinon on est soit avant le seuil, soit avant le prochain seuil, ou alors après le prochain seuil
    else:
        base_totale = personne(f'base_imposable_{impot}_ventes_tranche_{tranche}', period, parameters) / 4
        seuil_tranche_superieure = personne.pays(f'seuil_{impot}_prestations_tranche_{tranche + 1}', period, parameters)
        return (select(
            [assiette <= seuil_tranche_inferieure, assiette < seuil_tranche_superieure, assiette >= seuil_tranche_superieure],
            [0, assiette - seuil_tranche_inferieure - base_totale, seuil_tranche_superieure - seuil_tranche_inferieure - base_totale],
            ))


def creer_bareme(pays: Pays, period: Period, parameters: Parameters, impot: str, type: str, nom: str = "barème") -> MarginalRateTaxScale:
    """
    Créer un barème pour un impot calculé en plusieurs tranche.
    Une variable définissant le nombre de tranche doit exister dans le `Pays` et suivre la convention de nommage `nombre_tranches_[impot]_[type]`.
    Pour chaque tranche du barème deux variables doivent exister dans le `Pays`.
    La première qui défini le seuil pour la tranche doit suivre la convention de nommage `seuil_[impot]_[type]_tranche_[tranche]`.
    La deuxième  qui défini le taux pour la tranche doit suivre la convenstion de nommage `taux_[impot]_[type]_tranche_[tranche]`.

    :param pays:       Pays pour lequel sont définies les règles de calculs du barème.
    :param period:     Period durant laquelle le barème sera calculé.
    :param parameters: Parametres utilisés lors des calculs du barème.
    :param impot:      Code de l'impot.
    :param type:       Type de l'impot.
    :param nom:        Nom du barème.
    :return:           Le nouveau barème.
    """
    # Calculations are grouped per date, so we know the parameters for each entry is the same, thus we can create only one scale for all of them
    nombre_de_tranches = pays(f'nombre_tranches_{impot}_{type}', period, parameters)[0]
    bareme = MarginalRateTaxScale(nom)
    for tranche in range(1, nombre_de_tranches + 1):
        bareme.add_bracket(
            pays(f'seuil_{impot}_{type}_tranche_{tranche}', period, parameters)[0],
            pays(f'taux_{impot}_{type}_tranche_{tranche}', period, parameters)[0]
            )
    return bareme
