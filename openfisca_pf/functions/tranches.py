# -*- coding: utf-8 -*-


__all__ = [
    'calculer_base_imposable_ventes_tranche',
    'calculer_base_imposable_prestations_tranche',
    'creer_bareme'
    ]


from openfisca_core.taxscales import MarginalRateTaxScale
from openfisca_pf.base import (
    ArrayLike,
    Parameters,
    Period,
    select
    )
from openfisca_pf.entities import Pays, Personne


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
        return select(
            [assiette <= seuil_tranche_inferieure, seuil_tranche_inferieure < assiette],
            [0, assiette - seuil_tranche_inferieure],
            )

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
        return select(
            [assiette <= seuil_tranche_inferieure, assiette > seuil_tranche_inferieure],
            [0, assiette - seuil_tranche_inferieure - base_totale],
            )

    # Sinon on est soit avant le seuil, soit avant le prochain seuil, ou alors après le prochain seuil
    else:
        base_totale = personne(f'base_imposable_{impot}_ventes_tranche_{tranche}', period, parameters) / 4
        seuil_tranche_superieure = personne.pays(f'seuil_{impot}_prestations_tranche_{tranche + 1}', period, parameters)
        return select(
            [assiette <= seuil_tranche_inferieure, assiette < seuil_tranche_superieure, assiette >= seuil_tranche_superieure],
            [0, assiette - seuil_tranche_inferieure - base_totale, seuil_tranche_superieure - seuil_tranche_inferieure - base_totale],
            )


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
