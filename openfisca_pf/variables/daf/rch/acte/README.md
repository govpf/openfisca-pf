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

### `est_disposition` _(bool)_

Indique si la nature de l’acte correspond à une **disposition**.

---

## Paramètres d’entrée

### `NatureActe` _(enum)_

Liste exhaustive des valeurs possibles pour `NatureActe`.

---

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

### `montant_total_acte` _(int)_

Montant total de l’acte.

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

### `montant_taxe_disposition` _(int)_

Montant correspondant à la somme des dispositions définient pour un acte.

---

### Les régimes de faveur

Même principe que pour les disposition.

- `aide_juridictionnelle`
- `acte_administratif_exonere`
- `programme_habitat_social`
- `etablissement_public`
- `AISI`
- `succesorale`
- `defiscalisation_outre_mer`
- `collectivites`
- `comptable_public`
- `autre`

---

### `montant_initial_acte` _(int)_

Montant d’inscription initial de l’acte.

Ce champ est requis dans les cas suivants :

- `inscription_rectificative`
- `renouvellement_inscription`

Dans ces cas, `montant_total_acte` représente le montant de l’acte **pour l’inscription courante**.

---

## Calcul

Enfin, les variables calculées par OpenFisca, comme `montant_tpi_acte`, doivent pas être renseignées avec la valeur `null`.

Requête :

```json
{
  "personnes": {
    "acte1_disposition": {
      "nature_disposition": { "2026-04-01": "aucun" }
    },
    "acte2_disposition1": {
      "nature_disposition": { "2026-04-01": "echange" }
    },
    "acte2_disposition2": {
      "nature_disposition": { "2026-04-01": "rectification" }
    },
    "acte3_disposition1": {
      "nature_disposition": { "2026-04-01": "echange" }
    },
    "acte3_disposition2": {
      "nature_disposition": { "2026-04-01": "rectification" }
    }
  },
  "actes": {
    "acte1": {
      "nature_acte": {
        "2026-04-01": "Vente"
      },
      "montant_tpi_acte": {
        "2026-04-01": null
      },
      "montant_total_acte": {
        "2026-04-01": 25000
      },
      "dispositions": ["acte1_disposition"]
    },
    "acte2": {
      "nature_acte": {
        "2026-04-01": "Vente"
      },
      "montant_tpi_acte": {
        "2026-04-01": null
      },
      "montant_total_acte": {
        "2026-04-01": 25000
      },
      "dispositions": ["acte2_disposition1", "acte2_disposition2"]
    },
    "acte3": {
      "nature_acte": {
        "2026-04-01": "Vente"
      },
      "montant_tpi_acte": {
        "2026-04-01": null
      },
      "regime_faveur": {
        "2026-04-01": "succesorale"
      },
      "montant_total_acte": {
        "2026-04-01": 25000
      },
      "dispositions": ["acte3_disposition1", "acte3_disposition2"]
    }
  }
}
```

Réponse:

```json
{
  "actes": {
    "acte1": {
      "dispositions": ["acte1_disposition"],
      "montant_total_acte": {
        "2026-04-01": 25000
      },
      "montant_tpi_acte": {
        "2026-04-01": 1500
      },
      "nature_acte": {
        "2026-04-01": "Vente"
      }
    },
    "acte2": {
      "dispositions": ["acte2_disposition1", "acte2_disposition2"],
      "montant_total_acte": {
        "2026-04-01": 25000
      },
      "montant_tpi_acte": {
        "2026-04-01": 4525
      },
      "nature_acte": {
        "2026-04-01": "Vente"
      }
    },
    "acte3": {
      "dispositions": ["acte3_disposition1", "acte3_disposition2"],
      "montant_total_acte": {
        "2026-04-01": 25000
      },
      "montant_tpi_acte": {
        "2026-04-01": 0
      },
      "nature_acte": {
        "2026-04-01": "Vente"
      },
      "regime_faveur": {
        "2026-04-01": "succesorale"
      }
    }
  },
  "personnes": {
    "acte1_disposition": {
      "nature_disposition": {
        "2026-04-01": "aucun"
      }
    },
    "acte2_disposition1": {
      "nature_disposition": {
        "2026-04-01": "echange"
      }
    },
    "acte2_disposition2": {
      "nature_disposition": {
        "2026-04-01": "rectification"
      }
    },
    "acte3_disposition1": {
      "nature_disposition": {
        "2026-04-01": "echange"
      }
    },
    "acte3_disposition2": {
      "nature_disposition": {
        "2026-04-01": "rectification"
      }
    }
  }
}
```
