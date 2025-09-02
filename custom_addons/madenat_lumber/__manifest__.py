{
    'name': 'Métricas de Madera para Productos MADENAT',
    'version': '18.0.2.0.0',
    'summary': 'Añade campos de dimensiones y cálculo de volumen multi-unidad (m³, MBF) para productos madereros.',
    'author': 'MADENAT',
    'website': 'https://www.madenat.cl',
    'category': 'Inventory/Product',
    'depends': [
        'product',
        'stock',
        'uom',  # Dependencia explícita de Unidades de Medida
    ],
    'data': [
        'data/uom_data.xml',  # El nuevo archivo de datos va primero
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}


