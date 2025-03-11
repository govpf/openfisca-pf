from openfisca_core.model_api import YEAR, Variable
# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import Personne


# Participations et créances attachées à des participations
class is_immobilisations_financieres_participations_et_creances_participation_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Participations et créances attachées à des participations, Valeur brute des immobilisations au début de l'exercice (1L)"


class is_immobilisations_financieres_participations_et_creances_participation_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Participations et créances attachées à des participations, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (1M)"


class is_immobilisations_financieres_participations_et_creances_participation_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Participations et créances attachées à des participations, Augmentations Acquisitions, créations, apports et virements de poste à poste  (1N)"


class is_immobilisations_financieres_participations_et_creances_participation_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Participations et créances attachées à des participations, Diminutions par virement de poste à poste (IZ)"


class is_immobilisations_financieres_participations_et_creances_participation_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Participations et créances attachées à des participations, Diminutions par cession à des tiers ou mises hors services (1Y)"


class is_immobilisations_financieres_participations_et_creances_participation_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Participations et créances attachées à des participations, Valeur brute des immobilisations à la fin de l'exercice (1Z)"


class is_immobilisations_financieres_participations_et_creances_participation_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Participations et créances attachées à des participations, Valeur d'origine des immobilisations réévaluées en fin d'exercice (2A)"


# Prêts et autres immobilisations financières
class is_immobilisations_financieres_prets_et_autres_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Prêts et autres immobilisations financières, Valeur brute des immobilisations au début de l'exercice (1T)"


class is_immobilisations_financieres_prets_et_autres_augmentation_reevaluation(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = YEAR
    label = "Prêts et autres immobilisations financières, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (1U)"


class is_immobilisations_financieres_prets_et_autres_augmentation_nouveaux(Variable):
    value_type = int
    default_value = 0
    entity = Personne
    definition_period = YEAR
    label = "Prêts et autres immobilisations financières, Augmentations Acquisitions, créations, apports et virements de poste à poste (1V)"


class is_immobilisations_financieres_prets_et_autres_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Prêts et autres immobilisations financières, Diminutions par virement de poste à poste (I2)"


class is_immobilisations_financieres_prets_et_autres_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Prêts et autres immobilisations financières, Diminutions par cession à des tiers ou mises hors services (2E)"


class is_immobilisations_financieres_prets_et_autres_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Prêts et autres immobilisations financières, Valeur brute des immobilisations à la fin de l'exercice (2F)"


class is_immobilisations_financieres_prets_et_autres_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Prêts et autres immobilisations financières, Valeur d'origine des immobilisations réévaluées en fin d'exercice (2G)"


# Total IV
class is_immobilisations_total_financieres_brute_debut_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations financières, Valeur brute des immobilisations au début de l'exercice (LQ)"

    def formula(person, period):
        immo_participations = person('is_immobilisations_financieres_participations_et_creances_participation_brute_debut_exercice', period)
        immo_autres = person('is_immobilisations_financieres_prets_et_autres_brute_debut_exercice', period)
        return immo_participations + immo_autres


class is_immobilisations_total_financieres_augmentation_reevaluation(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations financières, Augmentations Consécutives à une réévaluation pratiquée au cours de l'exercice (LR)"

    def formula(person, period):
        immo_participations = person('is_immobilisations_financieres_participations_et_creances_participation_augmentation_reevaluation', period)
        immo_autres = person('is_immobilisations_financieres_prets_et_autres_augmentation_reevaluation', period)
        return immo_participations + immo_autres


class is_immobilisations_total_financieres_augmentation_nouveaux(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations financières, Augmentations Acquisitions, créations, apports et virements de poste à poste (LS)"

    def formula(person, period):
        immo_participations = person('is_immobilisations_financieres_participations_et_creances_participation_augmentation_nouveaux', period)
        immo_autres = person('is_immobilisations_financieres_prets_et_autres_augmentation_nouveaux', period)
        return immo_participations + immo_autres


class is_immobilisations_total_financieres_diminution_poste_a_poste(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations financières, Diminutions par virement de poste à poste (I3)"

    def formula(person, period):
        immo_participations = person('is_immobilisations_financieres_participations_et_creances_participation_diminution_poste_a_poste', period)
        immo_autres = person('is_immobilisations_financieres_prets_et_autres_diminution_poste_a_poste', period)
        return immo_participations + immo_autres


class is_immobilisations_total_financieres_diminution_cession_hors_services(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations financières, Diminutions par cession à des tiers ou mises hors services (NJ)"

    def formula(person, period):
        immo_participations = person('is_immobilisations_financieres_participations_et_creances_participation_diminution_cession_hors_services', period)
        immo_autres = person('is_immobilisations_financieres_prets_et_autres_diminution_cession_hors_services', period)
        return immo_participations + immo_autres


class is_immobilisations_total_financieres_brute_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations financières, Valeur brute des immobilisations à la fin de l'exercice (NK)"

    def formula(person, period):
        immo_participations = person('is_immobilisations_financieres_participations_et_creances_participation_brute_fin_exercice', period)
        immo_autres = person('is_immobilisations_financieres_prets_et_autres_brute_fin_exercice', period)
        return immo_participations + immo_autres


class is_immobilisations_total_financieres_origine_reevaluees_fin_exercice(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Total immobilisations financières, Valeur d'origine des immobilisations réévaluées en fin d'exercice (2H)"

    def formula(person, period):
        immo_participations = person('is_immobilisations_financieres_participations_et_creances_participation_origine_reevaluees_fin_exercice', period)
        immo_autres = person('is_immobilisations_financieres_prets_et_autres_origine_reevaluees_fin_exercice', period)
        return immo_participations + immo_autres
