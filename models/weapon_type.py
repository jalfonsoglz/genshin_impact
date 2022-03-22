# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class WeaponType(models.Model):
	_name = 'genshin.impact.weapon.type'
	_description = 'Configurar Tipo de Arma'
	_rec_name = 'name'
	_order = 'name asc'

	active = fields.Boolean(string='Activo', default=True)
	avatar = fields.Image(string='Icono de Arma')
	name = fields.Char(string='Nombre del Arma', required=True)
	note = fields.Text(string='Descripción', copy=False, tracking=True)