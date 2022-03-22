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
	weapon_sub_stat_type = fields.Selection(SUB_STAT_TYPES, string='Tipo Sub Stat')
	weapon_passive = fields.Text(string='Pasiva', copy=False)
	weapon_note = fields.Text(string='Descripción', copy=False)
