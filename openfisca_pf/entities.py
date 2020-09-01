# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.
from openfisca_core.entities import build_entity

Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'An individual. The minimal legal entity on which a legislation might be applied.',
    doc = '''

    Variables like 'salary' and 'income_tax' are usually defined for the entity 'Person'.

    Usage:
    Calculate a variable applied to a 'Person' (e.g. access the 'salary' of a specific month with person('salary', "2017-05")).
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'first_parent' in a 'Household' entity with person.has_role(Household.FIRST_PARENT)).

    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True,
    )

Personne = build_entity(
    key = "personne",
    plural = "personnes",
    label = u'An individual. The minimal legal entity on which a legislation might be applied.',
    doc = '''

    Variables like 'salary' and 'income_tax' are usually defined for the entity 'Person'.

    Usage:
    Calculate a variable applied to a 'Person' (e.g. access the 'salary' of a specific month with person('salary', "2017-05")).
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'first_parent' in a 'Household' entity with person.has_role(Household.FIRST_PARENT)).

    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True,
    )

Entreprise = build_entity(
    key = "entreprise",
    plural = "entreprises",
    label = u'Une entreprise.',
    doc = '''

    TODO.
    ''',
    roles = [
        {
            'key': 'Dirigeant',
            'plural': 'dirigeants',
            'label': u'Dirigeants',
            'max': 2,
            'subroles': ['dirigeant1', 'dirigeant2'],
            'doc': u'Le dirigeant de l\'entreprise.'
            },
        {
            'key': 'Employe',
            'plural': 'employes',
            'label': u'Employés',
            'doc': u'La liste des employés de l\'entreprise.'
            }
        ]
    )

entities = [Person, Personne, Entreprise]
