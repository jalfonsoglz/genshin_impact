# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, fields, models

ART_TYPES = [
	('FLOWER', 'Flor de la Vida'),
	('PLUME', 'Pluma de la Muerte'),
	('SANDS', 'Arenas del Eon'),
	('GOBLET', 'Cáliz de Eonothem'),
	('CIRCLET', 'Tiara de Logos'),
]


class Artifacts(models.Model):
	_name = 'genshin.impact.artifacts'
	_description = 'Configurar Artefactos'
	_rec_name = 'name'
	_order = 'name asc'

	image = fields.Image(string='Icono')
	name = fields.Char(string='Nombre del Artefactos', required=True)
	art_types = fields.Selection(ART_TYPES, string='Tipo')
	art_set = fields.Many2one('genshin.impact.artifacts.sets', string='Set de Artefactos')


class ArtifactsSets(models.Model):
	_name = 'genshin.impact.artifacts.sets'
	_description = 'Configurar Conjunto de Artefactos'
	_rec_name = 'name'
	_order = 'name asc'

	image = fields.Image(string='Icono')
	name = fields.Char(string='Conjunto de Artefactos')
	art_passive_note = fields.Html(string='Notas Bonus', copy=False)
	art_passive2 = fields.Html(string='2 Piezas', copy=False)
	art_passive4 = fields.Html(string='4 Piezas', copy=False)
