# -*- coding: utf-8 -*-
{
    'name': 'Madenat Lumber Logistics',
    'version': '18.0.1.0.0',
    'summary': 'Gestiona la logística de embarques de madera.',
    'author': 'Mauricio Canahuate, Asistente AI',
    'website': 'https://www.madenat.cl',
    'category': 'Inventory',
    'depends': [
        'stock',
        'madenat_lumber_core',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/lumber_shipment_views.xml',
    ],
    'installable': True,
    'application': False,
}