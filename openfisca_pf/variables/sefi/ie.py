# -*- coding: utf-8 -*-


"""
L'indemnité d'éloignement (IE) est une aide financière offerte aux agents qui sont affectés en Polynésie française
pour servir en dehors du territoire dans lequel est situé leur centre de leurs intérêts matériels et moraux.

Le montant de l'indemnité est égal à 5 mois de traitement brut,
majoré de 5% par enfant à charge et de 10% pour le conjoint ne percevant pas d’indemnité d’éloignement.

Les demandes pour cette indemnité sont traitées par le SEFI (Service de l'emploi, de la formation et de l'insertion professionnelles).

Pour bénéficier de cette indemnité, l'agent doit fournir des pièces justificatives selon la composition familiale du bénéficiaire.
Le traitement de la liquidation de l'indemnité d'éloignement est échelonné selon un calendrier précis,
en fonction de la situation vis à vis du séjour règlementé des agents qui en bénéficient.

Il est important de noter que le délai de traitement des dossiers peut atteindre environ trois semaines
entre la transmission des états liquidatifs au comptable public
et le versement effectif de l’indemnité d’éloignement sur le compte bancaire des intéressés.
"""


from openfisca_pf.base import (
    ADD,
    ArrayLike,
    Enum,
    MONTH,
    not_,
    ParameterNode,
    Period,
    Population,
    round_,
    select,
    Variable,
    YEAR
    )
from openfisca_pf.constants.units import BOOLEAN, XPF_PER_MONTH
from openfisca_pf.entities import Personne
from openfisca_pf.enums.impots import TypeContrat


