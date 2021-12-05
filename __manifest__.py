# -*- coding: utf-8 -*-
{
    'name': "Gestion_Inventaire",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/menu.xml',
        
        'wizards/bon_entrer.xml',
        
        'views/reception.xml',
        
        'views/livraison.xml',
        'views/article.xml',
        'views/rec_art.xml',
        'views/article_ent.xml',
        

        'views/qty.xml',

        # 'views/categorie.xml',
        
        # 'views/kanban.xml',
        'reports/report.xml',
        'reports/report_reception.xml',
        'reports/report_livraison.xml',
        'views/bonEntrer.xml'

        # 'views/inherit_client.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
