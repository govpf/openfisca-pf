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


class is_bilan_actif_immobilisation_incorporelles_frais_etablissement_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, frais d'établissement net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        frais_etablissement_brut = personne('is_bilan_actif_immobilisation_incorporelles_frais_etablissement_brut', period)
        frais_etablissement_amortissement_provisions = personne('is_bilan_actif_immobilisation_incorporelles_frais_etablissement_amortissements_provisions', period)
        return frais_etablissement_brut - frais_etablissement_amortissement_provisions


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


class is_bilan_actif_immobilisation_incorporelles_fonds_commercial_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, fonds commercial net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        fonds_commercial_brut = personne('is_bilan_actif_immobilisation_incorporelles_fonds_commercial_brut', period)
        fonds_commercial_amortissement_provisions = personne('is_bilan_actif_immobilisation_incorporelles_fonds_commercial_amortissements_provisions', period)
        return fonds_commercial_brut - fonds_commercial_amortissement_provisions


class is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, autres immobilisations incorporelles brut (AJ)"


class is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, autres immobilisations incorporelles amortissements, provisions (AK)"


class is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations incorporelles, autres immobilisations incorporelles net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        autres_immobilisations_incorporelles_brut = personne('is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_brut', period)
        autres_immobilisations_incorporelles_amortissement_provisions = personne('is_bilan_actif_immobilisation_incorporelles_autres_immobilisations_incorporelles_amortissements_provisions', period)
        return autres_immobilisations_incorporelles_brut - autres_immobilisations_incorporelles_amortissement_provisions


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


class is_bilan_actif_immobilisation_corporelles_terrains_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, terrains net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        terrains_brut = personne('is_bilan_actif_immobilisation_corporelles_terrains_brut', period)
        terrains_amortissement_provisions = personne('is_bilan_actif_immobilisation_corporelles_terrains_amortissements_provisions', period)
        return terrains_brut - terrains_amortissement_provisions


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


class is_bilan_actif_immobilisation_corporelles_constructions_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, constructions net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        constructions_brut = personne('is_bilan_actif_immobilisation_corporelles_constructions_brut', period)
        constructions_amortissement_provisions = personne('is_bilan_actif_immobilisation_corporelles_constructions_amortissements_provisions', period)
        return constructions_brut - constructions_amortissement_provisions


class is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_brut(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, installations techniques, matériel, outillage industriel brut (AR)"


class is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_amortissements_provisions(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, installations techniques, matériel, outillage industriel amortissements, provisions (AS)"


class is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, installations techniques, matériel, outillage industriel net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        installations_techniques_brut = personne('is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_brut', period)
        installations_techniques_amortissement_provisions = personne('is_bilan_actif_immobilisation_corporelles_installations_techniques_materiel_outillage_industriel_amortissements_provisions', period)
        return installations_techniques_brut - installations_techniques_amortissement_provisions


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


class is_bilan_actif_immobilisation_corporelles_autres_immobilisations_corporelles_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, autres immobilisations corporelles net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        autres_immobilisations_corporelles_brut = personne('is_bilan_actif_immobilisation_corporelles_autres_immobilisations_corporelles_brut', period)
        autres_immobilisations_corporelles_amortissement_provisions = personne('is_bilan_actif_immobilisation_corporelles_autres_immobilisations_corporelles_amortissements_provisions', period)
        return autres_immobilisations_corporelles_brut - autres_immobilisations_corporelles_amortissement_provisions


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


class is_bilan_actif_immobilisation_corporelles_immobilisations_en_cours_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations corporelles, immobilisations en cours net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        immobilisations_en_cours_brut = personne('is_bilan_actif_immobilisation_corporelles_immobilisations_en_cours_brut', period)
        immobilisations_en_cours_amortissement_provisions = personne('is_bilan_actif_immobilisation_corporelles_immobilisations_en_cours_amortissements_provisions', period)
        return immobilisations_en_cours_brut - immobilisations_en_cours_amortissement_provisions


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


class is_bilan_actif_immobilisation_financieres_participations_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, participations et créances rattachées net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        participations_brut = personne('is_bilan_actif_immobilisation_financieres_participations_brut', period)
        participations_amortissement_provisions = personne('is_bilan_actif_immobilisation_financieres_participations_amortissements_provisions', period)
        return participations_brut - participations_amortissement_provisions


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


class is_bilan_actif_immobilisation_financieres_creance_rattachees_participations_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, créances rattachées à des participations net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        creances_rattachees_participations_brut = personne('is_bilan_actif_immobilisation_financieres_creance_rattachees_participations_brut', period)
        creances_rattachees_participations_amortissement_provisions = personne('is_bilan_actif_immobilisation_financieres_creance_rattachees_participations_amortissements_provisions', period)
        return creances_rattachees_participations_brut - creances_rattachees_participations_amortissement_provisions


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


class is_bilan_actif_immobilisation_financieres_autres_titres_immobilises_net(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Immobilisations financières, autres titres immobilisés net"

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        autres_titres_immobilises_brut = personne('is_bilan_actif_immobilisation_financieres_autres_titres_immobilises_brut', period)
        autres_titres_immobilises_amortissement_provisions = personne('is_bilan_actif_immobilisation_financieres_autres_titres_immobilises_amortissements_provisions', period)
        return autres_titres_immobilises_brut - autres_titres_immobilises_amortissement_provisions
