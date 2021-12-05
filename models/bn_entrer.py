# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_
from datetime import datetime


class bn_entrer(models.Model):
    _name = 'bn.entrer'
    _description = 'bonEntrer'

    name = fields.Char(string="Numéro",
                    copy=False,
                    readonly=True,
                    index=True,
                    default='New')
    # num=fields.Many2one('reception.gestion__inventaire', string='name',readonly=True)

    num = fields.Char(string='Bon de reception :',readonly=True)
    date = fields.Date(string='Date', default=datetime.today())
    # article = fields.Many2many('article.gestion__inventaire', string='Article :')
    # @api.onchange('num')
    # def sub(self):
    #     self.article |= self.num.art
    #     return{}
    article=fields.Many2many('article.entrer',string='Article')

    # nbr_colis = fields.Float(string="Nombre colis    ")
    # poids_brut = fields.Float(string="Poids brut/kg    ")
    # poids_net = fields.Float(string="Poids net/kg    ")
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'bn.entrer.sequence') or 'New'
        result = super(bn_entrer, self).create(vals)
        return result
    # def def_value(self):
    #     values =[]
    #     values['article'] = (6, 0, [1])
    #     self.write(values)
    # total = fields.Float(string='Total net /Kgs')
    # total_br = fields.Float(string='Total brut /Kgs')
    #  , compute="_compute_total_br"
    
    # @api.depends('article')
    # def _compute_total(self):
    #     for rec in self:
    #         totals = 0
    #         for poids in rec.article:
    #             totals += poids.poids_net
    #         rec.total = totals

    # @api.depends('article')
    # def _compute_total_br(self):
    #     for rec in self:
    #         totals = 0
    #         for poids in rec.article:
    #             totals += poids.poids_brut
    #         rec.total_br = totals