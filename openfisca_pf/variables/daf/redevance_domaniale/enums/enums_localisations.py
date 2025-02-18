# -*- coding: utf-8 -*-

from openfisca_core.model_api import Enum


class Commune(Enum):
    # Code commune associée des communes de Polynésie Française
    com111 = u'ANAA'
    com112 = u'FAAITE'
    com120 = u'ARUE'
    com132 = u'ARUTUA'
    com131 = u'APATAKI'
    com133 = u'KAUKURA'
    com141 = u'ANAU'
    com142 = u'FAANUI'
    com143 = u'NUNUE'
    com150 = u'FAAA'
    com161 = u'FAKARAVA'
    com162 = u'KAUEHI'
    com163 = u'NIAU'
    com172 = u'FANGATAU'
    com171 = u'FAKAHINA'
    com180 = u'FATU-HIVA'
    com190 = u'GAMBIER'
    com202 = u'HAO'
    com201 = u'AMANU'
    com203 = u'HEREHERETUE'
    com211 = u'HIKUERU'
    com212 = u'MAROKAU'
    com221 = u'HITIAA'
    com222 = u'MAHAENA'
    com223 = u'PAPENOO'
    com224 = u'TIAREI'
    com231 = u'ATUONA'
    com232 = u'PUAMAU'
    com241 = u'FAIE'
    com242 = u'FARE'
    com243 = u'FITII'
    com244 = u'HAAPU'
    com245 = u'MAEVA'
    com246 = u'MAROE'
    com247 = u'PAREA'
    com248 = u'TEFARERII'
    com250 = u'MAHINA'
    com262 = u'MAKEMO'
    com261 = u'KATIU'
    com263 = u'RAROIA'
    com264 = u'TAENGA'
    com272 = u'MANIHI'
    com271 = u'AHE'
    com280 = u'MAUPITI'
    com291 = u'AFAREAITU'
    com292 = u'HAAPITI'
    com293 = u'MAIAO'
    com294 = u'PAOPAO'
    com295 = u'PAPETOAI'
    com296 = u'TEAVARO'
    com301 = u'NAPUKA'
    com302 = u'TEPOTO-NORD'
    com311 = u'HATIHEU'
    com312 = u'TAIOHAE'
    com313 = u'TAIPIVAI'
    com321 = u'NUKUTAVAKE'
    com322 = u'VAHITAHI'
    com323 = u'VAIRAATEA'
    com330 = u'PAEA'
    com340 = u'PAPARA'
    com350 = u'PAPEETE'
    com360 = u'PIRAE'
    com370 = u'PUKAPUKA'
    com380 = u'PUNAAUIA'
    com391 = u'ANATONU'
    com392 = u'RAIRUA-MAHANATOA'
    com393 = u'VAIURU'
    com403 = u'RANGIROA'
    com401 = u'MAKATEA'
    com402 = u'MATAIVA'
    com404 = u'TIKEHAU'
    com410 = u'RAPA'
    com422 = u'REAO'
    com421 = u'PUKARUA'
    com431 = u'AMARU'
    com432 = u'ANAPOTO'
    com433 = u'MUTUAURA'
    com441 = u'AVERA (RURUTU)'
    com442 = u'HAUTI'
    com443 = u'MOERAI'
    com451 = u'FAAAHA'
    com452 = u'HAAMENE'
    com453 = u'HIPU'
    com454 = u'IRIPAU'
    com455 = u'NIUA'
    com456 = u'RUUTIA'
    com457 = u'TAPUAMU'
    com458 = u'VAITOARE'
    com460 = u'TAHUATA'
    com471 = u'AFAAHITI'
    com472 = u'FAAONE'
    com473 = u'PUEU'
    com474 = u'TAUTIRA'
    com481 = u'TEAHUPOO'
    com482 = u'TOAHOTU'
    com483 = u'VAIRAO'
    com492 = u'TAKAROA'
    com491 = u'TAKAPOTO'
    com501 = u'AVERA (RAIATEA)'
    com502 = u'OPOA'
    com503 = u'PUOHINE'
    com510 = u'TATAKOTO'
    com521 = u'MATAIEA'
    com522 = u'PAPEARI'
    com531 = u'MAHU'
    com532 = u'MATAURA'
    com533 = u'TAAHUAIA'
    com541 = u'FETUNA'
    com542 = u'TEHURUI'
    com543 = u'TEVAITOA'
    com544 = u'VAIAAU'
    com550 = u'TUREIA'
    com560 = u'UA-HUKA'
    com571 = u'HAKAHAU'
    com572 = u'HAKAMAII'
    com580 = u'UTUROA'


