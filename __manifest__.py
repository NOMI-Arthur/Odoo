# -*- coding: utf-8 -*-
{
    'name': "Matrix Télécoms's CRM",

    'summary': """
        An all in one solution for CRM""",

    'description': """
        A module for the management of customers using unidirectional SMS sendings
    """,

    'author': "Matrix Télécoms SA",
    'website': "http://www.matrixtelecoms.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/USER/users.xml',
        'views/USER/client.xml',
        'views/USER/partner.xml',
        'views/Group/group.xml',
        'views/templates.xml',
        'reports/ticket.xml',
        'reports/client.xml',
        'reports/contract.xml',
        'reports/compte.xml',
        'reports/sms.xml',
        'reports/bondeSorti.xml',
        'reports/soldeCompte.xml',
        'views/Finances/compte.xml',
        'views/Finances/gestCompte.xml',
        'views/planning/planning.xml',
        'views/planning/visite_Technique.xml',
        'views/planning/contract.xml',
        'views/contact/ticket.xml',
        'views/contact/sms.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}