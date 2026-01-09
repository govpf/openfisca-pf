# TPI - Montant de la taxe de publicité immobilière

Documentation des paramètres et du calcul du montant de la **Taxe de Publicité Immobilière (TPI)**.

---

## Paramètres calculés

### `montant_tpi_acte` _(int)_

Montant de la taxe de publicité immobilière calculé pour l’acte.

---

### `type_acte` _(enum)_

Type de l’acte, déduit automatiquement à partir de la nature de l’acte (`NatureActe`).

- `Transcription`
- `Inscription`
- `Saisie`

---

### `is_disposition` _(bool)_

Indique si la nature de l’acte correspond à une **disposition**.

---

## Paramètres d’entrée

### `NatureActe` _(enum)_

Liste exhaustive des valeurs possibles pour `NatureActe`.

---

#### Transcription - Dispositions

- `Rectification`
- `Renonciation`
- `ActeComplementaire`
- `ConstitutionServitude`
- `DroitAcces`
- `DepotPiece`
- `PactePreference`
- `EtatDescriptifDivisionReglementCopropriete`
- `ModificationEtatDescriptifDivisionReglementCopropriete`
- `CahierCharges`
- `ModificationCahierCharges`
- `Avenant`
- `Echange`
- `RenouvellementAutorisationOccupationTemporaire`
- `ConstatationRealisationConditionSuspensive`
- `Constatation`
- `Remploi`
- `Convention`
- `Certificat`
- `PacteTontinier`
- `ReserveDroitUsageHabitation`
- `DecisionJustice`

---

#### Transcription - Acte initial

- `Vente`
- `VenteSousConditionSuspensive`
- `VenteEnEtatFuturAchevement`
- `ConventionDivorce`
- `Jugement`
- `JugementAdjudication`
- `Partage`
- `LiquidationPartage`
- `Bail`
- `BailEmphyteotique`
- `CessionBail`
- `AttestationImmobiliere`
- `AttestationImmobiliereComplementaire`
- `Donation`
- `DonationPartage`
- `AutorisationOccupationTemporaire`
- `CessionDroits`
- `ActeAdministratif`

---

#### Inscription

- `HypothequeLegale`
- `HypothequeConventionnelle`
- `HypothequeJudiciaireProvisoire`
- `PrivilegeVendeurActionResolutoire`
- `InscriptionRectificative`
- `HypothequeJudiciaireDefinitive`
- `RenouvellementInscription`

---

#### Saisie immobilière

- `PouvoirCommandementSaisieImmobiliere`
- `SommationFinsSaisieImmobiliere`
- `OrdonnanceValantSaisieImmobiliere`
- `PouvoirCommandementDePayerDelaisser`
- `SommationPayerDelaisser`

---

### `montant_total_acte` _(int)_

Montant total de l’acte.

---

### `regime_faveur` _(enum)_

Régime de faveur appliqué.

- `AideJuridictionnelle`
- `ActeAdministratifExonere`
- `ProgrammeHabitatSocial`
- `ComptablePublic`
- `Succesorale`
- `Collectivites`
- `Titrement`
- `Autre`
- `Aucun` _(par défaut)_

---

### `montant_initial_acte` _(int)_

Montant d’inscription initial de l’acte.

Ce champ est requis dans les cas suivants :

- `inscription_rectificative`
- `renouvellement_inscription`

Dans ces cas, `montant_total_acte` représente le montant de l’acte **pour l’inscription courante**.

---

## Calcul

### Exemple standard

```json
{
  "personnes": {
    "personne_1": {
      "montant_tpi_acte": {
        "2025-03-01": null
      },
      "nature_acte": {
        "2025-03-01": "Vente"
      },
      "montant_total_acte": {
        "2025-03-01": 25000
      }
    }
  }
}
```

---

### Exemple avec récupération du type d’acte et de la disposition

```json
{
  "personnes": {
    "personne_1": {
      "montant_tpi_acte": {
        "2025-03-01": null
      },
      "type_acte": {
        "2025-03-01": null
      },
      "is_disposition": {
        "2025-03-01": null
      },
      "nature_acte": {
        "2025-03-01": "Vente"
      },
      "montant_total_acte": {
        "2025-03-01": 25000
      }
    }
  }
}
```
