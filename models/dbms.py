# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Dbms(models.Model):
    _inherit = ['mail.thread']
    _name = 'genshin.impact.dbms'
    _description = 'Gestión de Personajes'
    _rec_name = 'name'
    _order = 'level'

    active = fields.Boolean(string='Activo', default=True)
    achieved = fields.Boolean(string='Invocado', default=False, tracking=True)
    # avatar = fields.Many2one(related='name.avatar', string="avatar", readonly=True)
    name = fields.Many2one('genshin.impact.characters', string="Nombre")
    char_element_type = fields.Many2one(related='name.char_element_type', string='Elemento', readonly=True)
    char_weapon_type = fields.Many2one(related='name.char_weapon_type', string='Tipo de Arma')
    weapons = fields.Many2one('genshin.impact.weapons', string='Arma')
    weapon_note = fields.Many2one(related='weapons_name.note', string='Efecto')
    weapon_atk = fields.Integer(string='Ataque', default="1", tracking=True)
    weapon_sub_stat = fields.Many2one(related='weapons_name.weapon_sub_stat_type', string='Sub Status')
    weapon_sub_stat_value = fields.Float(string='Valor', default="1", tracking=True)
    level = fields.Integer(string='Nivel', default="1", tracking=True)
    constellation = fields.Integer(string='Constelación', default="0", tracking=True)
    basic_attack_talent = fields.Integer(string='Ataque Básico', default="1", tracking=True)
    elemental_skill_talent = fields.Integer(string='Ataque Elemental', default="1", tracking=True)
    elemental_burst_talent = fields.Integer(string='Definitiva Elemental', default="1", tracking=True)
    char_hp = fields.Integer(string='Vida', default="1", tracking=True)
    char_atk = fields.Integer(string='Ataque', default="1", tracking=True)
    char_def = fields.Integer(string='Defensa', default="1", tracking=True)
    char_elemental_mastery = fields.Integer(string='Maestría Elemental', default="0", tracking=True)
    char_stamina = fields.Integer(string='Aguante Max.', default="0", tracking=True)
    char_crit_rate = fields.Float(string='Bonus Critico', default="5", tracking=True)
    char_crit_dmg = fields.Float(string='Bonus Daño Critico', default="50", tracking=True)
    char_heal_bonus = fields.Float(string='Bonus Curación', default="1", tracking=True)
    char_heal_bonus2 = fields.Float(string='Curación recibida', default="1", tracking=True)
    char_energy_recharge = fields.Float(string='Recarga de Energía', default="100", tracking=True)
    char_acd = fields.Float(string='Tiempo de Espera', default="1", tracking=True)
    char_shield = fields.Float(string='Bonus de Escudo', default="1", tracking=True)
    char_pyro_bonus = fields.Float(string='Bonus Pyro', default="1", tracking=True)
    char_pyro_res = fields.Float(string='Resistencia Pyro', default="1", tracking=True)
    char_hydro_bonus = fields.Float(string='Bonus Hydro', default="1", tracking=True)
    char_hydro_res = fields.Float(string='Resistencia Hydro', default="1", tracking=True)
    char_dendro_bonus = fields.Float(string='Bonus Dendro', default="1", tracking=True)
    char_dendro_res = fields.Float(string='Resistencia Dendro', default="1", tracking=True)
    char_electro_bonus = fields.Float(string='Bonus Electro', default="1", tracking=True)
    char_electro_res = fields.Float(string='Resistencia Electro', default="1", tracking=True)
    char_anemo_bonus = fields.Float(string='Bonus Anemo', default="1", tracking=True)
    char_anemo_res = fields.Float(string='Resistencia Anemo', default="1", tracking=True)
    char_cryo_bonus = fields.Float(string='Bonus Cryo', default="1", tracking=True)
    char_cryo_res = fields.Float(string='Resistencia Cryo', default="1", tracking=True)
    char_geo_bonus = fields.Float(string='Bonus Geo', default="1", tracking=True)
    char_geo_res = fields.Float(string='Resistencia Geo', default="1", tracking=True)
    char_phy_bonus = fields.Float(string='Bonus Daño Físico', default="1", tracking=True)
    char_phy_res = fields.Float(string='Resistencia Física', default="1", tracking=True)
