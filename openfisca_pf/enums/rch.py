# -*- coding: utf-8 -*-


"""
La Direction des Affaires Foncières (DAF) de la Polynésie française gère la section Recette-Conservation des Hypothèques (RCH),
qui a pour mission de conserver les registres fonciers, délivrer les titres de propriété, liquider et percevoir les droits relatifs,
accomplir les formalités civiles pour la conservation des hypothèques et la consolidation des mutations de propriétés immobilières,
délivrer des états et certificats, liquider et percevoir les droits d'enregistrement, les baux, et les redevances domaniales.
"""


from openfisca_pf.base import Enum


__all__ = [
    'TypeAcheteur',
    'TypeBien',
    'TypeDemarche',
    'TypeParente'
    ]


class TypeAcheteur(Enum):
    PrimoAcquereur = 'Primo_acquéreur'
    DroitCommun = 'Acquéreur de droit commun'


class TypeBien(Enum):
    TerrainNu = 'Terrain Nu'
    TerrainBati = 'Terrain bâti'
    Appartement = 'Appartement'


class TypeDemarche(Enum):
    DonsMeubles = 'Don manuel de biens meubles'
    Baux = 'Baux en régime normal'
    Acquisition = 'Acquisition ou vente'
    PlusValuesImmobiliere = 'Plus-values immobilières'
    Navire = 'Cession de navire'


class TypeParente(Enum):
    LigneDirecte = 'Mutations en ligne directe (époux/concubins, frères et soeurs)'
    ParentCollateral = 'Parents en ligne collatérale de 3eme degré'
    NonParent = 'Non parents et parents en ligne collatérale à partir du 4eme degré'
