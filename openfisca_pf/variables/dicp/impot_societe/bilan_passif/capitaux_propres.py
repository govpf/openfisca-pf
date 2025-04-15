# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne

class is_bilan_passif_capital_social_ou_individuel(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Capital social ou individuel (DA)"


class is_bilan_passif_capital_social_ou_individuel_dont_verse(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Capital social ou individuel dont verse"


class is_bilan_passif_primes_emission_de_fusion_apports(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Primes d'émission, de fusion et d'apport (DB)"


class is_bilan_passif_ecart_de_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Ecart de réévaluation (DC)"


class is_bilan_passif_reserve_legal(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Réserve légale (DD)"


class is_bilan_passif_reserve_statutaire_ou_contractuelles(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Réserves statutaires ou contractuelles (DE)"


class is_bilan_passif_autres_reserves(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres réserves (DG)"


class is_bilan_passif_report_a_nouveau(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Report à nouveau (DH)"


class is_bilan_passif_resultat_de_l_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Résultat de l'exercice (bénéfice ou perte) (DI)"


class is_bilan_passif_subventions_d_investissement(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Subventions d'investissement (DJ)"


class is_bilan_passif_provisions_reglementees(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Provisions réglementées (DK)"

