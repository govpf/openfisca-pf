from openfisca_core.indexed_enums import Enum


__all__ = [
    'RegimeCPS',
    'TypeContrat',
    'TypePersonne',
    'TypeSociete'
    ]


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
    P = 'Personne physique'
    M = 'Personne morale'


class TypeSociete(Enum):
    """
    Différents types de sociétées.
    """
    EI = 'Entreprise Individuelle'
    EURL = 'Entreprise Unipersonnelle à Responsabilité Limitée'
    SARL = 'Société à Responsabilité Limitée'
    SNC = 'Société en Nom Collectif'
    SA = 'Société Anonyme'
    SAS = 'Société par Action Simplifiée'
    SCI = 'Société Civile Immobilière'
