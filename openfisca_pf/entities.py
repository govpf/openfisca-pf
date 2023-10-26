# -*- coding: utf-8 -*-

from openfisca_core.entities import build_entity

Dossier = build_entity(
    key = "dossier",
    plural = "dossiers",
    label = u'Un dossier',
    doc = "Un dossier regroupe plusieurs demandes, représentés dans openfisca par plusieurs personnes",
    roles = [
        {
            "key": "demande",
            "plural": "demandes",
            "label": "Demandes",
            "doc": "Les demandes du dossier"
        }
    ]
)

Employes = build_entity(
    key = "employes",
    plural = "employes",
    label = "Un groupe d'employés",
    doc = "",
    roles = [
        {
            "key": "Employe",
            "plural": "employes",
            "label": "Employés",
            "doc": "La liste des employés"
        }
    ]
)

Personne = build_entity(
    key = "personne",
    plural = "personnes",
    label = "Une personne physique ou morale",
    is_person = True,
)

Pays = build_entity(
    key = "pays",
    plural = "pays",
    label = "Le pays",
    doc = "",
    roles = [
        {
            "key": "Contribuables",
            "plural": "contribuables",
            "label": "Contribuables",
            "doc": "Les contribuables du pays"
        }
    ]
)

Proprietaire = build_entity(
    key = "proprietaire",
    plural = "proprietaires",
    label = "Proprietaire de local ou de locaux soumis a l'impot foncier",
    doc = "https://lexpol.cloud.pf/LexpolAfficheTexte.php?texte=581595",
    roles = [
        {
            "key": "local"
        }
    ]
)

entities = [Pays, Personne, Employes, Dossier]
