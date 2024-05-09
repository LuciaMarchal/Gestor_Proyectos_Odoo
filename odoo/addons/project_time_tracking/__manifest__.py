# -*- coding: utf-8 -*-
{
    'name': "Project Time Tracking",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['project_mng'],

    'data': [
        'security/ir.model.access.csv',
        'views/time_tracking.xml',
        'views/project_project.xml',
        'views/actions.xml',
        'views/menus.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    
    'application': False,
}
