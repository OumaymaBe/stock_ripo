# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_


class livraison(models.Model):
    _name = 'livraison.gestion__inventaire'
    _description = 'Livraison'

    name = fields.Char(string='Référence    ',required=True)
    responsable = fields.Char(string='Responsable   ',required=True)
    demande_initial = fields.Char(string='Demande initial   ')
    qteRecu = fields.Char(string='Quantité Recu   ')

    date_prevue = fields.Date(string='Date prévue   ')
    client = fields.Char(string='Client   ')
    # client = fields.Many2one('res.partner', string='Client')
    # client = fields.Many2one('res.partner', readonly=True, tracking=True,
    #     check_company=True,
    #     string='Partner', change_default=True)
    article = fields.Many2many('article.gestion__inventaire', string='Article')
    emplacement = fields.Char(string='Emplacement   ')
    state = fields.Selection([('draft', 'entrer'),
                            ('inprogress', 'reception'),
                            ('done', 'Terminé'),
                            ('refus', 'Annulé'),
                            ], required=False
                            , default="draft"
                            , string='state')

    def action_star(self):
        for rec in self:
            rec.state = 'inprogress'
    def action_broui(self):
        for rec in self:
            rec.state = 'draft'
    def action_trem(self):
        for rec in self:
            rec.state = 'done'
    def action_anuuler(self):
        for rec in self:
            rec.state = 'refus'

    def print_livraison(self):
            livraisons = self.env['livraison.gestion__inventaire'].search_read([])
            data={
                'form' : self.read()[0],
                'livraisons' : livraisons
            }
            return self.env.ref('gestion__inventaire.print_livraison').report_action(self, data=data) 

# class client(models.Model):
#     _inherit = 'hr.employee'