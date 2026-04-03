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

### `disposition` _(enum)_

Disposition(s) appliquée.

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

La requête JSON est construite avec une population `personnes` utilisée ici pour représenter techniquement les dispositions rattachées aux actes. Chaque disposition doit donc être déclarée comme une entrée distincte dans `personnes`, avec sa `nature_disposition`. Lorsqu’un acte n’a pas de disposition, une disposition doit tout de même être fournie avec la valeur `Aucun` afin de conserver une structure homogène. Les actes sont ensuite déclarés dans `actes`, avec leurs variables propres (`nature_acte`, `montant_total_acte`, éventuellement `regime_faveur`, etc.) et une clé `dispositions` contenant la liste des identifiants de "personnes" correspondant aux dispositions de cet acte. Chaque disposition ne doit être rattachée qu’à un seul acte. Enfin, les variables calculées par OpenFisca, comme `montant_tpi_acte`, doivent pas être renseignées avec la valeur `null`.

Requête :

```json
{
  "personnes": {
    "acte1_disposition": {
      "nature_disposition": { "2026-04-01": "Aucun" }
    },
    "acte2_disposition1": {
      "nature_disposition": { "2026-04-01": "Echange" }
    },
    "acte2_disposition2": {
      "nature_disposition": { "2026-04-01": "Rectification" }
    },
    "acte3_disposition1": {
      "nature_disposition": { "2026-04-01": "Echange" }
    },
    "acte3_disposition2": {
      "nature_disposition": { "2026-04-01": "Rectification" }
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
        "2026-04-01": "Succesorale"
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
        "2026-04-01": "Succesorale"
      }
    }
  },
  "personnes": {
    "acte1_disposition": {
      "nature_disposition": {
        "2026-04-01": "Aucun"
      }
    },
    "acte2_disposition1": {
      "nature_disposition": {
        "2026-04-01": "Echange"
      }
    },
    "acte2_disposition2": {
      "nature_disposition": {
        "2026-04-01": "Rectification"
      }
    },
    "acte3_disposition1": {
      "nature_disposition": {
        "2026-04-01": "Echange"
      }
    },
    "acte3_disposition2": {
      "nature_disposition": {
        "2026-04-01": "Rectification"
      }
    }
  }
}
```
