from openfisca_core.model_api import Enum


class FormeJuridiqueExoneration(Enum):
    GIE = "Groupement d'intérêt économique"
    SCPR = "Société civile professionnelle"
    SCM = "Société civile de moyens"
    OBNL = "Organisme à but non lucratif"
