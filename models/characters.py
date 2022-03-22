# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Characters(models.Model):
    _name = 'genshin.impact.characters'
    _description = 'Configurar Personajes'
    _rec_name = 'name'
    _order = 'name'

    active = fields.Boolean(string='Activo', default=True)
    avatar = fields.Image(string='Avatar')
    full_avatar = fields.Image(string='Avatar')
    name = fields.Char(string='Nombre')
    char_element_type = fields.Many2one('genshin.impact.elements', string='Elemento')
    char_weapon_type = fields.Many2one('genshin.impact.weapon.type', string='Tipo de Arma')
    note = fields.Text(string='Descripción', copy=False, tracking=True)
