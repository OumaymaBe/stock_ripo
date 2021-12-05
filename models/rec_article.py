# -*- coding: utf-8 -*-

from odoo import models, fields, api




class reception_art(models.Model):
    _name = 'reception.article'
    _description = 'reception_article'

    article = fields.Many2one('article.gestion__inventaire', string='Article')
    nbr_colis = fields.Float(string="Nombre colis    ")
    poids_brut = fields.Float(string="Poids brut /kg    ")
    poids_net = fields.Float(string="Poids net /kg    ")