# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, fields, models


SUB_STAT_TYPES = [
	('ATK_FLAT', 'Ataque'),
	('ATK_PERC', 'Ataque %'),
	('DEF_FLAT', 'Defensa'),
	('DEF_PERC', 'Defensa %'),
	('HP_FLAT', 'Vida'),
	('HP_PERC', 'Vida %'),
	('ELE_MAST', 'Maestría Elemental'),
	('ERG_RCHG', 'Recarga de Energía'),
	('HEAL_BONUS', 'Bonus Curación'),
	('CRIT_PERC', 'Prob. Critico %'),
	('CRIT_DMG', 'Daño Critico %'),
	('PHY_DMG', 'Daño Físico %'),
]

RARITY = [('3', '★★★'),
          ('4', '★★★★'),
          ('5', '★★★★★')
          ]


class Weapons(models.Model):
	_name = 'genshin.impact.weapons'
	_description = 'Configurar Armas'
	_rec_name = 'name'
	_order = 'name asc'

	active = fields.Boolean(string='Activo', default=True)
	achieved = fields.Boolean(string='Invocada', default=False, tracking=True)
	image = fields.Image(string='Icono de Arma')
	name = fields.Char(string='Nombre del Arma', required=True)
	weapon_type = fields.Many2one('genshin.impact.weapon.type', string='Tipo de Arma', index=True)
	weapon_rarity = fields.Selection(RARITY, string='Rareza')
	weapon_sub_stat_type = fields.Selection(SUB_STAT_TYPES, string='Tipo Sub Stat')
	weapon_note = fields.Html(string='Descripción', copy=False)
	weapon_passive = fields.Html(string='Pasiva Rango 1', copy=False)
	weapon_passive2 = fields.Html(string='Pasiva Rango 2', copy=False)
	weapon_passive3 = fields.Html(string='Pasiva Rango 3', copy=False)
	weapon_passive4 = fields.Html(string='Pasiva Rango 4', copy=False)
	weapon_passive5 = fields.Html(string='Pasiva Rango 5', copy=False)
