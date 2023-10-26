# -*- coding: utf-8 -*-

import numpy
from openfisca_core.indexed_enums import EnumArray
from openfisca_core.model_api import Enum


class Archipel(Enum):
    AUSTRALES = "Australes"
    ILES_DU_VENT = "Îles du vent"
    ILES_SOUS_LE_VENT = "Îles sous le vent"
    MARQUISES = "Marquises"
    TUAMOTUS_ET_GAMBIERS = "Tuamotus et Gambiers"


class Commune(Enum):
    ANAA = "Anaa"
    ARUE = "Arue"
    ARUTUA = "Arutua"
    BORA_BORA = "Bora-Bora"
    FAAA = "Faaa"
    FAKARAVA = "Fakarava"
    FANGATAU = "Fangatau"
    FATU_HIVA = "Fatu Hiva"
    GAMBIER = "Gambier"
    HAO = "Hao"
    HIKUERU = "Hikueru"
    HITIAA_O_TE_RA = "Hitiaa O Te Ra"
    HIVA_OA = "Hiva Oa"
    HUAHINE = "Huahine"
    MAHINA = "Mahina"
    MAKEMO = "Makemo"
    MANIHI = "Manihi"
    MAUPITI = "Maupiti"
    MOOREA_MAIAO = "Moorea Maiao"
    NAPUKA = "Napuka"
    NUKU_HIVA = "Nuku Hiva"
    NUKUTAVAKE = "Nukutavake"
    PAEA = "Paea"
    PAPARA = "Papara"
    PAPEETE = "Papeete"
    PIRAE = "Pirae"
    PUKAPUKA = "Pukapuka"
    PUNAAUIA = "Puna'auia"
    RAIVAVAE = "Raivavae"
    RANGIROA = "Rangiroa"
    RAPA = "Rapa"
    REAO = "Reao"
    RIMATARA = "Rimatara"
    RURUTU = "Rurutu"
    TAHAA = "Tahaa"
    TAHUATA = "Tahuata"
    TAIARAPU_EST = "Taiarapu Est"
    TAIARAPU_OUEST = "Taiarapu Ouest"
    TAKAROA = "Takaroa"
    TAPUTAPUATEA = "Taputapuatea"
    TATAKOTO = "Tatakoto"
    TEVA_I_UTA = "Teva I Uta"
    TUBUAI = "Tubuai"
    TUMARAA = "Tamaraa"
    TUREIA = "Tureia"
    UA_HUKA = "Ua Huka"
    UA_POU = "Ua Pou"
    UTUROA = "Uturoa"


COMMUNES_DES_AUSTRALES = Commune.encode(numpy.asarray([
    Commune.RAIVAVAE,
    Commune.RAPA,
    Commune.RIMATARA,
    Commune.RURUTU,
    Commune.TUBUAI
    ]))

COMMUNES_DES_ILES_DU_VENT = Commune.encode(numpy.asarray([
    Commune.ARUE,
    Commune.FAAA,
    Commune.HITIAA_O_TE_RA,
    Commune.MAHINA,
    Commune.MOOREA_MAIAO,
    Commune.PAEA,
    Commune.PAPARA,
    Commune.PAPEETE,
    Commune.PIRAE,
    Commune.PUNAAUIA,
    Commune.TAIARAPU_EST,
    Commune.TAIARAPU_OUEST,
    Commune.TEVA_I_UTA
    ]))

COMMUNES_DES_ILES_SOUS_LE_VENT = Commune.encode(numpy.asarray([
    Commune.BORA_BORA,
    Commune.HUAHINE,
    Commune.MAUPITI,
    Commune.TAHAA,
    Commune.TAPUTAPUATEA,
    Commune.TUMARAA,
    Commune.UTUROA
    ]))

COMMUNES_DES_MARQUISES = Commune.encode(numpy.asarray([
    Commune.FATU_HIVA,
    Commune.HIVA_OA,
    Commune.NUKU_HIVA,
    Commune.TAHUATA,
    Commune.UA_HUKA,
    Commune.UA_POU
    ]))

COMMUNES_DES_TUAMOTUS_ET_DES_GAMBIERS = Commune.encode(numpy.asarray([
    Commune.ANAA,
    Commune.ARUTUA,
    Commune.FAKARAVA,
    Commune.FANGATAU,
    Commune.GAMBIER,
    Commune.HAO,
    Commune.HIKUERU,
    Commune.MAKEMO,
    Commune.MANIHI,
    Commune.NAPUKA,
    Commune.NUKUTAVAKE,
    Commune.PUKAPUKA,
    Commune.RANGIROA,
    Commune.REAO,
    Commune.TAKAROA,
    Commune.TATAKOTO,
    Commune.TUREIA
    ]))