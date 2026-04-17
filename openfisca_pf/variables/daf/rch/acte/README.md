# TPI - Montant de la taxe de publicité immobilière

Documentation des paramètres et du calcul du montant de la **Taxe de Publicité Immobilière (TPI)**.

---

## Variables

### `montant_total_acte` _(int)_

Montant total de l’acte.

---

### `NatureActe` _(enum)_

Liste exhaustive des valeurs possibles pour `NatureActe`.

#### Transcription - Disposition

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
- `ConventionDivorce`
- `Certificat`
- `PacteTontinier`
- `ReserveDroitUsageHabitation`
- `DecisionJustice`

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

### Les dispositions

Chaque disposition est modélisée sous forme de variable. Il suffit d’indiquer un nombre correspondant au nombre d’occurrences de cette disposition pour un acte.

- `rectification`
- `renonciation`
- `acte_complementaire`
- `constitution_servitude`
- `droit_acces`
- `depot_piece`
- `pacte_preference`
- `etat_descriptif_division_reglement_copropriete`
- `modification_etat_descriptif_division_reglement_copropriete`
- `cahier_charges`
- `modification_cahier_charges`
- `avenant`
- `echange`
- `renouvellement_autorisation_occupation_temporaire`
- `constatation_realisation_condition_suspensive`
- `constatation`
- `remploi`
- `convention`
- `convention_divorce`
- `certificat_conformite`
- `pacte_tontinier`
- `reserve_droit_usage_habitation`
- `decision_justice`

---

### Les régimes de faveur

Même principe que pour les disposition.

- `aide_juridictionnelle`
- `acte_administratif_exonere`
- `programme_habitat_social`
- `etablissement_public`
- `aisi`
- `succesorale`
- `defiscalisation_outre_mer`
- `collectivites`
- `comptable_public`
- `autre`

---

### `montant_initial_acte` _(int)_

Montant d’inscription initial de l’acte.

Ce champ est requis avec la nature d'acte suivante :

- `renouvellement_hypotheque_judiciaire`

Dans ces cas, `montant_total_acte` représente le montant de l’acte **pour l’inscription courante**.

---

## Variables calculables

### `montant_tpi_acte` _(int)_

Montant de la taxe de publicité immobilière calculé pour l’acte.

---

### `type_acte` _(enum)_

Type de l’acte, déduit automatiquement à partir de la nature de l’acte (`NatureActe`).

- `Transcription`
- `Inscription`
- `Saisie`

---

### `est_exonere` _(bool)_

Indique si l'acte est exonéré de la taxe de publicité immobilière.

---

### `est_disposition` _(bool)_

Indique si la nature de l’acte correspond à une **disposition**.

### `montant_taxe_disposition` _(int)_

Montant correspondant à la somme des dispositions définient pour un acte.

---

## Calcul

Les variables calculées que l’on souhaite faire évaluer par OpenFisca, comme `montant_tpi_acte`, doivent être renseignées avec la valeur `null`.

Requête :

```json
{
  "personnes": {
    "Acte Rectification": {
      "montant_taxe_disposition": {
        "2025-03-01": null
      },
      "rectification": {
        "2025-03-01": 1
      },
      "montant_tpi_acte": {
        "2025-03-01": null
      },
      "nature_acte": {
        "2025-03-01": "Vente"
      },
      "montant_total_acte": {
        "2025-03-01": 3500
      }
    },
    "Acte rectification Renonciation": {
      "montant_taxe_disposition": {
        "2025-03-01": null
      },
      "rectification": {
        "2025-03-01": 1
      },

      "renonciation": {
        "2025-03-01": 1
      },
      "montant_tpi_acte": {
        "2025-03-01": null
      },
      "nature_acte": {
        "2025-03-01": "Vente"
      },
      "montant_total_acte": {
        "2025-03-01": 3500
      }
    },
    "Acte rectification x2 Renonciation": {
      "montant_taxe_disposition": {
        "2025-03-01": null
      },
      "rectification": {
        "2025-03-01": 2
      },
      "renonciation": {
        "2025-03-01": 1
      },
      "montant_tpi_acte": {
        "2025-03-01": null
      },
      "nature_acte": {
        "2025-03-01": "Vente"
      },
      "montant_total_acte": {
        "2025-03-01": 3500
      }
    }
  }
}
```

Réponse:

```json
{
  "personnes": {
    "Acte Rectification": {
      "montant_taxe_disposition": {
        "2025-03-01": 1500
      },
      "montant_total_acte": {
        "2025-03-01": 3500
      },
      "montant_tpi_acte": {
        "2025-03-01": 1504
      },
      "nature_acte": {
        "2025-03-01": "Vente"
      },
      "rectification": {
        "2025-03-01": 1
      }
    },
    "Acte rectification Renonciation": {
      "montant_taxe_disposition": {
        "2025-03-01": 3000
      },
      "montant_total_acte": {
        "2025-03-01": 3500
      },
      "montant_tpi_acte": {
        "2025-03-01": 3004
      },
      "nature_acte": {
        "2025-03-01": "Vente"
      },
      "rectification": {
        "2025-03-01": 1
      },
      "renonciation": {
        "2025-03-01": 1
      }
    },
    "Acte rectification x2 Renonciation": {
      "montant_taxe_disposition": {
        "2025-03-01": 4500
      },
      "montant_total_acte": {
        "2025-03-01": 3500
      },
      "montant_tpi_acte": {
        "2025-03-01": 4504
      },
      "nature_acte": {
        "2025-03-01": "Vente"
      },
      "rectification": {
        "2025-03-01": 2
      },
      "renonciation": {
        "2025-03-01": 1
      }
    }
  }
}
```
