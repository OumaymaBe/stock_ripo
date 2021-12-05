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
    responsible_id = fields.Many2one(
        'res.users', string='Responsable', default=lambda self: self.env.uid, company_dependent=True, check_company=True)
    
    # qti = fields.Many2one('inventaire.gestion__inventaire', string='qty')
    # qte=fields.Float(string='Quantité')       

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'article.gestion__inventaire.sequence') or 'New'
        result = super(article, self).create(vals)
        return result
     
    # def action_update_quantity(self):
    #     for rec in self:
    #         vals ={
    #         'id_article' :rec.name,
    #         'quantite' :rec.qte,
    #         # 'article':rec.article,
            
    #         }
        
    #     bon_rec =rec.env['inventaire.gestion__inventaire'].create(vals)
    #     print ("Inventaire",bon_rec.id)
        
    #     return{
    #         'name':'Inventaire',
    #         'type':'ir.actions.act_window',
    #         'view_mode':'form',
    #         'res_model':'inventaire.gestion__inventaire',
    #         'target':'current',
    #         'res_id':bon_rec.id 
    #     }
 
    # @api.depends('qti')
    # def _compute_qty(self):
    #     for rec in self:
    #         qtotals = 0
    #         for poids in rec.qti:
    #             if rec.name == poids.id_article:
    #                  qtotals = poids.quantite
    #         rec.qte = qtotals
        

    # @api.depends('quantite')
    # def _compute_qty(self):
    #     if self.a==1:
    #         for rec in self:
    #             qts = 0
    #             for qty in rec.quantite:
    #                 if rec.name == qty.id_article:
    #                     qts = qty.quantite
    #             rec.qte = qts