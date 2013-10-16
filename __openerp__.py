{
    'name' : 'Maintenance',
    'version' : '0.1',
    'author' : 'Emad Shaaban',
    'sequence': 110,
    'description' : """
Maintenance
==================================
Bla Bla Bla

""",
    'depends' : [
        'base',
        'mail',
        'board',
        'hr',
    ],
    'data' : [
        'maintenance_view.xml',
        'maintenance_conf_view.xml',
        'maintenance_menus.xml',
    ],
    
    'installable' : True,
    'application' : True,
    'auto_install': False,
}
