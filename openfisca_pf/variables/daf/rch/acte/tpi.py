# -*- coding: utf-8 -*-


from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    ParameterNode,
    Period,
    Population,
    select,
    Variable
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.rch import (
    NatureActe,
    TypeActe,
    RegimeFaveur
    )
from openfisca_pf.functions.currency import arrondi_superieur


class nature_acte(Variable):
    value_type = Enum
    possible_values = NatureActe
    default_value = NatureActe.Vente
    entity = Personne
    definition_period = DAY
    label = "Nature de l'acte"


class type_acte(Variable):
    value_type = Enum
    possible_values = TypeActe
    default_value = TypeActe.Transcription
    entity = Personne
    definition_period = DAY
    label = "Type d'acte auprès de la RCH"

    def formula(personne: Population, period: Period) -> ArrayLike:
        nature_acte = personne('nature_acte', period)
        is_disposition = personne('is_disposition', period)
        return select(
            [
                is_disposition
                | (nature_acte == NatureActe.Vente)
                | (nature_acte == NatureActe.VenteSousConditionSuspensive)
                | (nature_acte == NatureActe.VenteEnEtatFuturAchevement)
                | (nature_acte == NatureActe.ConventionDivorce)
                | (nature_acte == NatureActe.Jugement)
                | (nature_acte == NatureActe.JugementAdjudication)
                | (nature_acte == NatureActe.Partage)
                | (nature_acte == NatureActe.LiquidationPartage)
                | (nature_acte == NatureActe.Bail)
                | (nature_acte == NatureActe.BailEmphyteotique)
                | (nature_acte == NatureActe.CessionBail)
                | (nature_acte == NatureActe.AttestationImmobiliere)
                | (nature_acte == NatureActe.AttestationImmobiliereComplementaire)
                | (nature_acte == NatureActe.Donation)
                | (nature_acte == NatureActe.DonationPartage)
                | (nature_acte == NatureActe.AutorisationOccupationTemporaire)
                | (nature_acte == NatureActe.CessionDroits)
                | (nature_acte == NatureActe.ActeAdministratif),
                (nature_acte == NatureActe.HypothequeLegale)
                | (nature_acte == NatureActe.HypothequeConventionnelle)
                | (nature_acte == NatureActe.PrivilegeVendeurActionResolutoire)
                | (nature_acte == NatureActe.InscriptionRectificative)
                | (nature_acte == NatureActe.HypothequeJudiciaireDefinitive)
                | (nature_acte == NatureActe.RenouvellementInscription),
                (nature_acte == NatureActe.PouvoirCommandementSaisieImmobiliere)
                | (nature_acte == NatureActe.SommationFinsSaisieImmobiliere)
                | (nature_acte == NatureActe.OrdonnanceValantSaisieImmobiliere)
                | (nature_acte == NatureActe.PouvoirCommandementDePayerDelaisser)
                | (nature_acte == NatureActe.SommationPayerDelaisser)
                ],
            [
                TypeActe.Transcription,
                TypeActe.Inscription,
                TypeActe.Saisie
                ]
            )


class regime_faveur(Variable):
    value_type = Enum
    possible_values = RegimeFaveur
    default_value = RegimeFaveur.Aucun
    entity = Personne
    definition_period = DAY
    label = "Indique un régime de faveur de l'acte"


