# -*- coding: utf-8 -*-

import numpy
from openfisca_core.model_api import Enum


class Activite(Enum):
    NORMALE = "Normale"
    SOCIETES_MINIERES = "Sociétés minières"
    ETABLISSEMENTS_FINANCIERS_CREDIT_BAIL = "Établissement financiers et de crédit, sociétés de crédit-bail"
    ENERGIES_RENOUVELABLES = "Énergies renouvelables"
    SECTEUR_NUMERIQUE = "Activités du secteur numérique exclusivement"
    SECTEUR_RECHERCHE_DEVELOPPEMENT = "Activités du secteur de la recherche et de développement exclusivement"
    SOCIETES_EXPORTATRICES = "Exportation de biens corporels neufs et de services informatiques"
    CROISIERE_MIXTE = "Navigation maritime mixte"
    SOCIETES_GESTION_FONDS_GARANTIE = "Gestion de fonds de garantie - Sociétés commerciales de crédit"
    ACTIVITES_CROISIERE = "Croisière touristique en Polynésie française"
    HOTEL_RESIDENCE_INTERNATIONAL = "Hôtellerie ou résidence de tourisme internationale"
    CONCESSIONS_MINIERES = "Activités extractives sous concession minière"
    MEMBRE_GROUPE_FISCAL = "Membre groupe fiscal - Société fille"
    GIE = "Groupement d'intérêt économique"
    SCPR = "Société civile professionnelle"
    SCM = "Société civile de moyens"
    OBNL = "Organisme à but non lucratif"


ACTIVITE_TAUX_IS = Activite.encode(numpy.asarray([
    Activite.NORMALE,
    Activite.SOCIETES_MINIERES,
    Activite.ETABLISSEMENTS_FINANCIERS_CREDIT_BAIL,
    Activite.ENERGIES_RENOUVELABLES,
    Activite.SECTEUR_NUMERIQUE,
    Activite.SECTEUR_RECHERCHE_DEVELOPPEMENT
    ]))

ACTIVITE_ABATTEMENT_IS = Activite.encode(numpy.asarray([
    Activite.SOCIETES_GESTION_FONDS_GARANTIE
    ]))

ACTIVITE_ABATTEMENT_IMF = Activite.encode(numpy.asarray([
    Activite.SOCIETES_GESTION_FONDS_GARANTIE
    ]))

ACTIVITE_ABATTEMENT_CSIS = Activite.encode(numpy.asarray([
    ]))


ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_IS = Activite.encode(numpy.asarray([
    ]))

ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_IMF = Activite.encode(numpy.asarray([
    ]))

ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_CSIS = Activite.encode(numpy.asarray([
    ]))

ACTIVITE_REDUCTION_IS = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    Activite.CROISIERE_MIXTE,
    Activite.ACTIVITES_CROISIERE,
    Activite.CONCESSIONS_MINIERES,
    Activite.MEMBRE_GROUPE_FISCAL,
    Activite.GIE,
    Activite.SCPR,
    Activite.SCM,
    Activite.OBNL
    ]))

ACTIVITE_REDUCTION_IMF = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    Activite.CROISIERE_MIXTE,
    Activite.ACTIVITES_CROISIERE,
    Activite.CONCESSIONS_MINIERES,
    Activite.MEMBRE_GROUPE_FISCAL,
    Activite.GIE,
    Activite.SCPR,
    Activite.SCM,
    Activite.OBNL
    ]))

ACTIVITE_REDUCTION_CSIS = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    Activite.CROISIERE_MIXTE,
    Activite.ACTIVITES_CROISIERE,
    Activite.CONCESSIONS_MINIERES,
    Activite.MEMBRE_GROUPE_FISCAL,
    Activite.GIE,
    Activite.SCPR,
    Activite.SCM,
    Activite.OBNL
    ]))

ACTIVITE_REDUCTION_TAUX_A_SAISIR_IS = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    Activite.CROISIERE_MIXTE
    ]))


ACTIVITE_REDUCTION_TAUX_A_SAISIR_IMF = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    Activite.CROISIERE_MIXTE
    ]))

ACTIVITE_REDUCTION_TAUX_A_SAISIR_CSIS = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    Activite.CROISIERE_MIXTE
    ]))
