# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *
from openfisca_pf.base import *

# class salaire(Variable):
#     value_type = float
#     entity = Personne
#     default_value = 0
#     definition_period = MONTH
#     set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
#     label = "Salaire"
#     reference = "https://law.gov.example/salary"  # Always use the most official source


class eligible_ie(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = MONTH
    # set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Salaire"
    reference = ["https://www.actusefi.org/ie2021", "https://pceco.squarespace.com/s/Loi-du-Pays-n-2021-12-du-24_02_2021.pdf", "https://www.actusefi.org/s/Arrete-n-209-CM-du-24_02_2021.pdf"]

    def formula(personne, period, parameters):

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
        applicabilite_ie_mois_N_moins_1 = parameters(period.last_month).sefi.IE.parametres.periodes[contrat_mois_N_moins_1]
        applicabilite_ie_mois_N_moins_2 = parameters(period.last_month.last_month).sefi.IE.parametres.periodes[contrat_mois_N_moins_2]
        applicabilite_ie_mois_N_moins_3 = parameters(period.last_month.last_month.last_month).sefi.IE.parametres.periodes[contrat_mois_N_moins_3]

        # On déterminer l'éligibilité pour chacun des 3 derniers mois
        eligibilite_ie_mois_N_moins_1 = en_activite_mois_N_moins_1 * applicabilite_ie_mois_N_moins_1
        eligibilite_ie_mois_N_moins_2 = en_activite_mois_N_moins_2 * applicabilite_ie_mois_N_moins_2
        eligibilite_ie_mois_N_moins_3 = en_activite_mois_N_moins_3 * applicabilite_ie_mois_N_moins_3

        # print(en_activite, en_activite_mois_N_moins_1, en_activite_mois_N_moins_2, en_activite_mois_N_moins_3)
        # print(contrat_mois_N_moins_1, contrat_mois_N_moins_2, contrat_mois_N_moins_3)
        # print(applicabilite_ie_mois_N_moins_1, applicabilite_ie_mois_N_moins_2, applicabilite_ie_mois_N_moins_3)
        # print(eligibilite_ie_mois_N_moins_1, eligibilite_ie_mois_N_moins_2, eligibilite_ie_mois_N_moins_3)
        # type_activite = select(
        #     [en_activite_mois_precedent],
        #     [0, ca - seuil_tranche_inferieure, seuil_tranche_superieure - seuil_tranche_inferieure],
        #     ))
        return not_(dispositif_percu) * not_(en_activite) * (eligibilite_ie_mois_N_moins_1 + eligibilite_ie_mois_N_moins_2 + eligibilite_ie_mois_N_moins_3)


class dernier_contrat_3_derniers_mois(Variable):
    value_type = Enum
    possible_values = TypeContrat
    default_value = TypeContrat.Aucun
    entity = Personne
    definition_period = MONTH
    label = "Indique le type de contrat perdu lors des 3 derniers mois"

    def formula(personne, period, parameters):
        # Type de contrat des mois précédents
        contrat_mois_N_moins_1 = personne('type_contrat', period.last_month)
        contrat_mois_N_moins_2 = personne('type_contrat', period.last_month.last_month)
        contrat_mois_N_moins_3 = personne('type_contrat', period.last_month.last_month.last_month)
        return select([contrat_mois_N_moins_1 != TypeContrat.Aucun, contrat_mois_N_moins_2 != TypeContrat.Aucun, contrat_mois_N_moins_3 != TypeContrat.Aucun],
        [contrat_mois_N_moins_1, contrat_mois_N_moins_2, contrat_mois_N_moins_3])


class dernier_salaire_percu_3_derniers_mois(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    label = "Salaire"

    def formula(personne, period, parameters):
        salaire_mois_N_moins_1 = personne('salaire', period.last_month)
        salaire_mois_N_moins_2 = personne('salaire', period.last_month.last_month)
        salaire_mois_N_moins_3 = personne('salaire', period.last_month.last_month.last_month)
        return select([salaire_mois_N_moins_1 != 0, salaire_mois_N_moins_2 != 0, salaire_mois_N_moins_3 != 0],
        [salaire_mois_N_moins_1, salaire_mois_N_moins_2, salaire_mois_N_moins_3])


class eligible_ie_annee(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = YEAR
    # set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Indique si la personne est éligible à l'IE sur l'année en cours"
    reference = ["https://www.actusefi.org/ie2021", "https://pceco.squarespace.com/s/Loi-du-Pays-n-2021-12-du-24_02_2021.pdf", "https://www.actusefi.org/s/Arrete-n-209-CM-du-24_02_2021.pdf"]

    def formula(personne, period, parameters):
        eligibilite_ie = personne('eligible_ie', period, options = [ADD])
        return eligibilite_ie


class dispositif_percu(Variable):
    value_type = bool
    entity = Personne
    default_value = False
    definition_period = MONTH
    label = "Indique si la personne a perçu un dispositif d'aide sur le mois"


class montant_ie(Variable):
    value_type = float
    entity = Personne
    default_value = 0
    definition_period = MONTH
    # set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Montant IE à verser"
    reference = ["https://www.actusefi.org/ie2021", "https://pceco.squarespace.com/s/Loi-du-Pays-n-2021-12-du-24_02_2021.pdf", "https://www.actusefi.org/s/Arrete-n-209-CM-du-24_02_2021.pdf"]

    def formula_2021_01(personne, period, parameters):
        eligible_ie = personne('eligible_ie', period)
        dernier_contrat_3_derniers_mois = personne('dernier_contrat_3_derniers_mois', period)
        dernier_salaire_percu_3_derniers_mois = personne('dernier_salaire_percu_3_derniers_mois', period)
        montant_smig = parameters(period).sefi.smig.mensuel
        echelle_cdi = parameters(period).sefi.IE.tranche_si_salaire_cdi_superieur_smig
        echelle_cdd_ou_extras = parameters(period).sefi.IE.tranche_si_cdd_ou_extras
        montant_si_salaire_superieur_smig = echelle_cdi.calc((dernier_salaire_percu_3_derniers_mois - 1) / montant_smig)
        montant_si_salaire_cdi_egal_smig = parameters(period).sefi.IE.parametres.montant_si_salaire_cdi_egal_smig
        montant_si_salaire_inferieur_smig = round_(dernier_salaire_percu_3_derniers_mois * parameters(period).sefi.IE.parametres.taux_si_salaire_cdi_inferieur_smig)
        montant_si_cdi = select(
            [dernier_salaire_percu_3_derniers_mois < montant_smig, dernier_salaire_percu_3_derniers_mois == montant_smig, dernier_salaire_percu_3_derniers_mois > montant_smig],
            [montant_si_salaire_inferieur_smig, montant_si_salaire_cdi_egal_smig, montant_si_salaire_superieur_smig]
            )
        montant_si_cdd_ou_extras = echelle_cdd_ou_extras.calc(dernier_salaire_percu_3_derniers_mois)
        return eligible_ie * select(
            [dernier_contrat_3_derniers_mois == TypeContrat.CDI, dernier_contrat_3_derniers_mois != TypeContrat.CDI],
            [montant_si_cdi, montant_si_cdd_ou_extras])
        # taux = personne('taux_cst_s_tranche_1', period)
        # cst_s_tranche = taux * where(revenus_tranche_inf_0, 0, salaires_tranche)
        # return arrondiSup(cst_s_tranche)

    def formula(personne, period, parameters):
        return 0
