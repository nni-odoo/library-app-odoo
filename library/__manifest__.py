# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Library',
    'version': '1.0',
    'summary': 'Library',
    'description': """
        Library
    """,
    'depends': ['base', 'contacts'],
    'data': [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/library_book.xml",
        "views/library_rental.xml",
        "views/res_partner.xml",
        "views/menus.xml",
        "views/report_contact_rentals.xml",
        "views/template_book.xml",
        "security/ir_rule.xml",
    ],
    'license': 'LGPL-3',
}