class dispositif_percu(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Est-ce que la personne à percu un dispositif d'aide ce mois ci ?"


class eligible_ie(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Indique si la personne est eligible à l'indemnité d'éloignement"
    reference = [
        'https://www.actusefi.org/ie2021',
        'https://pceco.squarespace.com/s/Loi-du-Pays-n-2021-12-du-24_02_2021.pdf',
        'https://www.actusefi.org/s/Arrete-n-209-CM-du-24_02_2021.pdf'
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        dispositif_percu = personne('dispositif_percu', period)
        en_activite = personne('en_activite_salariee', period)
        en_activite_mois_N_moins_1 = personne('en_activite_salariee', period.last_month)
        en_activite_mois_N_moins_2 = personne('en_activite_salariee', period.last_month.last_month)
        en_activite_mois_N_moins_3 = personne('en_activite_salariee', period.last_month.last_month.last_month)

        # Type de contrat des mois précédents
        contrat_mois_N_moins_1 = personne('type_contrat', period.last_month)
        contrat_mois_N_moins_2 = personne('type_contrat', period.last_month.last_month)
        contrat_mois_N_moins_3 = personne('type_contrat', period.last_month.last_month.last_month)

        # En fonction du type de contrat, l'IE est-il applicable
        applicabilite_ie_mois_N_moins_1 = parameters(period.last_month).sefi.ie.parametres.periodes[contrat_mois_N_moins_1]
        applicabilite_ie_mois_N_moins_2 = parameters(period.last_month.last_month).sefi.ie.parametres.periodes[contrat_mois_N_moins_2]
        applicabilite_ie_mois_N_moins_3 = parameters(period.last_month.last_month.last_month).sefi.ie.parametres.periodes[contrat_mois_N_moins_3]

        # On déterminer l'éligibilité pour chacun des 3 derniers mois
        eligibilite_ie_mois_N_moins_1 = en_activite_mois_N_moins_1 * applicabilite_ie_mois_N_moins_1
        eligibilite_ie_mois_N_moins_2 = en_activite_mois_N_moins_2 * applicabilite_ie_mois_N_moins_2
        eligibilite_ie_mois_N_moins_3 = en_activite_mois_N_moins_3 * applicabilite_ie_mois_N_moins_3

        return not_(dispositif_percu) \
            * not_(en_activite) \
            * (eligibilite_ie_mois_N_moins_1 + eligibilite_ie_mois_N_moins_2 + eligibilite_ie_mois_N_moins_3)


class eligible_ie_annee(Variable):
    entity = Personne
    definition_period = YEAR
    value_type = bool
    default_value = False
    unit = BOOLEAN
    label = "Indique si la personne est éligible à l'indemnité d'éloignement sur l'année en cours"
    reference = [
        'https://www.actusefi.org/ie2021',
        'https://pceco.squarespace.com/s/Loi-du-Pays-n-2021-12-du-24_02_2021.pdf',
        'https://www.actusefi.org/s/Arrete-n-209-CM-du-24_02_2021.pdf'
        ]

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        return personne('eligible_ie', period, options = [ADD])


class dernier_contrat_3_derniers_mois(Variable):
    value_type = Enum
    possible_values = TypeContrat
    default_value = TypeContrat.Aucun
    entity = Personne
    definition_period = MONTH
    label = 'Indique le type de contrat perdu lors des 3 derniers mois'

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        # Type de contrat des mois précédents
        contrat_mois_N_moins_1 = personne('type_contrat', period.last_month)
        contrat_mois_N_moins_2 = personne('type_contrat', period.last_month.last_month)
        contrat_mois_N_moins_3 = personne('type_contrat', period.last_month.last_month.last_month)
        return select(
            [
                contrat_mois_N_moins_1 != TypeContrat.Aucun,
                contrat_mois_N_moins_2 != TypeContrat.Aucun,
                contrat_mois_N_moins_3 != TypeContrat.Aucun
                ],
            [
                contrat_mois_N_moins_1,
                contrat_mois_N_moins_2,
                contrat_mois_N_moins_3
                ]
            )


class dernier_salaire_percu_3_derniers_mois(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = float
    default_value = 0.
    unit = XPF_PER_MONTH
    label = 'Indique le dernier salaire du ou des contrats perdus lors des 3 derniers mois'

    def formula(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        salaire_mois_N_moins_1 = personne('salaire', period.last_month)
        salaire_mois_N_moins_2 = personne('salaire', period.last_month.last_month)
        salaire_mois_N_moins_3 = personne('salaire', period.last_month.last_month.last_month)
        return select(
            [
                salaire_mois_N_moins_1 > 0,
                salaire_mois_N_moins_2 > 0,
                salaire_mois_N_moins_3 > 0
                ],
            [
                salaire_mois_N_moins_1,
                salaire_mois_N_moins_2,
                salaire_mois_N_moins_3
                ]
            )


class montant_ie(Variable):
    entity = Personne
    definition_period = MONTH
    value_type = float
    default_value = 0
    unit = XPF_PER_MONTH
    label = "Montant de l'indemnité d'éloignement ce mois ci"
    reference = [
        'https://www.actusefi.org/ie2021',
        'https://pceco.squarespace.com/s/Loi-du-Pays-n-2021-12-du-24_02_2021.pdf',
        'https://www.actusefi.org/s/Arrete-n-209-CM-du-24_02_2021.pdf'
        ]

    def formula_2021_01(personne: Population, period: Period, parameters: ParameterNode) -> ArrayLike:
        eligible_ie = personne('eligible_ie', period)
        dernier_contrat_3_derniers_mois = personne('dernier_contrat_3_derniers_mois', period)
        dernier_salaire_percu_3_derniers_mois = personne('dernier_salaire_percu_3_derniers_mois', period)
        montant_smig = parameters(period).sefi.smig.mensuel
        echelle_cdi = parameters(period).sefi.ie.tranche_si_salaire_cdi_superieur_smig
        echelle_cdd_ou_extras = parameters(period).sefi.ie.tranche_si_cdd_ou_extras
        montant_si_salaire_superieur_smig = echelle_cdi.calc((dernier_salaire_percu_3_derniers_mois - 1) / montant_smig)
        montant_si_salaire_cdi_egal_smig = parameters(period).sefi.ie.parametres.montant_si_salaire_cdi_egal_smig
        montant_si_salaire_inferieur_smig = round_(dernier_salaire_percu_3_derniers_mois * parameters(period).sefi.IE.parametres.taux_si_salaire_cdi_inferieur_smig)
        montant_si_cdi = select(
            [
                dernier_salaire_percu_3_derniers_mois < montant_smig,
                dernier_salaire_percu_3_derniers_mois == montant_smig,
                dernier_salaire_percu_3_derniers_mois > montant_smig
                ],
            [
                montant_si_salaire_inferieur_smig,
                montant_si_salaire_cdi_egal_smig,
                montant_si_salaire_superieur_smig
                ]
            )
        montant_si_cdd_ou_extras = echelle_cdd_ou_extras.calc(dernier_salaire_percu_3_derniers_mois)
        return eligible_ie * select(
            [
                dernier_contrat_3_derniers_mois == TypeContrat.CDI,
                dernier_contrat_3_derniers_mois != TypeContrat.CDI
                ],
            [
                montant_si_cdi,
                montant_si_cdd_ou_extras
                ]
            )
