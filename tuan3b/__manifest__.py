# -*- coding: utf-8 -*-
{
    'name': "Tuan3b Task manager",
    'summary': "",
    'description': "Use object staff (users)",
    'author': "",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/root_menu.xml',
        'views/project_views.xml',
        'views/task_views.xml',
        'views/staff_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}