# -*- coding: utf-8 -*-
from odoo import models, fields, api ,_



class bon_entrer(models.TransientModel):
    _name = 'bon.entrer'
    
     

    reception_id=fields.Many2one('reception.gestion__inventaire', string='Réception',readonly=True)
    # @api.onchange('reception_id')
    # def sub(self):
    #     self.art |= self.reception_id.article
    #     return{}
    # art = fields.Many2many('article.gestion__inventaire', string='Article')
    art=fields.Many2many('article.entrer',string='Article')

    def action_create_bon_entrer(self):
        self.reception_id.state = 'inprogress'
        vals ={
            'num':self.reception_id.name,
            'article':self.art,
        }
        bon_rec =self.env['bn.entrer'].create(vals)
        print ("Bon entrer",bon_rec.id)
        return{
            'name':'bonEntrer',
            'type':'ir.actions.act_window',
            'view_mode':'tree,form',
            'res_model':'bn.entrer',
            'target':'current',
        }
    
# bn = fields.Many2many('bn.entrer', string='Article :')
    # def confirmer(self):
    #     self.bn.article |=self.art
    
        # arts=[(11, 0, 0 ,0 ,0)]
        # self.write({"art":[(11,0,arts)]})
    # nbr_colis = fields.Float(string="Nombre colis    ")
    # poids_brut = fields.Float(string="Poids brut/kg    ")
    # poids_net = fields.Float(string="Poids net/kg    ")
    # art = fields.One2many(
    #     'reception.gestion__inventaire',
    #     'article',
    #     'Article',
    # )
    # def action_view_bon_entrer(self):
    #     # action =self.env["ir.actions.actions"]._for_xml_id("gestion__inventaire.action_wizard_view")
    #     # action['domain']=[('name','=',self.name.name)]
    #     action =self.env['article.gestion__inventaire'].read()[0]
    #     action['domain']=[('name','=',self.name.name)]
    #     return{
    #         'type':'ir.actions.act_window',
    #         'name':'BonEntrer',
    #         'res_model':'article.gestion__inventaire',
    #         'view_type':'form',
    #         'domain':[('name','=',self.name.name)],
    #         'view_mode':'tree,form',
    #         'target':'current',
    #     }


        