# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Elements(models.Model):
	_name = 'genshin.impact.elements'
	_description = 'Configurar Elementos'
	_rec_name = 'name'
	_order = 'name asc'

	active = fields.Boolean(string='Activo', default=True)
	avatar = fields.Image(string='Icono del Elemento')
	name = fields.Char(string='Nombre del Elemento', required=True)
