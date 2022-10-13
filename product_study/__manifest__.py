# -*- coding: utf-8 -*-
{
    'name': "Enmasys Study Project",
    'summary': "",
    'description': "",
    'author': "",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base',
        'product',
    ],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/project_study_views.xml',
        'security/security.xml',

    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}