from openfisca_pf.base import ndarray, rint, nextafter


__all__ = [
    'arrondi_inferieur',
    'arrondi_superieur'
    ]


def arrondi_inferieur(valeur: ndarray) -> ndarray:
    """
    Arrondi a l'entier inférieur la value donnée en entrée. Par exemple `1.5` est arrondit à `1`, et `1.6` to `2`.

    :param valeur: Valeur ou vecteur de valeur à arrondir.
    :return:       Valeur ou vecteur de valeurs arrondis à l'entier inférieur.
    """
    return rint(nextafter(valeur, valeur - 1))


def arrondi_superieur(valeur: ndarray) -> ndarray:
    """
    Arrondi a l'entier supérieur la value donnée en entrée. Par exemple `1.4` est arrondit à `1`, et `1.5` to `2`.

    :param valeur: Valeur ou vecteur de valeur à arrondir.
    :return:       Valeur ou vecteur de valeurs arrondis à l'entier supérieur.
    """
    return rint(nextafter(valeur, valeur + 1))


def arrondi_millier_inferieur(value):
    return (value // 1000) * 1000
