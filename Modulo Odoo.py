{
    'name':"Restaurante",

    'summary': """Módulo de platos y menús""
        Short (1 phrase/line) summary of the module's purpose, used as
        subtititle on modules listing or apps.openerp.com""",
    
    'description': """
        modulo para manejar:
        - platos
        - menus
    """,

    'author': "Daniel Pérez Benítez",

    'website': "https://github.com/danipxbz/Python-Gestion.git",

    'category': 'Test',

    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}