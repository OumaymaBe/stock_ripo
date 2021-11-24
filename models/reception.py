# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_
from datetime import datetime


class reception(models.Model):
    _name = 'reception.gestion__inventaire'
    _description = 'reception'

    name = fields.Char(string="Numéro",
                       copy=False,
                       readonly=True,
                       index=True,
                       default='New')
    origine = fields.Char(string='Origine   ',required=True)
    fournisseur = fields.Char(string='Fournisseur   ')
    matricule = fields.Char(string='Matricule véhicule   ',required=True)
    chauffeur = fields.Char(string='Nom du chauffeur   ',required=True)
    cin = fields.Char(string='N° CIN   ',required=True)
    date = fields.Date(string='Date', default=datetime.today())
    acheteur = fields.Char(string='Acheteur   ',required=True)
    beneficiaire = fields.Char(string='Bénéficiaire   ',required=True)
    etat_art = fields.Char(string='Etat du produit   ',required=True)
    date_marree = fields.Char(string='Date marrée   ',required=True)
    article = fields.Many2many('article.gestion__inventaire', string='Article')
    observation =fields.Html(string='Observation   ')
    
    # responsable = fields.Char(string='Responsable   ',required=True)
    # quantite_demander = fields.Char(string='Quantité demander   ')
    # date_prevue = fields.Date(string='Date prévue   ')
    # fournisseur = fields.Char(string='Fournisseur   ')
    # # article = fields.Char(string='Article   ')

    # emplacement = fields.Char(string='Emplacement   ')
    # qtefinal = fields.Char(string='Quantité Final   ')

    state = fields.Selection([('draft', 'Reception'),
                            ('inprogress', 'Entrer'),
                            # ('done', 'Terminé'),
                            ('refus', 'Rejeter'),
                            ], required=False
                            , default="draft"
                            , string='state')

    total = fields.Float(string='Total' , compute="_compute_total")
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'reception.gestion__inventaire.sequence') or 'New'
        result = super(reception, self).create(vals)
        return result

    def action_star(self):
        for rec in self:
            rec.state = 'inprogress'
    def action_broui(self):
        for rec in self:
            rec.state = 'draft'
    # def action_trem(self):
    #     for rec in self:
    #         rec.state = 'done'
    def action_anuuler(self):
        for rec in self:
            rec.state = 'refus'


    def print_reception(self):
        receptions = self.env['reception.gestion__inventaire'].search_read([])
        data={
            'form' : self.read()[0],
            'receptions' : receptions
        }
        return self.env.ref('gestion__inventaire.print_reception').report_action(self, data=data) 

                
    @api.depends('article')
    def _compute_total(self):
        for rec in self:
            totals = 0
            for poids in rec.article:
                totals += poids.poids_net
            rec.total = totals
   
        # bn = self.env["bn.entrer"]
        # for o in self:
        #     if o.state == 'inprogress':
        #             vals = {
        #                 'name': 'Bon Entrer: ' + o.name,
        #                 # 'chang': o.state,
        #             }
            # bn_obj = bn.create(bn_create)
            # bn_id = bn_obj.id
            # view_id = self.env.ref(
            #     'gestion_inventaire.view_bn_entrer_form').id
            # self.write({'state': 'done'})
            # return {
            #     'view_type': 'form',
            #     'view_mode': 'form',
            #     'res_model': 'bn.entrer',
            #     'view_id': view_id,
            #     'type': 'ir.actions.act_window',
            #     'name':'Analyse',
            #     'res_id': bn_id
            # }
            #  def action_create_bon_entrer(self):
        # bon_rec =self.env['bn.entrer'].create(vals)
        # print ("Bon entrer",bon_rec.id)
    def creat_bn(self):
        self.state = 'inprogress'
        for rec in self:
            
            vals ={
            'num' :rec.name,
            'date':rec.date,
            # 'article':rec.article,
        }
        bon_rec =rec.env['bn.entrer'].create(vals)
        print ("Bon entrer",bon_rec.id)
        # rec.state = 'inprogress',
        # self.state = 'inprogress',
        return{
            'name':'bonEntrer',
            'type':'ir.actions.act_window',
            'view_mode':'form',
            'res_model':'bn.entrer',
            'target':'current',
            'res_id':bon_rec.id 
        }
