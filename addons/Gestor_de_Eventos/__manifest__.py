{
    'name': 'Gestión Eventos Sergio',
    'version': '1.0',
    'summary': 'Módulo de gestión de eventos',
    'author': 'sercanmar',
    'depends': ['base', 'sale_management', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'application': True,
    'installable': True,
}