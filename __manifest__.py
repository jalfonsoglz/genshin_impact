# -*- coding: utf-8 -*-
{
    'name': "Genshin Impact Tracker",

    'summary': """Módulo de Gestión de Personajes de Genshin Impact""",

    'description': """
    ** Update **
    Add 34 Artifacts Sets with Set Name and Icon (next update individual names)
    ** 2.6 Update **
    * Add Ayato
    * Add Artifact Set
        * Vermillion Hereafter (new)
        * Echoes of an Offering (new)
    ** Fixes **
    * Add Artifact Set
        * Husk of Opulent Dreams (missed)
        * Ocean-Hued Clam (missed)
    * Add Ayaka last name
    * More minor fixes
    """,
    'author': "Alfonso Gonzalez",
    'website': "https://ntropy.tech",
    'category': 'Customizations',
    'version': '15.0.0.1.8',
    'license': "AGPL-3",
    'sequence': "-99",
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
        'data/artifacts.sets.xml',
        'data/artifacts.xml',
        'data/characters.xml'
        # 'data/genshin.impact.characters.csv'
    ],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
