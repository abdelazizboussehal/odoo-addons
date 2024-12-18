# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule_appointment.xml',
        'wizards/add_appointment.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/appointment.xml',
        'views/medicine.xml',
        'views/custom_kanban_sidebar.xml',
        'report/report.xml',
        'views/menu_hospital.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hospital/static/src/components/*/*.js',
            'hospital/static/src/components/*/*.xml',
            'hospital/static/src/components/*/*.scss',
        ]
    }
}

