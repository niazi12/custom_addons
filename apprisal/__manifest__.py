# -*- coding: utf-8 -*-
{
    'name': "Appraisal",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Niazi Mahrab",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/group.xml',
        'views/employee_view.xml',
        'views/menus.xml',
        'views/apprisal_view.xml',
        'views/reporting_view.xml',
        'views/goals_view.xml',
        'views/meeting_view.xml',
        'reports/print_report.xml',
        'reports/report.xml',
        'views/status_change.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
