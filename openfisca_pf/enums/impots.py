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
    Forme legale d'une personne
    """
    # TODO CLEAN THIS ENUM IN PAREO-SPRING-LIB

    ADF = 'ADF'
    """
    Association de fait (Personne morale)
    """

    ADM = 'ADM'
    """
    Administration (Personne morale)
    """

    ASSO = 'ASSO'
    """
    Association (Personne morale)
    """

    CIE = 'CIE'
    """
    Compagnie (Personne morale)
    """

    CONSULAT = '..'
    """
    Consulat (Personne morale)
    """

    COOP = 'COOP'
    """
    Coopérative (Personne morale)
    """

    COPRO = 'COPRO'
    """
    Copropriété (Personne physique)
    """

    CRTS = 'CRTS'
    """
    Consorts (Personne morale)
    """

    EARL = 'EARL'
    """
    Exploitation agricole à responsabilité limitée (Personne morale)
    """

    EGL = 'EGL'
    """
    Eglise (Personne morale)
    """

    EPA = 'EPA'
    """
    Etablissement public à caractère administratif (Personne morale)
    """

    EPCI = 'EPCI'
    """
    Établissement public de coopération intercommunale (Personne morale)
    """

    EPIC = 'EPIC'
    """
    Etablissement public à caractère industriel et cormmercial (Personne morale)
    """

    EURL = 'EURL'
    """
    Entreprise unipersonnelle à responsabilité limitée (Personne morale)
    """

    EPST = 'EPST'
    """
    Etablissement public à caractère scientifique et technologique (Personne morale)
    """

    GIE = 'GIE'
    """
    Groupement d'interet economique (Personne morale)
    """

    INC = 'INC'
    """
    Titre inconnu (Personne morale)
    """

    ME = 'ME'
    """
    Maître (Personne physique)
    """

    MLE = 'MLE'
    """
    Mademoiselle (Personne physique)
    """

    MME = 'MME'
    """
    Madame (Personne physique)
    """

    MR = 'MR'
    """
    Monsieur (Personne physique)
    """

    REPRIS = 'REPRIS'
    """
    Titre issu de la reprise (Personne morale)
    """

    SA = 'SA'
    """
    Société anonyme (Personne morale)
    """

    SAEM = 'SAEM'
    """
    Société anonyme d'économie mixte (Personne morale)
    """

    SAI = 'SAI'
    """
    Société anonyme immobilière (Personne morale)
    """

    SARL = 'SARL'
    """
    Société à responsabilité limitée (Personne morale)
    """

    SAS = 'SAS'
    """
    Société par action simplifiée (Personne morale)
    """

    SASU = 'SASU'
    """
    Société par action simplifiée à associé unique (Personne morale)
    """

    SC = 'SC'
    """
    Société civile (Personne morale)
    """

    SCA = 'SCA'
    """
    Société civile agricole (Personne morale)
    """

    SCAQ = 'SCAQ'
    """
    Société civile aquacole (Personne morale)
    """

    SCI = 'SCI'
    """
    Société civile immobilière (Personne morale)
    """

    SELARL = 'SELARL'
    """
    Société d'exercice liberal à responsabilité limitée (Personne morale)
    """

    SEP = 'SEP'
    """
    Société en participation (Personne morale)
    """

    SCAC = 'SCAC'
    """
    Société en commandité par action (Personne morale)
    """

    SCCV = 'SCCV'
    """
    Société civile de construction et de vente (Personne morale)
    """

    SCF = 'SCF'
    """
    Société créée de fait (Personne morale)
    """

    SCM = 'SCM'
    """
    Société civile de moyens (Personne morale)
    """

    SCP = 'SCP'
    """
    Société civile de participation (Personne morale)
    """

    SCPA = 'SCPA'
    """
    Société civile particulière (Personne morale)
    """

    SCPE = 'SCPE'
    """
    Société civile de pêche (Personne morale)
    """

    SCPR = 'SCPR'
    """
    Société civile professionelle (Personne morale)
    """

    SELFA = 'SELFA'
    """
    Société d'exercice libérale à forme anonyme (Personne morale)
    """

    SOUSCRIPTEUR = '.'
    """
    Souscripteur (Personne morale)
    """

    SCS = 'SCS'
    """
    Société en commandité simple (Personne morale)
    """

    SNC = 'SNC'
    """
    Société en nom collectif (Personne morale)
    """

    SP = 'SP'
    """
    Société particulière (Personne morale)
    """

    SPL = 'SPL'
    """
    Société publique locale (Personne morale)
    """

    SYND = 'SYND'
    """
    Syndicat (Personne morale)
    """


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
