# -*- coding: utf-8 -*-

from openfisca_pf.base import asarray, Enum


class Archipel(Enum):
    AUSTRALES = "Australes"
    GAMBIERS = "Gambiers"
    ILES_DU_VENT = "Îles du vent"
    ILES_SOUS_LE_VENT = "Îles sous le vent"
    MARQUISES = "Marquises"
    TUAMOTUS = "Tuamotus"


class CommuneFiscale(Enum):
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


COMMUNES_DES_AUSTRALES = CommuneFiscale.encode(asarray([
    CommuneFiscale.RAIVAVAE,
    CommuneFiscale.RAPA,
    CommuneFiscale.RIMATARA,
    CommuneFiscale.RURUTU,
    CommuneFiscale.TUBUAI
    ]))


COMMUNES_DES_GAMBIERS = CommuneFiscale.encode(asarray([
    CommuneFiscale.GAMBIER
    ]))


COMMUNES_DES_ILES_DU_VENT = CommuneFiscale.encode(asarray([
    CommuneFiscale.ARUE,
    CommuneFiscale.FAAA,
    CommuneFiscale.HITIAA_O_TE_RA,
    CommuneFiscale.MAHINA,
    CommuneFiscale.MOOREA_MAIAO,
    CommuneFiscale.PAEA,
    CommuneFiscale.PAPARA,
    CommuneFiscale.PAPEETE,
    CommuneFiscale.PIRAE,
    CommuneFiscale.PUNAAUIA,
    CommuneFiscale.TAIARAPU_EST,
    CommuneFiscale.TAIARAPU_OUEST,
    CommuneFiscale.TEVA_I_UTA
    ]))


COMMUNES_DES_ILES_SOUS_LE_VENT = CommuneFiscale.encode(asarray([
    CommuneFiscale.BORA_BORA,
    CommuneFiscale.HUAHINE,
    CommuneFiscale.MAUPITI,
    CommuneFiscale.TAHAA,
    CommuneFiscale.TAPUTAPUATEA,
    CommuneFiscale.TUMARAA,
    CommuneFiscale.UTUROA
    ]))


COMMUNES_DES_MARQUISES = CommuneFiscale.encode(asarray([
    CommuneFiscale.FATU_HIVA,
    CommuneFiscale.HIVA_OA,
    CommuneFiscale.NUKU_HIVA,
    CommuneFiscale.TAHUATA,
    CommuneFiscale.UA_HUKA,
    CommuneFiscale.UA_POU
    ]))


COMMUNES_DES_TUAMOTUS = CommuneFiscale.encode(asarray([
    CommuneFiscale.ANAA,
    CommuneFiscale.ARUTUA,
    CommuneFiscale.FAKARAVA,
    CommuneFiscale.FANGATAU,
    CommuneFiscale.HAO,
    CommuneFiscale.HIKUERU,
    CommuneFiscale.MAKEMO,
    CommuneFiscale.MANIHI,
    CommuneFiscale.NAPUKA,
    CommuneFiscale.NUKUTAVAKE,
    CommuneFiscale.PUKAPUKA,
    CommuneFiscale.RANGIROA,
    CommuneFiscale.REAO,
    CommuneFiscale.TAKAROA,
    CommuneFiscale.TATAKOTO,
    CommuneFiscale.TUREIA
    ]))
