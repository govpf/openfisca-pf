
# Documentation openfisca_pf - RCH

Ce document vise a fournir une documentation pour l'API des formules RCH implémentées dans le moteur de calcul Openfisca de la Polynésie Française développé par la DSI.

> Pour plus d'informations sur Openfisca :  
> [openfisca.org/doc/index.html](https://openfisca.org/doc/index.html)


# Les variables

Pour effectuer un calcul via l'API web Openfisca, vous devez définir la variable souhaitée avec la valeur `null` et fournir tous les paramètres requis pour le calcul.

L'API va ensuite remplacer la valeur `null` par le résultat du calcul demandé. Si le moteur ne trouve pas de formule avec les paramètres rentrés, le résultat sera égal à 0.

En cas d'erreurs quelconques lors du calcul, une erreur 500 sera renvoyée

> **Endpoint pour lancer un calcul** :  
> `POST {api-url}/calculate`

----------

## ENR - Montant de droit d'enregistrement

#### Paramètres

-   **`montant_droit_enregistrement` : `int` (variable à calculer)**
-   `type_demarche_rch` : `Acquisition`, `Baux`, `Navire`
-   `type_acheteur_rch` : `DroitCommun`, `PrimoAcquereur`
-   `type_bien_rch` : `TerrainNu`, `TerrainBati` (type du bien à définir pour les primo-acquéreurs)
-   `valeur_totale_bien_achat` : `int` (valeur du bien pour les acquisitions et cessions de navire)
-   `duree_bail_mois` : `int` (durée en mois du bail)
-   `valeur_locative_bien` : `int`

#### Exemples

**Acquisition - Droit commun**

```json
{
  "personnes": {
    "personne_1": {
      "montant_droit_enregistrement": {
        "2025-03-01": null
      },
      "type_demarche_rch": {
        "2025-03-01": "Acquisition"
      },
      "type_acheteur_rch": {
        "2025-03-01": "DroitCommun"
      },
      "valeur_totale_bien_achat": {
        "2025-03-01": 25000000
      }
    }
  }
}

```

**Acquisition - Primo-acquéreur**

```json
{
  "personnes": {
    "personne_1": {
      "montant_droit_enregistrement": {
        "2025-03-01": null
      },
      "type_demarche_rch": {
        "2025-03-01": "Acquisition"
      },
      "type_acheteur_rch": {
        "2025-03-01": "PrimoAcquereur"
      },
      "type_bien_rch": {
        "2025-03-01": "TerrainNu"
      },
      "valeur_totale_bien_achat": {
        "2025-03-01": 25000000
      }
    }
  }
}

```

**Baux**

```json
{
  "personnes": {
    "personne_1": {
      "montant_droit_enregistrement": {
        "2025-03-01": null
      },
      "type_demarche_rch": {
        "2025-03-01": "Baux"
      },
      "duree_bail_mois": {
        "2025-03-01": 12
      },
      "valeur_locative_bien": {
        "2025-03-01": 25000000
      }
    }
  }
}

```

**Cession de navire**

```json
{
  "personnes": {
    "personne_1": {
      "montant_droit_enregistrement": {
        "2025-03-01": null
      },
      "type_demarche_rch": {
        "2025-03-01": "Navire"
      },
      "valeur_totale_bien_achat": {
        "2025-03-01": 5000000
      }
    }
  }
}

```

----------

## TPI - Montant de taxe publicité immobilière

#### Paramètres

-   **`montant_taxe_publicite` : `int` (variable à calculer)**
-   `type_demarche_rch` : `Acquisition`, `Baux`
-   `type_acheteur_rch` : `DroitCommun`, `PrimoAcquereur`
-   `type_bien_rch` : `TerrainNu`, `TerrainBati` (type du bien à définir pour les primo-acquéreurs)
-   `valeur_totale_bien_achat` : `int` (valeur du bien pour les acquisitions)
-   `duree_bail_mois` : `int` (durée en années du bail)
-   `valeur_locative_bien` : `int`

#### Exemples

**Acquisition - Droit commun**

```json
{
  "personnes": {
    "personne_1": {
      "montant_taxe_publicite": {
        "2025-03-01": null
      },
      "type_demarche_rch": {
        "2025-03-01": "Acquisition"
      },
      "type_acheteur_rch": {
        "2025-03-01": "DroitCommun"
      },
      "valeur_totale_bien_achat": {
        "2025-03-01": 25000000
      }
    }
  }
}

```

**Acquisition - Primo-acquéreur**

```json
{
  "personnes": {
    "personne_1": {
      "montant_taxe_publicite": {
        "2025-03-01": null
      },
      "type_demarche_rch": {
        "2025-03-01": "Acquisition"
      },
      "type_acheteur_rch": {
        "2025-03-01": "PrimoAcquereur"
      },
      "type_bien_rch": {
        "2025-03-01": "TerrainNu"
      },
      "valeur_totale_bien_achat": {
        "2025-03-01": 25000000
      }
    }
  }
}

```

**Baux**

```json
{
  "personnes": {
    "personne_1": {
      "montant_taxe_publicite": {
        "2025-03-01": null
      },
      "type_demarche_rch": {
        "2025-03-01": "Baux"
      },
      "duree_bail_mois": {
        "2025-03-01": 12
      },
      "valeur_locative_bien": {
        "2025-03-01": 25000000
      }
    }
  }
}

```

----------

## Taxe sur la plus-value immobilière

#### Paramètres

-   **`montant_taxe_plus_value` : `int` (variable à calculer)**
-   `duree_possession_annee` : `int` (durée en années de la possession)
-   `valeur_plus_value_net` : `int`

#### Exemple

```json
{
  "personnes": {
    "personne_1": {
      "montant_taxe_plus_value": {
        "2025-03-01": null
      },
      "duree_possession_annee": {
        "2025-03-01": 2
      },
      "valeur_plus_value_net": {
        "2025-03-01": 600000
      }
    }
  }
}

```