# Import the Entities specifically defined for this tax and benefit system
from openfisca_pf.base import (
    Variable,
    YEAR
    )
from openfisca_pf.entities import Personne

class is_bilan_passif_emprunts_et_dettes_aupres_des_etablissements_de_credit(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Emprunts et dettes auprès des établissements de crédit (DU)"


class is_bilan_passif_emprunts_et_dettes_financieres_diverses(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Emprunts et dettes financières diverses (DV)"


class is_bilan_passif_avances_et_acomptes_recus_sur_commandes_en_cours(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Avances et acomptes reçus sur commandes en cours (DW)"

class is_bilan_passif_dettes_fournisseurs_et_comptes_rattaches(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dettes fournisseurs et comptes rattachés (DX)"


class is_bilan_passif_dettes_fiscales_et_sociales(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dettes fiscales et sociales (DY)"


class is_bilan_passif_dettes_sur_immobilisations_et_comptes_rattaches(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Dettes sur immobilisations et comptes rattachés (DZ)"


class is_bilan_passif_autres_dettes(Variable):
    value_type = int
    entity = Personne
    definition_period = YEAR
    label = "Autres dettes (EA)"