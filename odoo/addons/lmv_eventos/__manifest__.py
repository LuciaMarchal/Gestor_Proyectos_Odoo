# -*- coding: utf-8 -*-
{
    'name': "lmv_eventos",

    'summary': """
        Módulo que gestiona diferentes tipos de eventos, sus asistentes, informes y recordatorios""",

    'description': """
        Módulo que gestiona diferentes tipos de eventos, sus asistentes, informes y recordatorios.
        Los recordatorios se gestionan y editan automáticamente al crear/editar el evento asignado y los informes pueden imprimirse con la informacion principal del evento.
    """,

    'author': "Lucia Marchal",
    'website': "https://www.lmv_eventos_odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestión de eventos',
    'version': '0.1',
    'license': 'LGPL-3',
    
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'data/demo.xml',
        'security/ir.model.access.csv',
        'views/asistente.xml',
        'views/evento.xml',
        'views/informe.xml',
        'views/recordatorio.xml',
        'views/acciones.xml',
        'views/menus.xml'
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'data/demo.xml',
    ],
    
    'application': True,

    
}
