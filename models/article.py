# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_


class article(models.Model):
    _name = 'article.gestion__inventaire'
    _description = 'Article'

    name = fields.Char(string="Numéro",
                       copy=False,
                       readonly=True,
                       index=True,
                       default='New')
    des = fields.Char(string="Désignation    ")
    nbr_colis = fields.Float(string="Nombre colis    ")
    poids_brut = fields.Float(string="Poids brut/kg    ")
    poids_net = fields.Float(string="Poids net/kg    ")
    nature = fields.Selection([('1', 'plastique'),
                            ('2', 'carton'),
                            ('3', 'bois'),
                            ], required=False
                            , string='Nature')

    # type = fields.Char(string="Type    ")
    # -------------------
    
    image = fields.Binary(string="Image")
    # taxe = fields.Char(string="Taxes à la vente    ")
    # coût = fields.Char(string="Coût    ")
    description = fields.Text(string="Description    ")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'article.gestion__inventaire.sequence') or 'New'
        result = super(article, self).create(vals)
        return result