# -*- coding: utf-8 -*-
{
    'name': "Genshin Impact Tracker",

    'summary': """Módulo de Gestión de Personajes de Genshin Impact""",

    'description': """
    * Add Artifact Sets Preload
    * Images view on every view move to right corner
    """,
    'author': "Alfonso Gonzalez",
    'website': "https://ntropy.tech",
    'category': 'Customizations',
    'version': '15.0.0.1.7',
    'license': "AGPL-3",
    'sequence': "-95",
    'depends': [
        'base',
        'mail',
    ],
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
        'data/artifacts.xml',
        'data/artifacts.sets.xml',
        'data/characters.xml'
        # 'data/genshin.impact.characters.csv'
    ],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
