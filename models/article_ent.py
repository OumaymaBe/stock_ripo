# -*- coding: utf-8 -*-

from odoo import models, fields, api


class article_ent(models.Model):
    _name = 'article.entrer'
    _description = 'article_entrer'


    article = fields.Many2one('article.gestion__inventaire', string='Article')
    nbr_colis = fields.Float(string="Nombre colis    ")
    poids_brut = fields.Float(string="Poids brut /kg    ")
    poids_net = fields.Float(string="Poids net /kg    ")