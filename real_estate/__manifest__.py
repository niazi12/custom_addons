# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Niazi",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Practice',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','sale','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'wizard/wizards.xml',
        'views/views.xml',
        'views/em_view.xml',
        'views/templates.xml',
        'views/partner_view.xml',
        'views/web_form.xml',
        'reports/report.xml',
        'reports/sale_report_inherit.xml',
        'reports/function.xml',
        'reports/normal_report.xml',
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
