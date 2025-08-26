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


ACTIVITE_TAUX_IS = numpy.asarray([
    Activite.NORMALE,
    Activite.SOCIETES_MINIERES,
    Activite.ETABLISSEMENTS_FINANCIERS_CREDIT_BAIL,
    Activite.ENERGIES_RENOUVELABLES,
    Activite.SECTEUR_NUMERIQUE,
    Activite.SECTEUR_RECHERCHE_DEVELOPPEMENT
    ])

ACTIVITE_TAUX_IS_ENCODEE = Activite.encode(ACTIVITE_TAUX_IS)

ActiviteTauxIS = Enum(
    'ActiviteTauxIS',
    {act.name: act.value for act in ACTIVITE_TAUX_IS}
    )

ACTIVITE_ABATTEMENT_IS = numpy.asarray([Activite.SOCIETES_GESTION_FONDS_GARANTIE])

ActiviteAbattementIS = Enum(
    'ActiviteAbattementIS',
    {act.name: act.value for act in ACTIVITE_ABATTEMENT_IS}
    )

ACTIVITE_ABATTEMENT_IS_ENCODEE = Activite.encode(ACTIVITE_ABATTEMENT_IS)

ACTIVITE_ABATTEMENT_IMF_ENCODEE = Activite.encode(numpy.asarray([
    Activite.SOCIETES_GESTION_FONDS_GARANTIE
    ]))

ACTIVITE_ABATTEMENT_CSIS_ENCODEE = Activite.encode(numpy.asarray([
    ]))


ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_IS_ENCODEE = Activite.encode(numpy.asarray([
    ]))

ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_IMF_ENCODEE = Activite.encode(numpy.asarray([
    ]))

ACTIVITE_ABATTEMENT_TAUX_A_SAISIR_CSIS_ENCODEE = Activite.encode(numpy.asarray([
    ]))


ACTIVITE_REDUCTION_IS = numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    Activite.CROISIERE_MIXTE,
    Activite.ACTIVITES_CROISIERE,
    Activite.CONCESSIONS_MINIERES,
    Activite.MEMBRE_GROUPE_FISCAL,
    Activite.GIE,
    Activite.SCPR,
    Activite.SCM,
    Activite.OBNL
    ])

ActiviteReductionIS = Enum(
    'ActiviteReductionIS',
    {act.name: act.value for act in ACTIVITE_REDUCTION_IS}
    )

ACTIVITE_REDUCTION_IS_ENCODEE = Activite.encode(ACTIVITE_REDUCTION_IS)

ACTIVITE_REDUCTION_IMF_ENCODEE = Activite.encode(numpy.asarray([
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

ACTIVITE_REDUCTION_CSIS_ENCODEE = Activite.encode(numpy.asarray([
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

ACTIVITE_REDUCTION_TAUX_A_SAISIR_IS_ENCODEE = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    ]))


ACTIVITE_REDUCTION_TAUX_A_SAISIR_IMF_ENCODEE = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    ]))

ACTIVITE_REDUCTION_TAUX_A_SAISIR_CSIS_ENCODEE = Activite.encode(numpy.asarray([
    Activite.SOCIETES_EXPORTATRICES,
    ]))
