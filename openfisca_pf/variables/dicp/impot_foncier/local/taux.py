# -*- coding: utf-8 -*-

from openfisca_core.periods import Period

from openfisca_pf.base import *
from openfisca_pf.entities import Personne
from openfisca_pf.enums.geographie import Archipel


class taux_archipel(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la valeur locative direct en fonction de la valeur venale et de l'archipel du local"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        archipel = local('archipel', period, parameters)
        taux_archipel_australes_pays = local.pays('taux_archipel_australes_pays', period, parameters)
        taux_archipel_gambiers_pays = local.pays('taux_archipel_gambiers_pays', period, parameters)
        taux_archipel_iles_du_vent_pays = local.pays('taux_archipel_iles_du_vent_pays', period, parameters)
        taux_archipel_iles_sous_le_vent_pays = local.pays('taux_archipel_iles_sous_le_vent_pays', period, parameters)
        taux_archipel_marquises_pays = local.pays('taux_archipel_marquises_pays', period, parameters)
        taux_archipel_tuamotus_pays = local.pays('taux_archipel_tuamotus_pays', period, parameters)
        return numpy.select(
            [
                archipel == Archipel.AUSTRALES,
                archipel == Archipel.GAMBIERS,
                archipel == Archipel.ILES_DU_VENT,
                archipel == Archipel.ILES_SOUS_LE_VENT,
                archipel == Archipel.MARQUISES,
                archipel == Archipel.TUAMOTUS
                ],
            [
                taux_archipel_australes_pays,
                taux_archipel_gambiers_pays,
                taux_archipel_iles_du_vent_pays,
                taux_archipel_iles_sous_le_vent_pays,
                taux_archipel_marquises_pays,
                taux_archipel_tuamotus_pays
                ])


class taux_logement_social(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.02
    label = "Taux permettant de calculer la valeur locative direct d'un local utilisé comme logement social"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        return local.pays('taux_logement_social_pays', period, parameters)


class taux_meuble_de_tourisme(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.06
    label = "Taux permettant de calculer la valeur locative d'un local loué en meuble de tourisme en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters):
        return local.pays('taux_meuble_de_tourisme_pays', period, parameters)


class taux_villa_de_luxe(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.06
    label = "Taux permettant de calculer la valeur locative d'un local loué en villa de luxe en fonction de sa valeur vénale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        return local.pays('taux_villa_de_luxe_pays', period, parameters)


class taux_part_pays(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux permettant de calculer la part pays de la contribution à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        return local.pays('taux_part_pays_pays', period, parameters)


class taux_part_commune_fiscale(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux utilisé pour calculer la contribution foncière allant à la commune fiscale"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        commune_fiscale = local('commune_fiscale', period, parameters)
        return parameters(period).dicp.impot_foncier.taux.commune_fiscale[commune_fiscale]


class taux_premier_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux du premier abattement appliqué à la valeur locative pour calculer la base imposable de l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_premier_abattement_pays', period, parameters)


class taux_second_abattement_si_non_loue(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux du second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local n'est pas loué"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_second_abattement_si_non_loue_pays', period, parameters)


class taux_second_abattement_si_loue_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux du second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_second_abattement_si_loue_meuble_pays', period, parameters)


class taux_second_abattement_si_loue_non_meuble(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux du second abattement appliqué pour calculer la base imposable de l'impôt foncier si le local est loué en non-meublé"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_second_abattement_si_loue_non_meuble_pays', period, parameters)


class taux_second_abattement(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux du second abattement appliqué pour calculer la base imposable de l'impôt foncier en fonction de sa situation"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):

        loue = local('loue', period, parameters)
        meuble = local('meuble', period, parameters)
        non_meuble = local('non_meuble', period, parameters)
        taux_second_abattement_si_non_loue = local('taux_second_abattement_si_non_loue', period, parameters)
        taux_second_abattement_si_loue_meuble = local('taux_second_abattement_si_loue_meuble', period, parameters)
        taux_second_abattement_si_loue_non_meuble = local('taux_second_abattement_si_loue_non_meuble', period, parameters)
        return numpy.select(
            [loue and meuble, loue and non_meuble],
            [taux_second_abattement_si_loue_meuble, taux_second_abattement_si_loue_non_meuble],
            taux_second_abattement_si_non_loue
            )


class taux_premiere_exemption_temporaire(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 1.00
    label = "Taux de la première exemption temporaire pour lequel les constructions nouvelles, reconstructions et additions de constructions ne sont pas soumises à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_premiere_exemption_temporaire_pays', period, parameters)


class taux_seconde_exemption_temporaire(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0.50
    label = "Taux de la seconde exemption temporaire pour lequel l'impôt foncier n'est établi que sur la moitié de la valeur locative de l'immeuble"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        return local.pays('taux_seconde_exemption_temporaire_pays', period, parameters)


class taux_degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Dégrèvement sur demande dans le cas d'une baisse de revenus d'un local loué en meublé de tourisme"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local, period, parameters):
        taux_degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme_pays = local.pays('taux_degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme_pays', period, parameters)
        meuble_de_tourisme_est_eligible_et_demande_un_degrevement = local('meuble_de_tourisme_est_eligible_et_demande_un_degrevement', period, parameters)
        return numpy.where(meuble_de_tourisme_est_eligible_et_demande_un_degrevement, taux_degrevement_pour_baisse_de_revenus_loue_en_meuble_de_tourisme_pays, 0)


class acces_exemption_temporaire_exceptionnelle(Variable):
    value_type = bool
    entity = Personne
    definition_period = YEAR
    default_value = False
    label = "True si les conditions sont remplis afin d'obtenir l'exemption temporaire exceptionnelle, sinon False."
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        date_certificat_conformite = local('date_certificat_conformite', period, parameters)
        date_permis_construire = local('date_permis_construire', period, parameters)
        duree_premiere_exemption_temporaire_exceptionnelle_pays = local.pays('duree_premiere_exemption_temporaire_exceptionnelle_pays', period, parameters)

        annee_depuis_date_certificat_conformite = period.date.year - (date_certificat_conformite.astype('datetime64[Y]').astype(int) + 1970)
        date_minimum_permis_construire = date(2022, 12, 31)
        date_maximum_certificat_conformite = date(2025, 12, 31)

        return numpy.select([
            date_permis_construire > date_minimum_permis_construire
            and date_certificat_conformite < date_maximum_certificat_conformite
            and annee_depuis_date_certificat_conformite <= duree_premiere_exemption_temporaire_exceptionnelle_pays
        ], [
            True
        ], False)


class taux_exemption_temporaire(Variable):
    value_type = float
    entity = Personne
    definition_period = YEAR
    default_value = 0
    label = "Taux de l'exemption temporaire pour lequel les constructions sont soumises à l'impôt foncier"
    reference = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595"

    def formula(local: Personne, period: Period, parameters: Parameter):
        acces_exemption_temporaire_exceptionnelle = local('acces_exemption_temporaire_exceptionnelle', period, parameters)
        demande_exemption_temporaire_exceptionnelle = local('demande_exemption_temporaire_exceptionnelle', period, parameters)
        date_certificat_conformite = local('date_certificat_conformite', period, parameters)
        duree_premiere_exemption_temporaire_pays = local.pays('duree_premiere_exemption_temporaire_pays', period, parameters)
        taux_premiere_exemption_temporaire = local('taux_premiere_exemption_temporaire', period, parameters)
        duree_seconde_exemption_temporaire_pays = local.pays('duree_seconde_exemption_temporaire_pays', period, parameters)
        taux_seconde_exemption_temporaire = local('taux_seconde_exemption_temporaire', period, parameters)

        annee_depuis_date_certificat_conformite = period.date.year - (date_certificat_conformite.astype('datetime64[Y]').astype(int) + 1970)

        return numpy.select([
            demande_exemption_temporaire_exceptionnelle and acces_exemption_temporaire_exceptionnelle,
            annee_depuis_date_certificat_conformite <= duree_premiere_exemption_temporaire_pays,
            duree_premiere_exemption_temporaire_pays < annee_depuis_date_certificat_conformite <= (duree_premiere_exemption_temporaire_pays + duree_seconde_exemption_temporaire_pays)
        ],[
            taux_premiere_exemption_temporaire,
            taux_premiere_exemption_temporaire,
            taux_seconde_exemption_temporaire
        ], 0)
