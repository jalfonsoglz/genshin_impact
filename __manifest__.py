# -*- coding: utf-8 -*-
{
    'name': "Genshin Impact Tracker",

    'summary': """Módulo de Gestión de Personajes de Genshin Impact""",

    'description': """Módulo de Gestión de Personajes de Genshin Impact""",
    'author': "Alfonso Gonzalez",
    'website': "https://ntropy.tech",
    'category': 'Customizations',
    'version': '15.0.0.2.0',
    'license': "AGPL-3",
    'sequence': "-99",
    'depends': ['mail'],
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/dbms.xml',
        'views/characters.xml',
        'views/weapon_type.xml',
        'views/weapons.xml',
        'views/elements.xml',
        'views/artifacts.xml',
        'views/artifacts_sets.xml',
        # Data Sample
        'data/elements.xml',
        'data/weapon.type.xml',
        'data/weapons.xml',
        'data/artifacts.sets.xml',
        'data/artifacts.xml',
        'data/characters.xml',
        'data/dbms.xml'
    ],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
