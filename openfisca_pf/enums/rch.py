# -*- coding: utf-8 -*-


"""
La Direction des Affaires Foncières (DAF) de la Polynésie française gère la section Recette-Conservation des Hypothèques (RCH),
qui a pour mission de conserver les registres fonciers, délivrer les titres de propriété, liquider et percevoir les droits relatifs,
accomplir les formalités civiles pour la conservation des hypothèques et la consolidation des mutations de propriétés immobilières,
délivrer des états et certificats, liquider et percevoir les droits d'enregistrement, les baux, et les redevances domaniales.
"""


from openfisca_pf.base import Enum


__all__ = [
    'TypeAcheteur',
    'TypeBien',
    'TypeDemarche',
    'TypeParente'
    ]


class TypeAcheteur(Enum):
    PrimoAcquereur = 'Primo_acquéreur'
    DroitCommun = 'Acquéreur de droit commun'


class TypeBien(Enum):
    TerrainNu = 'Terrain Nu'
    TerrainBati = 'Terrain bâti'
    Appartement = 'Appartement'


class TypeDemarche(Enum):
    DonsMeubles = 'Don manuel de biens meubles'
    Baux = 'Baux en régime normal'
    Acquisition = 'Acquisition ou vente'
    PlusValuesImmobiliere = 'Plus-values immobilières'
    Navire = 'Cession de navire'


class TypeParente(Enum):
    LigneDirecte = 'Mutations en ligne directe (époux/concubins, frères et soeurs)'
    ParentCollateral = 'Parents en ligne collatérale de 3eme degré'
    NonParent = 'Non parents et parents en ligne collatérale à partir du 4eme degré'


class TypeActe(Enum):
    Transcription = 'Transcription'
    Inscription = 'Inscription'
    Saisie = 'Saisie'


class RegimeFaveur(Enum):
    AideJuridictionnelle = 'aide_juridictionnelle'
    ActeAdministratifExonere = 'acte_administratif_exonere'
    ProgrammeHabitatSocial = 'programme_habitat_social'
    EtablissementPublic = 'etablissement_public'
    AISI = 'aisi'
    Succesorale = 'succesorale'
    DefiscalisationOutreMer = 'defiscalisation_outre_mer'
    Collectivites = 'collectivites'
    ComptablePublic = 'comptable_public'
    titrement = 'titrement'
    Autre = 'autre'


class DispositionVariables(Enum):
    Rectification = 'rectification'
    Renonciation = 'renonciation'
    ActeComplementaire = 'acte_complementaire'
    ConstitutionServitude = 'constitution_servitude'
    DroitAcces = 'droit_acces'
    DepotPiece = 'depot_piece'
    PactePreference = 'pacte_preference'
    EtatDescriptifDivisionReglementCopropriete = 'etat_descriptif_division_reglement_copropriete'
    ModificationEtatDescriptifDivisionReglementCopropriete = 'modification_etat_descriptif_division_reglement_copropriete'
    CahierCharges = 'cahier_charges'
    ModificationCahierCharges = 'modification_cahier_charges'
    Avenant = 'avenant'
    Echange = 'echange'
    RenouvellementAutorisationOccupationTemporaire = 'renouvellement_autorisation_occupation_temporaire'
    ConstatationRealisationConditionSuspensive = 'constatation_realisation_condition_suspensive'
    Constatation = 'constatation'
    Remploi = 'remploi'
    Convention = 'convention'
    Certificat = 'certificat_conformite'
    PacteTontinier = 'pacte_tontinier'
    ReserveDroitUsageHabitation = 'reserve_droit_usage_habitation'
    DecisionJustice = 'decision_justice'
    ConventionDivorce = 'convention_divorce'


class NatureActe(Enum):
    # Transcription (Disposition)
    Rectification = 'rectification'
    Renonciation = 'renonciation'
    ActeComplementaire = 'acte_complementaire'
    ConstitutionServitude = 'constitution_servitude'
    DroitAcces = 'droit_acces'
    DepotPiece = 'depot_piece'
    PactePreference = 'pacte_preference'
    EtatDescriptifDivisionReglementCopropriete = 'etat_descriptif_division_reglement_copropriete'
    ModificationEtatDescriptifDivisionReglementCopropriete = 'modification_etat_descriptif_division_reglement_copropriete'
    CahierCharges = 'cahier_charges'
    ModificationCahierCharges = 'modification_cahier_charges'
    Avenant = 'avenant'
    Echange = 'echange'
    RenouvellementAutorisationOccupationTemporaire = 'renouvellement_autorisation_occupation_temporaire'
    ConstatationRealisationConditionSuspensive = 'constatation_realisation_condition_suspensive'
    Constatation = 'constatation'
    Remploi = 'remploi'
    Convention = 'convention'
    Certificat = 'certificat_conformite'
    PacteTontinier = 'pacte_tontinier'
    ReserveDroitUsageHabitation = 'reserve_droit_usage_habitation'
    DecisionJustice = 'decision_justice'

    # Transcription (Acte initial)
    Vente = 'vente'
    VenteSousConditionSuspensive = 'vente_sous_condition_suspensive'
    VenteEnEtatFuturAchevement = 'vente_en_etat_futur_achevement'
    ConventionDivorce = 'convention_divorce'
    Jugement = 'jugement'
    JugementAdjudication = 'jugement_adjudication'
    Partage = 'partage'
    LiquidationPartage = 'liquidation_partage'
    Bail = 'bail'
    BailEmphyteotique = 'bail_emphyteotique'
    CessionBail = 'cession_bail'
    AttestationImmobiliere = 'attestation_immobiliere'
    AttestationImmobiliereComplementaire = 'attestation_immobiliere_complementaire'
    Donation = 'donation'
    DonationPartage = 'donation_partage'
    AutorisationOccupationTemporaire = 'autorisation_occupation_temporaire'
    CessionDroits = 'cession_droits'
    ActeAdministratif = 'acte_administratif'

    # Inscription
    HypothequeLegale = 'hypotheque_legale'
    HypothequeConventionnelle = 'hypotheque_conventionnelle'
    HypothequeJudiciaireProvisoire = 'hypotheque_judiciaire_provisoire'
    PrivilegeVendeurActionResolutoire = 'privilege_vendeur_action_resolutoire'
    InscriptionRectificative = 'inscription_rectificative'
    HypothequeJudiciaireDefinitive = 'hypotheque_judiciaire_definitive'
    RenouvellementHypothequeJudiciaire = 'renouvellement_hypotheque_judiciaire'
    RenouvellementInscription = 'renouvellement_inscription'

    # Saisie-immobiliere
    PouvoirCommandementSaisieImmobiliere = 'pouvoir_commandement_saisie_immobiliere'
    SommationFinsSaisieImmobiliere = 'sommation_fins_saisie_immobiliere'
    OrdonnanceValantSaisieImmobiliere = 'ordonnance_valant_saisie_immobiliere'
    PouvoirCommandementDePayerDelaisser = 'pouvoir_commandement_de_payer_delaisser'
    SommationPayerDelaisser = 'sommation_payer_delaisser'
