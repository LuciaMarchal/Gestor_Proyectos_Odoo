# -*- coding: utf-8 -*-
{
    'name': "project_mng",

    'summary': """
        Permite a los usuarios crear y gestionar proyectos dentro de la plataforma Odoo.
    """,

    'description': """
        Proporciona funcionalidades para crear nuevos proyectos, asignar responsables, establecer fechas de inicio y fin, y gestionar la información general del proyecto. Los usuarios pueden acceder a una lista de proyectos existentes, ver su estado y detalles, así como realizar acciones como la creación de nuevas tareas dentro de cada proyecto.
    """,

    'author': "Lucia Marchal",
    'website': "https://www.luciamarchal.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Other',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_project.xml',
        'views/project_employee.xml',
        'views/actions.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
