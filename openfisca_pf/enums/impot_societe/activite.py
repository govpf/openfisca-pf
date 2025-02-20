from openfisca_core.model_api import Enum


class ActiviteTauxIS(Enum):
    NORMALE = "Normale"
    SOCIETES_MINIERES = "Sociétés minières"
    ETABLISSEMENTS_FINANCIERS_CREDIT_BAIL = "Établissement financiers et de crédit, sociétés de crédit-bail"
    ENERGIES_RENOUVELABLES = "Énergies renouvelables"
    SECTEUR_NUMERIQUE = "Activités du secteur numérique exclusivement"
    SECTEUR_RECHERCHE_DEVELOPPEMENT = "Activités du secteur de la recherche et de développement exclusivement"
    ZONE_REVITALISATION_ZRAE = "Siège social dans une zone de revitalisation des activités économiques (ZRAE)"


class ActiviteExoneratrice(Enum):
    SOCIETES_EXPORTATRICES = "Exportation de biens corporels neufs et de services informatiques"
    CROISIERE_MIXTE = "Navigation maritime mixte"
    SOCIETES_GESTION_FONDS_GARANTIE = "Gestion de fonds de garantie - Sociétés commerciales de crédit"
    ACTIVITES_CROISIERE = "Croisière touristique en Polynésie française"
    HOTEL_RESIDENCE_INTERNATIONAL = "Hôtellerie ou résidence de tourisme internationale"
    CONCESSIONS_MINIERES = "Activités extractives sous concession minière"
    MEMBRE_GROUPE_FISCAL = "Membre groupe fiscal - Société fille"
