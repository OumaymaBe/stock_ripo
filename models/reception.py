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
    origine = fields.Char(string='Origine   ')
    fournisseur = fields.Many2one(
        'res.partner', 'Fournisseur',
        ondelete='cascade')
    matricule = fields.Char(string='Matricule véhicule   ')
    chauffeur = fields.Char(string='Nom du chauffeur   ')
    cin = fields.Char(string='N° CIN   ')
    date = fields.Date(string='Date', default=datetime.today())
    acheteur = fields.Many2one(
        'res.partner', 'Acheteur',
        ondelete='cascade')
    beneficiaire = fields.Char(string='Bénéficiaire   ')
    etat_art = fields.Char(string='Etat du produit   ')
    date_marree = fields.Date(string='Date marrée   ')
    # nbr_colis = fields.Float(string="Nombre colis    ")
    # poids_brut = fields.Float(string="Poids brut/kg    ")
    # poids_net = fields.Float(string="Poids net/kg    ")
    article=fields.Many2many('reception.article',string='Article')
    # article = fields.Many2many('article.gestion__inventaire', string='Article')
    observation =fields.Html(string='Observation   ')
    state = fields.Selection([('draft', 'Reception'),
                            ('inprogress', 'Entrer'),
                            # ('done', 'Terminé'),
                            ('refus', 'Rejeter'),
                            ], required=False
                            , default="draft"
                            , string='state')

    # total = fields.Float(string='Total net' , compute="_compute_total")
    # total_br = fields.Float(string='Total brut' , compute="_compute_total_br")
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'reception.gestion__inventaire.sequence') or 'New'
        result = super(reception, self).create(vals)
        return result
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



    # def default_get(self):
    #     arts=[(11)]
    #     self.write({"article":[(11,0,0,0,0,0,0,0,0,0,0,0,arts)]})         
   
   
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
    # def creat_bn(self):
    #     # self.state = 'inprogress'
    #     for rec in self:
    #         vals ={
    #         'name' :rec.name,
    #         # 'date':rec.date,
    #         # 'article':rec.article,
    #     }
    #     bon_rec =rec.env['bon.entrer'].create(vals)
    # #     print ("Bon entrer",bon_rec.id)
    # #     # rec.state = 'inprogress',
    # #     # self.state = 'inprogress',
    #     return{
    #         'name':'bonEntrer',
    #         'type':'ir.actions.act_window',
    #         'view_mode':'form',
    #         'res_model':'bon.entrer',
    #         'target':'current',
    #         'res_id':bon_rec.id 
    #     }
        
    # @api.depends('article')
    # def count_article(self):
    #     return len(self.article)