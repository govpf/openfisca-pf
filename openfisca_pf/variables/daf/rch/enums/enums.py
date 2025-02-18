# -*- coding: utf-8 -*-

# This file defines variables for the modelled legislation.
# A variable is a property of an Entity such as a Person, a Household…
# See https://openfisca.org/doc/key-concepts/variables.html

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# # Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.entities import *


class TypeDemarche(Enum):
    DonsMeubles = u'Don manuel de biens meubles'
    Baux = u'Baux en régime normal'
    Acquisition = u'Acquisition ou vente'
    PlusValuesImmobiliere = u'Plus-values immobilières'
    Navire = u'Cession de navire'


class TypeAcheteur(Enum):
    PrimoAcquereur = u'Primo_acquéreur'
    DroitCommun = u'Acquéreur de droit commun'


class TypeBien(Enum):
    TerrainNu = u'Terrain Nu'
    TerrainBati = u'Terrain bâti'
    Appartement = u'Appartement'


class TypeParente(Enum):
    LigneDirecte = u'Mutations en ligne directe (époux/concubins, frères et soeurs)'
    ParentCollateral = u'Parents en ligne collatérale de 3eme degré'
    NonParent = u'Non parents et parents en ligne collatérale à partir du 4eme degré'
