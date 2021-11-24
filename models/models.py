# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mouvement_stock(models.Model):
    _name = 'mouvement.gestion__inventaire'
    _description = 'Mouvement'

    reception_id = fields.Many2one('reception.gestion__inventaire', string='Reception' )
    entrer= fields.Many2one('bn.entrer.gestion__inventaire', string='Livraison')