class montant_total_acte(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant total d'un acte"


class montant_initial_acte(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de l'inscription initial d'un acte"


class is_disposition(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Indique si la nature de l'acte est une disposition"

    def formula(personne: Population, period: Period) -> ArrayLike:
        nature_acte = personne('nature_acte', period)
        return (
            (nature_acte == NatureActe.Rectification)
            | (nature_acte == NatureActe.Renonciation)
            | (nature_acte == NatureActe.ActeComplementaire)
            | (nature_acte == NatureActe.ConstitutionServitude)
            | (nature_acte == NatureActe.DroitAcces)
            | (nature_acte == NatureActe.DepotPiece)
            | (nature_acte == NatureActe.PactePreference)
            | (nature_acte == NatureActe.EtatDescriptifDivisionReglementCopropriete)
            | (nature_acte == NatureActe.ModificationEtatDescriptifDivisionReglementCopropriete)
            | (nature_acte == NatureActe.CahierCharges)
            | (nature_acte == NatureActe.ModificationCahierCharges)
            | (nature_acte == NatureActe.Avenant)
            | (nature_acte == NatureActe.Echange)
            | (nature_acte == NatureActe.RenouvellementAutorisationOccupationTemporaire)
            | (nature_acte == NatureActe.ConstatationRealisationConditionSuspensive)
            | (nature_acte == NatureActe.Constatation)
            | (nature_acte == NatureActe.Remploi)
            | (nature_acte == NatureActe.Convention)
            | (nature_acte == NatureActe.Certificat)
            | (nature_acte == NatureActe.PacteTontinier)
            | (nature_acte == NatureActe.ReserveDroitUsageHabitation)
            | (nature_acte == NatureActe.DecisionJustice)
            )


class taux_tpi(Variable):
    value_type = float
    entity = Personne
    definition_period = DAY
    label = "Taux de la taxe de publicité immobilière selon le type d'acte"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        nature_acte = personne('nature_acte', period)
        taux_parameters = parameters(period).daf.rch.taxe_publicite_immobiliere.acte.taux
        return select(
            [
                # Transcription (Acte initial)
                nature_acte == NatureActe.Vente,
                nature_acte == NatureActe.VenteSousConditionSuspensive,
                nature_acte == NatureActe.VenteEnEtatFuturAchevement,
                nature_acte == NatureActe.ConventionDivorce,
                nature_acte == NatureActe.Jugement,
                nature_acte == NatureActe.JugementAdjudication,
                nature_acte == NatureActe.Partage,
                nature_acte == NatureActe.LiquidationPartage,
                nature_acte == NatureActe.Bail,
                nature_acte == NatureActe.BailEmphyteotique,
                nature_acte == NatureActe.CessionBail,
                nature_acte == NatureActe.AttestationImmobiliere,
                nature_acte == NatureActe.AttestationImmobiliereComplementaire,
                nature_acte == NatureActe.Donation,
                nature_acte == NatureActe.DonationPartage,
                nature_acte == NatureActe.AutorisationOccupationTemporaire,
                nature_acte == NatureActe.CessionDroits,
                nature_acte == NatureActe.ActeAdministratif,
                # Inscription
                nature_acte == NatureActe.HypothequeLegale,
                nature_acte == NatureActe.HypothequeConventionnelle,
                nature_acte == NatureActe.PrivilegeVendeurActionResolutoire,
                nature_acte == NatureActe.InscriptionRectificative,
                nature_acte == NatureActe.HypothequeJudiciaireDefinitive,
                nature_acte == NatureActe.RenouvellementInscription
                ],
            [
                # Transcription (Acte initial)
                taux_parameters.vente,
                taux_parameters.vente_sous_condition_suspensive,
                taux_parameters.vente_en_etat_futur_achevement,
                taux_parameters.convention_divorce,
                taux_parameters.jugement,
                taux_parameters.jugement_adjudication,
                taux_parameters.partage,
                taux_parameters.liquidation_partage,
                taux_parameters.bail,
                taux_parameters.bail_emphyteotique,
                taux_parameters.cession_bail,
                taux_parameters.attestation_immobiliere,
                taux_parameters.attestation_immobiliere_complementaire,
                taux_parameters.donation,
                taux_parameters.donation_partage,
                taux_parameters.autorisation_occupation_temporaire,
                taux_parameters.cession_droits,
                taux_parameters.acte_administratif,
                # Inscription
                taux_parameters.hypotheque_legale,
                taux_parameters.hypotheque_conventionnelle,
                taux_parameters.privilege_vendeur_action_resolutoire,
                taux_parameters.inscription_rectificative,
                taux_parameters.hypotheque_judiciaire_definitive,
                taux_parameters.renouvellement_inscription
                ]
            )


class montant_tpi_acte(Variable):
    value_type = int
    entity = Personne
    definition_period = DAY
    label = "Montant de la taxe de publicité immobilière selon la nature de l'acte"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        type_acte = personne('type_acte', period)
        nature_acte = personne('nature_acte', period)
        is_disposition = personne('is_disposition', period)
        regime_faveur = personne('regime_faveur', period)
        montant_total_acte = personne('montant_total_acte', period)
        montant_initial_acte = personne('montant_initial_acte', period)

        taux_tpi = personne('taux_tpi', period)
        fixed_default_value = parameters(period).daf.rch.taxe_publicite_immobiliere.acte.fixed.default

        montant_tpi = select(
            [
                regime_faveur != RegimeFaveur.Aucun,
                nature_acte == NatureActe.Echange,
                is_disposition | (type_acte == TypeActe.Saisie),
                (nature_acte == NatureActe.RenouvellementInscription) | (nature_acte == NatureActe.InscriptionRectificative),
                True
                ],
            [
                0,
                fixed_default_value * 2,
                fixed_default_value,
                fixed_default_value + arrondi_superieur((montant_total_acte - montant_initial_acte) * taux_tpi),
                arrondi_superieur(montant_total_acte * taux_tpi),
                ]
            )

        return montant_tpi
