# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inventaire(models.Model):
    _name = 'inventaire.gestion__inventaire'
    _description = 'inventaire'


    quantite= fields.Float(string='Quantite')
    id_article = fields.Char(string='Article' )
    emplacement = fields.Char(string='Emplacement')
    # id_article = fields.One2many(
    #     'article.gestion__inventaire', string="Article")
    
    # count = fields.Integer(string='Count')

    # @api.depends('id_article')
    # def count_article(self):
    #     for rec in self:
    #         # counte=0
    #         for art in rec.id_article:
    #             if rec.id_article == art:
    #                 rec.count = len(rec.id_article)