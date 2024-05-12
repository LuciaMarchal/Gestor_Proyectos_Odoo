# -*- coding: utf-8 -*-
{
    'name': "Project Management",

    'summary': """
        Permite a los usuarios crear y gestionar proyectos dentro de la plataforma Odoo.
    """,

    'description': """
        Proporciona funcionalidades para crear nuevos proyectos, asignar responsables, establecer fechas de inicio y fin, y gestionar la información general del proyecto. Los usuarios pueden acceder a una lista de proyectos existentes, ver su estado y detalles, así como realizar acciones como la creación de nuevas tareas dentro de cada proyecto.
    """,

    'author': "Lucia Marchal",
    'website': "https://www.luciamarchal.com",

    'category': 'Other',
    'version': '16.0',

    'depends': ['base'],

    'data': [
        'data/demo.xml',
        'security/ir.model.access.csv',
        'views/project_project.xml',
        'views/project_employee.xml',
        'views/project_report.xml',
        'views/project_resource.xml',
        'views/actions.xml',
        'views/menus.xml',
    ],

    'demo': [
        'data/demo.xml',
    ],
    'application': True
}
