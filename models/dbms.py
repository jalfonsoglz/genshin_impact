# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields

RARITY = [('4', '★★★★'),
          ('5', '★★★★★')]

ART_STAT_TYPES = [('ATK_FLAT', 'Ataque'),
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
                  ('ANM_DMG', 'Daño Anemo %'),
                  ('CRY_DMG', 'Daño Cryo %'),
                  ('ELC_DMG', 'Daño Electro %'),
                  ('GEO_DMG', 'Daño Geo %'),
                  ('HYD_DMG', 'Daño Hydro %'),
                  ('PHY_DMG', 'Daño Físico %')
                  ]


class Dbms(models.Model):
    _inherit = ['mail.thread']
    _name = 'genshin.impact.dbms'
    _description = 'Gestión de Personajes'
    _rec_name = 'name'
    _order = 'level, constellation'

    active = fields.Boolean(string='Activo', default=True)
    achieved = fields.Boolean(string='Invocado', default=False, tracking=True)
    avatar = fields.Image(related='name.avatar', string="avatar")
    name = fields.Many2one('genshin.impact.characters', string="Nombre")
    char_rarity = fields.Selection(related='name.char_rarity', string='Rareza')
    char_element_type = fields.Many2one(related='name.char_element_type', string='Elemento', readonly=True, store=True)
    char_weapon_type = fields.Many2one(related='name.char_weapon_type', string='Tipo Arma', readonly=True, store=True)
    char_weapon = fields.Many2one('genshin.impact.weapons', string='Arma')
    weapon_rarity = fields.Selection(related='char_weapon.weapon_rarity', string='Rareza')
    char_weapon_level = fields.Integer(string='Niv.', default="1", tracking=True)
    char_weapon_upgrade = fields.Integer(string='Refinamiento', default="1", tracking=True)
    weapon_stat = fields.Selection(related='char_weapon.weapon_sub_stat_type', string='Tipo de Sub Stat')
    weapon_passive = fields.Html(related='char_weapon.weapon_passive', string='Pasiva R1')
    weapon_passive2 = fields.Html(related='char_weapon.weapon_passive2', string='Pasiva R2')
    weapon_passive3 = fields.Html(related='char_weapon.weapon_passive3', string='Pasiva R3')
    weapon_passive4 = fields.Html(related='char_weapon.weapon_passive4', string='Pasiva R4')
    weapon_passive5 = fields.Html(related='char_weapon.weapon_passive5', string='Pasiva R5')
    weapon_atk = fields.Integer(string='Ataque', default="1", tracking=True)
    weapon_sub_stat_value = fields.Float(string='Sub Valor', default="1", tracking=True)
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
    char_art_flower = fields.Many2one('genshin.impact.artifacts', string='Flor de la Vida', tracking=True)
    char_art_flower_rarity = fields.Selection(RARITY, string='Rareza (Flor)', tracking=True)
    char_art_flower_level = fields.Integer(string='Nivel', default="1", tracking=True)
    char_art_flower_stat0 = fields.Float(string='Estad. Base', default="1", tracking=True)
    char_art_flower_stat1 = fields.Float(string='Estad. Sec. 1', default="1", tracking=True)
    char_art_flower_stat2 = fields.Float(string='Estad. Sec. 2', default="1", tracking=True)
    char_art_flower_stat3 = fields.Float(string='Estad. Sec. 3', default="1", tracking=True)
    char_art_flower_stat4 = fields.Float(string='Estad. Sec. 4', default="1", tracking=True)
    char_art_flower_sub0 = fields.Selection(ART_STAT_TYPES, string='Tipo Base', default='HP_FLAT', tracking=True)
    char_art_flower_sub1 = fields.Selection(ART_STAT_TYPES, string='Tipo Estad. 1', tracking=True)
    char_art_flower_sub2 = fields.Selection(ART_STAT_TYPES, string='Tipo Estad. 2', tracking=True)
    char_art_flower_sub3 = fields.Selection(ART_STAT_TYPES, string='Tipo Estad. 3', tracking=True)
    char_art_flower_sub4 = fields.Selection(ART_STAT_TYPES, string='Tipo Estad. 4', tracking=True)
    char_art_plume = fields.Many2one('genshin.impact.artifacts', string='Pluma de la Muerte', tracking=True)
    char_art_plume_rarity = fields.Selection(RARITY, string='Rareza (Pluma)', tracking=True)
    char_art_plume_level = fields.Integer(string='Nivel', default="1", tracking=True)
    char_art_plume_stat0 = fields.Float(string='Estad. Base', default="1", tracking=True)
    char_art_plume_stat1 = fields.Float(string='Stat 1', default="1", tracking=True)
    char_art_plume_stat2 = fields.Float(string='Stat 2', default="1", tracking=True)
    char_art_plume_stat3 = fields.Float(string='Stat 3', default="1", tracking=True)
    char_art_plume_stat4 = fields.Float(string='Stat 4', default="1", tracking=True)
    char_art_plume_sub0 = fields.Selection(ART_STAT_TYPES, string='Tipo Base', default='ATK_FLAT', tracking=True)
    char_art_plume_sub1 = fields.Selection(ART_STAT_TYPES, string='Sub 1', tracking=True)
    char_art_plume_sub2 = fields.Selection(ART_STAT_TYPES, string='Sub 2', tracking=True)
    char_art_plume_sub3 = fields.Selection(ART_STAT_TYPES, string='Sub 3', tracking=True)
    char_art_plume_sub4 = fields.Selection(ART_STAT_TYPES, string='Sub 4', tracking=True)
    char_art_sands = fields.Many2one('genshin.impact.artifacts', string='Arenas del Eon', tracking=True)
    char_art_sands_rarity = fields.Selection(RARITY, string='Rareza (Arenas)', tracking=True)
    char_art_sands_level = fields.Integer(string='Nivel', default="1", tracking=True)
    char_art_sands_stat0 = fields.Float(string='Estad. Base', default="1", tracking=True)
    char_art_sands_stat1 = fields.Float(string='Stat 1', default="1", tracking=True)
    char_art_sands_stat2 = fields.Float(string='Stat 2', default="1", tracking=True)
    char_art_sands_stat3 = fields.Float(string='Stat 3', default="1", tracking=True)
    char_art_sands_stat4 = fields.Float(string='Stat 4', default="1", tracking=True)
    char_art_sands_sub0 = fields.Selection(ART_STAT_TYPES, string='Tipo Base', tracking=True)
    char_art_sands_sub1 = fields.Selection(ART_STAT_TYPES, string='Sub 1', tracking=True)
    char_art_sands_sub2 = fields.Selection(ART_STAT_TYPES, string='Sub 2', tracking=True)
    char_art_sands_sub3 = fields.Selection(ART_STAT_TYPES, string='Sub 3', tracking=True)
    char_art_sands_sub4 = fields.Selection(ART_STAT_TYPES, string='Sub 4', tracking=True)
    char_art_goblet = fields.Many2one('genshin.impact.artifacts', string='Cáliz de Eonothem', tracking=True)
    char_art_goblet_rarity = fields.Selection(RARITY, string='Rareza (Cáliz)', tracking=True)
    char_art_goblet_level = fields.Integer(string='Nivel', default="1", tracking=True)
    char_art_goblet_stat0 = fields.Float(string='Estad. Base', default="1", tracking=True)
    char_art_goblet_stat1 = fields.Float(string='Stat 1', default="1", tracking=True)
    char_art_goblet_stat2 = fields.Float(string='Stat 2', default="1", tracking=True)
    char_art_goblet_stat3 = fields.Float(string='Stat 3', default="1", tracking=True)
    char_art_goblet_stat4 = fields.Float(string='Stat 4', default="1", tracking=True)
    char_art_goblet_sub0 = fields.Selection(ART_STAT_TYPES, string='Tipo Base', tracking=True)
    char_art_goblet_sub1 = fields.Selection(ART_STAT_TYPES, string='Sub 1', tracking=True)
    char_art_goblet_sub2 = fields.Selection(ART_STAT_TYPES, string='Sub 2', tracking=True)
    char_art_goblet_sub3 = fields.Selection(ART_STAT_TYPES, string='Sub 3', tracking=True)
    char_art_goblet_sub4 = fields.Selection(ART_STAT_TYPES, string='Sub 4', tracking=True)
    char_art_circlet = fields.Many2one('genshin.impact.artifacts', string='Tiara de Logos', tracking=True)
    char_art_circlet_rarity = fields.Selection(RARITY, string='Rareza (Tiara)', tracking=True)
    char_art_circlet_level = fields.Integer(string='Nivel', default="1", tracking=True)
    char_art_circlet_stat0 = fields.Float(string='Estad. Base', default="1", tracking=True)
    char_art_circlet_stat1 = fields.Float(string='Stat 1', default="1", tracking=True)
    char_art_circlet_stat2 = fields.Float(string='Stat 2', default="1", tracking=True)
    char_art_circlet_stat3 = fields.Float(string='Stat 3', default="1", tracking=True)
    char_art_circlet_stat4 = fields.Float(string='Stat 4', default="1", tracking=True)
    char_art_circlet_sub0 = fields.Selection(ART_STAT_TYPES, string='Tipo Base', tracking=True)
    char_art_circlet_sub1 = fields.Selection(ART_STAT_TYPES, string='Sub 1', tracking=True)
    char_art_circlet_sub2 = fields.Selection(ART_STAT_TYPES, string='Sub 2', tracking=True)
    char_art_circlet_sub3 = fields.Selection(ART_STAT_TYPES, string='Sub 3', tracking=True)
    char_art_circlet_sub4 = fields.Selection(ART_STAT_TYPES, string='Sub 4', tracking=True)
    art_2pza_set = fields.Many2one('genshin.impact.artifacts.sets', string='Set 2 Piezas')
    art_4pza_set = fields.Many2one('genshin.impact.artifacts.sets', string='Set 4 Piezas')
    art_2pza_passive = fields.Html(related='art_2pza_set.art_passive2', string='Pasiva 2 Piezas', readonly=True)
    art_4pza_passive = fields.Html(related='art_4pza_set.art_passive4', string='Pasiva 4 Piezas', readonly=True)
