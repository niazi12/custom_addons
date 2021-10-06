# -*- coding: utf-8 -*-
{
    'name': "Niazi_Academy",

    'summary': 'learning',

    'description': """
        Long description of module's purpose
    """,

    'author': "Niazi Mahrab",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'app',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/shop.xml',
        'views/web.xml',
        'views/templates.xml',
        'views/course.xml',
        'views/student.xml',
        'views/admin.xml',
        'views/faculty.xml',
        'views/front_view_website.xml'
       
        
      
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}