class ZoneDomPrive(Enum):
    # Ensemble des noms de zones de l arrêté 136CM
    village = u'Village'
    secteur = u'Secteur'
    zone_de_base = u'Zone de base'
    zone_bord_de_mer = u'Zone bord de mer'
    zone_cote_mer = u'Zone cote mer'
    zone_plaines_et_basses_montagnes = u'Zone plaines et basses montagnes'
    zone_moyennes_montagnes = u'Zone moyennes montagnes'
    zone_rurale = u'Zone rurale'
    zone_touristique = u'Zone touristique'
    motu = u'Motu'
    centre_ville = u'Centre-ville'
    zone_hautes_montagnes = u'Zone hautes montagnes'
    tetamanu = u'TETAMANU'
    village_zone_rurale = u'Village (zone rurale)'
    zone_montagne = u'Zone montagne'
    zone_habitation = u'Zone d\'habitation'
    zone_habitat = u'Zone d\'habitat'
    zone_agricole_motu = u'Zone agricole motu'
    zone_montagneuse = u'Zone montagneuse'
    bord_de_mer = u'Bord de mer'
    cote_montagne = u'Cote montagne'
    domaine_opunohu = u'Domaine Opunohu'
    vaiare_bord_de_mer = u'Vaiare Bord de mer'
    vaiare_cote_montagne = u'Vaiare Cote montagne'
    temae_bord_de_mer = u'Temae Bord de mer'
    temae_cote_montagne = u'Temae Cote montagne'
    temae_bel_air = u'Temae Residence Bel Air'
    taunoa_zone_urbaine = u'Taunoa - Zone urbaine à forte densite de population'
    taunoa_zone_bord_de_mer = u'Taunoa - Zone bord de mer'
    mamao_zone_commercial = u'Mamao - Zone commercial et d\'habitat'
    titioro_zone_industrielle_et_commerciale = u'Titioro - Zone industrielle et commerciale'
    titioro_zone_habitat = u'Titioro - Zone habitat'
    paofai_zone_plaine = u'Paofai - Zone commerciale (plaine)'
    paofai_zone_montagne = u'Paofai - Zone d\'habitat (montagne)'
    sainte_amelie_zone_habitat = u'Sainte Amelie - Zone d’habitat'
    sainte_amelie_quartier_des_institutions = u'Sainte Amelie - Quartier des institutions (quartier broche)'
    tipaerui_zone_industrielle_et_commerciale = u'Tipaerui - Zone industrielle et commerciale'
    tipaerui_zone_residentielle = u'Tipaerui - Zone residentielle'
    tipaerui_zone_sociale = u'Tipaerui - Zone sociale'
    motu_et_bord_de_mer = u'Motu et bord de mer'
    zone_habitat_village = u'Zone d\'habitat village'
    zone_rurale_montagneuse = u'Zone rurale montagneuse'
    zone_rurale_plaine = u'Zone rurale plaine'
    village_hors_bord_de_mer = u'Village (hors bord de mer)'
    bord_de_mer_et_bord_de_route = u'Bord de mer et bord de route'
    bord_de_route = u'Bord de route'
    zone_de_lotissement = u'Zone de lotissement'
    zone_hors_lotissement = u'Zone hors lotissement'


class ZoneLotAgricole(Enum):
    # Ensemble des lotissements agricoles
    amo = u'AMO'
    atimaono_1 = u'ATIMAONO 1'
    atimaono_2 = u'ATIMAONO 2'
    marumarutua_1_15 = u'MARUMARUTUA - Lot 1 à 15'
    marumarutua_16_22 = u'MARUMARUTUA - Lot 16 à 22'
    plateau_taravao_1_6 = u'PLATEAU TARAVAO - Lot 1 à 6'
    plateau_taravao_7_20 = u'PLATEAU TARAVAO - Lot 7 à 20'
    plateau_taravao_extension = u'PLATEAU TARAVAO EXTENSION'
    plateau_taravao_extension_2 = u'PLATEAU TARAVAO EXTENSION 2'
    rose = u'ROSE'
    socredo_1 = u'SOCREDO - à mettre à jour'
    socredo_2_4 = u'SOCREDO - Lot 2, 3, 4'
    vaitepiha = u'VAITEPIHA'
    opunohu = u'OPUNOHU'
    opunohu_rive_gauche = u'OPUNOHU RIVE GAUCHE'
    rotui = u'ROTUI'
    vaianae = u'VAIANAE'
    opoa = u'OPOA'
    faaroa_agri = u'FAAROA - lots à des fins agricoles'
    faaroa_elevage = u'FAAROA - 143b, 199, 200 et 201 (lots à des fins d\'élevage)'
    maraeroa = u'MARAEROA'
    tarodiere_opoa = u'TARODIERE OPOA'
    bachelier = u'BACHELIER'
    hamoa = u'HAMOA'
    faahue = u'FAAHUE'
    matavahi_1 = u'MATAVAHI 1'
    matavahi_2 = u'MATAVAHI 2'
    metuarii = u'METUARII'
    atai = u'ATAI'
    terre_deserte = u'TERRE DESERTE'
    taipivai = u'TAIPIVAI'
    hiniaehi = u'HINIAEHI'
