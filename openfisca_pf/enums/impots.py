# -*- coding: utf-8 -*-


from openfisca_pf.base import Enum


__all__ = [
    'FormeLegale',
    'RegimeCPS',
    'TypeContrat',
    'TypePersonne',
    'TypeSociete'
    ]


class FormeLegale(Enum):
    """
    Forme légale d'une personne
    """
    # TODO CLEAN THIS ENUM IN PAREO-SPRING-LIB
    ADF = 'Association de fait (Personne morale)'
    ADM = 'Administration (Personne morale)'
    ASSO = 'Association (Personne morale)'
    CIE = 'Compagnie (Personne morale)'
    CONSULAT = 'Consulat (Personne morale)'
    COOP = 'Coopérative (Personne morale)'
    COPRO = 'Copropriété (Personne physique)'
    CRTS = 'Consorts (Personne morale)'
    EARL = 'Exploitation agricole à responsabilité limitée (Personne morale)'
    EGL = 'Église (Personne morale)'
    EPA = 'Établissement public à caractère administratif (Personne morale'
    EPCI = 'Établissement public de coopération intercommunale (Personne morale)'
    EPIC = 'Établissement public à caractère industriel et commercial (Personne morale)'
    EURL = 'Entreprise unipersonnelle à responsabilité limitée (Personne morale)'
    EPST = 'Établissement public à caractère scientifique et technologique (Personne morale)'
    GIE = 'Groupement d intérêt économique (Personne morale)'
    INC = 'Titre inconnu (Personne morale)'
    M = 'Monsieur (Personne physique)'
    MR = 'Mister (Personne physique)'
    ME = 'Maître (Personne physique)'
    MLE = 'Mademoiselle (Personne physique)'
    MME = 'Madame (Personne physique)'
    REPRIS = 'Titre issu de la reprise (Personne morale)'
    SA = 'Société anonyme (Personne morale)'
    SAEM = 'Société anonyme d économie mixte (Personne morale)'
    SAI = 'Société anonyme immobilière (Personne morale)'
    SARL = 'Société à responsabilité limitée (Personne morale)'
    SAS = 'Société par action simplifiée (Personne morale)'
    SASU = 'Société par action simplifiée à associé unique (Personne morale)'
    SC = 'Société civile (Personne morale)'
    SCA = 'Société civile agricole (Personne morale)'
    SCAQ = 'Société civile aquacole (Personne morale)'
    SCI = 'Société civile immobilière (Personne morale)'
    SELARL = 'Société d exercice liberal à responsabilité limitée (Personne morale)'
    SEP = 'Société en participation (Personne morale)'
    SCAC = 'Société en commandité par action (Personne morale)'
    SCCV = 'Société civile de construction et de vente (Personne morale)'
    SCF = 'Société créée de fait (Personne morale)'
    SCM = 'Société civile de moyens (Personne morale)'
    SCP = 'Société civile de participation (Personne morale)'
    SCPA = 'Société civile particulière (Personne morale)'
    SCPE = 'Société civile de pêche (Personne morale)'
    SCPR = 'Société civile professionelle (Personne morale)'
    SELFA = 'Société d exercice libérale à forme anonyme (Personne morale)'
    SOUSCRIPTEUR = 'Souscripteur (Personne morale)'
    SCS = 'Société en commandité simple (Personne morale)'
    SNC = 'Société en nom collectif (Personne morale)'
    SP = 'Société particulière (Personne morale)'
    SPL = 'Société publique locale (Personne morale)'
    SYND = 'Syndicat (Personne morale)'


class RegimeCPS(Enum):
    """
    Différents regimes d'affiliation à la contribution pour la santé.
    """
    NonAffilie = "La personne n'est pas affiliée"
    RSPF = "Régime de solidarité"
    RNS = "Régime des non salariés"
    RS = "Régime des salariés"


class TypeContrat(Enum):
    """
    Différents types de contrats de travails.
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
