# -*- coding: utf-8 -*-
from odoo import models, fields, api ,_
# from openerp.osv import fields,osv
# from openerp.tools.translate import _


class bon_entrer(models.TransientModel):
    _name = 'bon.entrer'
    
     

# class bon_entrer(osv.osv_memory):
#     _name = "bon.entrer"
#     _columns={
#         'text': fields.text("confirmer"),
#     }
#     bon_entrer()

#     @api.multi
#     def btn_show_dialog_box(self):
#         text = """Write your custom message here to show in dialog box"""
#         query ='delete from bon_entrer'
#         self.env.cr.execute(query)
#         value = self.env['bon.entrer'].sudo().create({'text':text})
#         return{
#             'type':'ir.actions.act_window',
#             'name':'Message',
#             'res_model':'bon.entrer',
#             'view_type':'form',
#             'view_mode':'form',
#             'target':'new',
#             'res_id':value.id                
#         }
    # name =fields.many2one('article.gestion__inventaire', string='name')
    # des =fields.one2many('article.gestion__inventaire', 'des', 'des')
    # nature =fields.one2many('article.gestion__inventaire', 'nature', 'nature')
    # name = fields.Many2one('article.gestion__inventaire', string='Ref Article')
    # des = fields.Many2one('article.gestion__inventaire', string='Ref Article',readonly=True)
    # nature = fields.Many2one('article.gestion__inventaire', string='Ref Article',readonly=True)
    # name = fields.Many2many('reception.gestion__inventaire', string='Article')
    # name = fields.Many2many('article.gestion__inventaire', string='Article')
    name=fields.Char(string="valider le bon reception",readonly=True)

    # art = fields.Many2one('article.gestion__inventaire', string='Article')
    # nbr_colis = fields.Float(string="Nombre colis    ")
    # poids_brut = fields.Float(string="Poids brut/kg    ")
    # poids_net = fields.Float(string="Poids net/kg    ")
    # des = fields.One2many(
    #     'article.gestion__inventaire',
    #     'des',
    #     'des',
        
    # )
    def action_create_bon_entrer(self):
        # vals ={
            
            # 'name' :self.name,
            # 'nbr_colis':self.nbr_colis,
            # 'poids_brut':self.poids_brut,
            # 'poids_net':self.poids_net,
        # }
        # bon_rec =self.env['article.gestion__inventaire'].create(vals)
        # print ("Bon entrer",bon_rec.id)
        return{
            'name':'bonEntrer',
            'type':'ir.actions.act_window',
            'view_mode':'tree,form',
            'res_model':'bn.entrer',
            'target':'current',
            
        }

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

        