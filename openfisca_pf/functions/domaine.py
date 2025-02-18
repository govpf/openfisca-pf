from openfisca_pf.base import array, ArrayLike, EnumArray, ndarray, Parameter, where


def figer_emprise(mask: ndarray, emprise: EnumArray, default: str) -> ndarray:
    """
    Lors de demandes multiples avec des types de calculs différents,
    il est nécessaire de figer l'emprise sur une donnée existante pour le type associé.

    :param mask: Masque binaire contenant des 1 et des 0
    :param emprise: Array de valeur d'emprise dont les valeurs seront utilisé là ou le masque est égale à 1.
    :param default: Emprise attendu là ou le masque est egale 0
    :return: Array de valeurs d'emprise sous forme de texte.
    """
    return where(
        mask,
        emprise.decode_to_str(),
        default
        )


def indexer_zone_commune(parameter: Parameter, commune: EnumArray, zone: EnumArray, valeur: str) -> ArrayLike:
    """
    Index le parametre donnée avec le nom de la commune, puis avec le nom de la zone et enfin avec la valeur souhaitée.

    :param parameter: Paramètre à indexer
    :param commune: Commune
    :param zone: Zone
    :param valeur: Valeur à récupérer.
    :return: Valeur du paramètre dans la commune et dans la zone.
    """
    communes = commune.decode()
    zones = zone.decode()
    values = []
    for i in range(len(communes)):
        nom_commune = communes[i].name
        nom_zone = zones[i].name
        valeur_venale = parameter[nom_commune][nom_zone][valeur]
        values.append(valeur_venale)
    return array(values)
