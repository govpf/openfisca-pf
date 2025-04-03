# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    ArrayLike,
    ParameterNode,
    Period,
    Population,
    Variable,
    YEAR
)
from openfisca_pf.entities import Personne


# Immobilisations incorporelles
class is_bilan_actif_immobilisation_incorporelles_frais_etablissement_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, frais d'établissement brut (AB)"


class is_bilan_actif_immobilisation_incorporelles_frais_etablissement_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, frais d'établissement amortissement, provisions (AC)"


class is_bilan_actif_immobilisation_incorporelles_fonds_commercial_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, fonds commercial brut (AH)"


class is_bilan_actif_immobilisation_incorporelles_fonds_commercial_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, fonds commercial amortissements, provisions (AI)"


class is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, autres immobilisations incorporelles brut (AJ)"


class is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_amortissements_provisions(
    Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, autres immobilisations incorporelles amortissements, provisions (AK)"


# Immobilisations corporelles
class is_bilan_actif_immobilisation_corporelles_terrains_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, terrains brut (AN)"


class is_bilan_actif_immobilisation_corporelles_terrains_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, terrains amortissements, provisions (AO)"


class is_bilan_actif_immobilisation_corporelles_constructions_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, constructions brut (AP)"


class is_bilan_actif_immobilisation_corporelles_constructions_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, constructions amortissements, provisions (AQ)"


class is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, installations techniques, matériel, outillage industriel brut (AR)"


class is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_amortissements_provisions(
    Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, installations techniques, matériel, outillage industriel amortissements, provisions (AS)"


class is_bilan_actif_immobilisation_corporelles_autres_immobilisations_corporelles_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, autres immobilisations corporelles brut (AT)"


class is_bilan_actif_immobilisation_corporelles_autres_immobilisations_corporelles_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, autres immobilisations corporelles amortissements, provisions (AU)"


class is_bilan_actif_immobilisation_corporelles_immobilisations_en_cours_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, immobilisations en cours brut (AV)"


class is_bilan_actif_immobilisation_corporelles_immobilisations_en_cours_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, immobilisations en cours amortissements, provisions (AW)"


# Immobilisations financières
class is_bilan_actif_immobilisation_financieres_participations_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, participations et créances rattachées brut (AZ)"


class is_bilan_actif_immobilisation_financieres_participations_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, participations et créances rattachées amortissements, provisions (BA)"


class is_bilan_actif_immobilisation_financieres_creance_rattachees_participations_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, créances rattachées à des participations brut (BB)"


class is_bilan_actif_immobilisation_financieres_creance_rattachees_participations_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, créances rattachées à des participations amortissements, provisions (BC)"


class is_bilan_actif_immobilisation_financieres_autres_titres_immobilises_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, autres titres immobilisés brut (BD)"


class is_bilan_actif_immobilisation_financieres_autres_titres_immobilises_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, autres titres immobilisés amortissements, provisions (BE)"
