# -*- coding: utf-8 -*-
{
    'name': 'Madenat Lumber Core',
    'version': '18.0.1.0.0',
    'summary': 'Modelo de datos y cálculos base para la operación maderera.',
    'author': 'Mauricio Canahuate, Asistente AI',
    'website': 'https://www.madenat.cl',
    'category': 'Inventory',
    'depends': [
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/decimal_precision.xml', 
        'data/res_config_settings_data.xml',
        'data/stock_lot_actions.xml',
        'views/stock_lot_views.xml',
    ],
    'installable': True,
    'application': True, # Lo marcamos como aplicación para que sea fácil de encontrar
}
