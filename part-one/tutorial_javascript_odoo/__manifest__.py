# -*- coding: utf-8 -*-
{
    'name': "Odoo JavaScript Programming Tutorial",
    'summary': """
        Tutorial about how to create and use Javascript files in Odoo""",
    'description': """
        This module is a tutorial in the form of an app. In this app you can find the code to create and use
        JavaScript functionalities in Odoo 13.

        Sources:
            - https://en.ngasturi.id/2021/04/24/odoo-javascript-programming-tutorial-part-one-create-widget-view/
    """,
    'version': '13.0.0.1',
    'author': 'Ngasturi',
    'support': 'z.nry27@gmail.com',
    'website': 'https://en.ngasturi.id/',
    'license': 'LGPL-3',
    'maintainer': 'Leonardo J. Caballero G. <leonardocaballero@gmail.com>',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorial',
    # Any module necessary for this one to work correctly
    'depends': [
        'base',
        'web'
    ],
    # Always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/views.xml'
    ],
    # Only loaded in demonstration mode
    'demo': [],
    # QWeb templates
    'qweb': [
        'static/src/xml/widget_one_template.xml'
    ],
    'images': [
        'static/description/icon.png'
    ],
    'application': True,
    'installable': True
}

