# -*- coding: utf-8 -*-


from fractions import Fraction
from openfisca_pf.base import (
    ArrayLike,
    DAY,
    Enum,
    ParameterNode,
    Period,
    Population,
    select,
    where,
    Variable
    )
from openfisca_pf.entities import Personne
from openfisca_pf.enums.rch import (
    NatureActe,
    TypeActe,
    )
from openfisca_pf.functions.currency import arrondi_superieur
from openfisca_pf.constants.units import BOOLEAN


class type_acte(Variable):
    value_type = Enum
    possible_values = TypeActe
    default_value = TypeActe.Transcription
    entity = Personne
    definition_period = DAY
    label = "Type d'acte auprès de la RCH"


class nature_acte(Variable):
    value_type = Enum
    possible_values = NatureActe
    default_value = NatureActe.Vente
    entity = Personne
    definition_period = DAY
    label = "Nature de l'acte"


class regime_de_faveur(Variable):
    value_type = bool
    entity = Personne
    definition_period = DAY
    label = "Indique si l'acte bénéficie d'un régime de faveur"
    unit = BOOLEAN


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
            (nature_acte == NatureActe.Rectification) |
            (nature_acte == NatureActe.Renonciation) |
            (nature_acte == NatureActe.ActeComplementaire) |
            (nature_acte == NatureActe.ConstitutionServitude) |
            (nature_acte == NatureActe.DroitAcces) |
            (nature_acte == NatureActe.DepotPiece) |
            (nature_acte == NatureActe.PactePreference) |
            (nature_acte == NatureActe.EtatDescriptifDivisionReglementCopropriete) |
            (nature_acte == NatureActe.ModificationEtatDescriptifDivisionReglementCopropriete) |
            (nature_acte == NatureActe.CahierCharges) |
            (nature_acte == NatureActe.ModificationCahierCharges) |
            (nature_acte == NatureActe.Avenant) |
            (nature_acte == NatureActe.Echange) |
            (nature_acte == NatureActe.RenouvellementAutorisationOccupationTemporaire) |
            (nature_acte == NatureActe.ConstatationRealisationConditionSuspensive) |
            (nature_acte == NatureActe.Constatation) |
            (nature_acte == NatureActe.Remploi) |
            (nature_acte == NatureActe.Convention) |
            (nature_acte == NatureActe.Certificat) |
            (nature_acte == NatureActe.PacteTontinier) |
            (nature_acte == NatureActe.ReserveDroitUsageHabitation) |
            (nature_acte == NatureActe.DecisionJustice)
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
        regime_de_faveur = personne('regime_de_faveur', period)
        montant_total_acte = personne('montant_total_acte', period)
        montant_initial_acte = personne('montant_initial_acte', period)

        disposition_default_value = parameters(period).daf.rch.taxe_publicite_immobiliere.disposition.default

        montant_tpi = select(
            [
                is_disposition,
            ],
            [
                disposition_default_value,
            ]
        )
        
        return montant_tpi