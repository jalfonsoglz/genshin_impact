# -*- coding: utf-8 -*-
{
    'name': "Genshin Impact Tracker",

    'summary': """Módulo de Gestión de Personajes de Genshin Impact""",

    'description': """
    Elements and Weapons as Many2one model
    """,
    'author': "Alfonso Gonzalez (alfonso@ptree.com.mx)",
    'website': "https://ntropy.tech",
    'category': 'Customizations',
    'version': '15.0.0.0.5',
    'license': "AGPL-3",
    'sequence': "-95",
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/elements.xml',
        'views/weapon_type.xml',
        'views/characters_conf.xml',
        'data/elements.xml',
        'data/weapon_type.xml',
        'data/characters_conf.xml'
    ],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
