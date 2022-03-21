# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class CharactersConf(models.Model):
    _inherit = ['mail.thread']
    _name = 'genshin.impact.characters.conf'
    _description = 'Personajes'
    _rec_name = 'name'
    _order = 'level'

    active = fields.Boolean(string='Activo', default=True)
    avatar = fields.Image(string='Avatar')
    full_avatar = fields.Image(string='Avatar')
    name = fields.Char(string='Nombre', required=True)
    achieved = fields.Boolean(string='Invocado', default=False, tracking=True)
    element = fields.Many2one('genshin.impact.elements', string='Elemento', required=True)
    weapon_type = fields.Many2one('genshin.impact.weapon.type', string='Tipo de Arma', required=True)
    level = fields.Integer(string='Nivel', default="1", tracking=True)
    constellation = fields.Integer(string='Constelación', default="0", tracking=True)
    basic_attack_talent = fields.Integer(string='Ataque Básico', default="1", tracking=True)
    elemental_skill_talent = fields.Integer(string='Ataque Elemental', default="1", tracking=True)
    elemental_burst_talent = fields.Integer(string='Definitiva Elemental', default="1", tracking=True)
    char_hp = fields.Integer(string='Vida', default="1", tracking=True)
    char_atk = fields.Integer(string='Ataque', default="1", tracking=True)
    char_def = fields.Integer(string='Defensa', default="1", tracking=True)
    char_crit_rate = fields.Integer(string='Bonus Critico', default="1", tracking=True)
    char_crit_dmg = fields.Integer(string='Bonus Daño Critico', default="1", tracking=True)
    char_heal_bonus = fields.Integer(string='Bonus Curación', default="1", tracking=True)
    char_heal_bonus2 = fields.Integer(string='Curación recibida', default="1", tracking=True)
    char_energy_recharge = fields.Integer(string='Recarga de Energía', default="1", tracking=True)
    char_acd = fields.Integer(string='Tiempo de Espera', default="1", tracking=True)
    char_shield = fields.Integer(string='Bonus de Escudo', default="1", tracking=True)
    char_pyro_bonus = fields.Integer(string='Bonus Pyro', default="1", tracking=True)
    char_pyro_res = fields.Integer(string='Resistencia Pyro', default="1", tracking=True)
    char_hydro_bonus = fields.Integer(string='Bonus Hydro', default="1", tracking=True)
    char_hydro_res = fields.Integer(string='Resistencia Hydro', default="1", tracking=True)
    char_dendro_bonus = fields.Integer(string='Bonus Dendro', default="1", tracking=True)
    char_dendro_res = fields.Integer(string='Resistencia Dendro', default="1", tracking=True)
    char_electro_bonus = fields.Integer(string='Bonus Electro', default="1", tracking=True)
    char_electro_res = fields.Integer(string='Resistencia Electro', default="1", tracking=True)
    char_anemo_bonus = fields.Integer(string='Bonus Anemo', default="1", tracking=True)
    char_anemo_res = fields.Integer(string='Resistencia Anemo', default="1", tracking=True)
    char_cryo_bonus = fields.Integer(string='Bonus Cryo', default="1", tracking=True)
    char_cryo_res = fields.Integer(string='Resistencia Cryo', default="1", tracking=True)
    char_geo_bonus = fields.Integer(string='Bonus Geo', default="1", tracking=True)
    char_geo_res = fields.Integer(string='Resistencia Geo', default="1", tracking=True)
    char_phy_bonus = fields.Integer(string='Bonus Daño Físico', default="1", tracking=True)
    char_phy_res = fields.Integer(string='Resistencia Daño Físico', default="1", tracking=True)
