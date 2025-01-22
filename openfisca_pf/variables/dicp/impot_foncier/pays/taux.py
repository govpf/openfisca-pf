# -*- coding: utf-8 -*-

from openfisca_pf.base import *
from openfisca_pf.entities import Pays
from openfisca_pf.enums.geographie import Archipel


class taux_archipel_australes_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.02
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Australes"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.archipel[Archipel.AUSTRALES.name]


class taux_archipel_gambiers_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.02
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et des archipels des Gambiers"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.archipel[Archipel.GAMBIERS.name]


class taux_archipel_iles_du_vent_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.04
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Îles du vent"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.archipel[Archipel.ILES_DU_VENT.name]


class taux_archipel_iles_sous_le_vent_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.03
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Îles sous le vent"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.archipel[Archipel.ILES_SOUS_LE_VENT.name]


class taux_archipel_marquises_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.02
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel des Marquises"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.archipel[Archipel.MARQUISES.name]


class taux_archipel_tuamotus_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.02
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et des archipels des Touamotus"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.archipel[Archipel.TUAMOTUS.name]


class taux_logement_social_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.02
    label = "Taux permettant de calculer la valeur locative direct d'un local utilisé comme logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.logement_social


class taux_meuble_de_tourisme_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.06
    label = "Taux permettant de calculer la valeur locative d'un local loué en meuble de tourisme en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.meuble_de_tourisme


class taux_villa_de_luxe_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.06
    label = "Taux permettant de calculer la valeur locative d'un local loué en villa de luxe en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.villa_de_luxe


class taux_part_pays_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la part pays de la contribution à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.pays


class taux_premier_abattement_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux du premier abattement appliqué à la valeur locative pour calculer la base imposable de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.abattement.premier


class taux_second_abattement_si_non_loue_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux du second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local n'est pas loué"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.abattement.second_si_non_loue


class taux_second_abattement_si_loue_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux du second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.abattement.second_si_loue_meuble


class taux_second_abattement_si_loue_non_meuble_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux du second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en non-meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.abattement.second_si_loue_non_meuble


class taux_degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0
    label = "Taux du dégrèvement sur demande dans le cas d'une baisse de revenus d'un local loué en meublé de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.degrevement.pour_baisse_de_revenus_loue_en_meuble_de_tourisme


class duree_premiere_exemption_temporaire_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 5
    label = "Nombre d'année d'exemption temporaire durant lequel les constructions nouvelles, reconstructions et additions de constructions ne sont pas soumises à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.exemption.duree_premiere_exemption_temporaire


class taux_premiere_exemption_temporaire_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 1.00
    label = "Taux de la première exemption temporaire pour lequel les constructions nouvelles, reconstructions et additions de constructions ne sont pas soumises à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.exemption.taux_premiere_exemption_temporaire


class duree_seconde_exemption_temporaire_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 3
    label = "Nombre d'année d'exemption temporaire durant lequel l'impôt foncier n'est établi que sur la moitié de la valeur locative de l'immeuble"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.exemption.duree_seconde_exemption_temporaire


class taux_seconde_exemption_temporaire_pays(Variable):
    value_type = float
    entity = Pays
    definition_period = YEAR
    default_value = 0.50
    label = "Taux de la seconde exemption temporaire pour lequel l'impôt foncier n'est établi que sur la moitié de la valeur locative de l'immeuble"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.exemption.taux_seconde_exemption_temporaire


class duree_exemption_temporaire_exceptionnelle_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 10
    label = "Nombre d'année d'exemption temporaire exceptionnelle durant lequel les constructions nouvelles, reconstructions et additions de constructions ne sont pas soumises à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.exemption.duree_exemption_temporaire_exceptionnelle


class date_minimum_permis_construire_pour_exemption_temporaire_exceptionnelle_pays(Variable):
    value_type = date
    entity = Pays
    definition_period = YEAR
    default_value = date(2023, 1, 1)
    label = "Date minimum du permis de construire pour lequel le contribuable peut d'accéder à l'exemption temporaire exceptionnelle"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022(pays, period, parameters):
        return date(2023, 1, 1)


class date_maximum_certificat_conformite_pour_exemption_temporaire_exceptionnelle_pays(Variable):
    value_type = date
    entity = Pays
    definition_period = YEAR
    default_value = date(2025, 12, 31)
    label = "Date maximum du certificat de conformité pour lequel le contribuable peut d'accéder à l'exemption temporaire exceptionnelle"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula_2022(pays, period, parameters):
        return date(2025, 12, 31)


class valeur_venale_maximum_pour_exemption_permanente_pays(Variable):
    value_type = int
    entity = Pays
    definition_period = YEAR
    default_value = 500000
    label = "Valeur venale maximum pour obtenir l'exemption permanente de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(pays, period, parameters):
        return parameters(period).dicp.impot_foncier.taux.exemption.valeur_venale_maximum_pour_exemption_permanente
