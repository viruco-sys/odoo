# -*- coding: utf-8 -*-
{
    'name': 'Madenat Lumber Importer',
    'version': '18.0.1.0.0',
    'summary': 'Asistente para importar packing lists de proveedores.',
    'author': 'Mauricio Canahuate, Asistente AI',
    'website': 'https://www.madenat.cl',
    'category': 'Inventory',
    'depends': [
        'stock',
        'purchase', # Dependemos de Compras para la referencia
        'madenat_lumber_core', # Dependemos de nuestro módulo core
    ],
    'data': [
        'security/ir.model.access.csv', # No olvides crear este archivo
        'wizards/packing_list_importer_views.xml',
    ],
    'installable': True,
    'application': False,
}