# -*- coding: utf-8 -*-
import datetime
from odoo import http, api, SUPERUSER_ID
from odoo.http import request
import json

class Controllers(http.Controller):
    @http.route("/books")
    def books(self, **kw):
        books = request.env['library.book'].search([('copies', '>', 0)])
        values = {"books": books}
        return request.render('library.books', values)

    @http.route("/fines")
    def fines(self, **kw):
        rental_groups = request.env['library.rental'].read_group([], ['overdue_fee:sum'], ['renter'])
        user_fee = {}
        for group in rental_groups:
            user_fee[group['renter'][0]] = group['overdue_fee']
        return json.dumps(user_fee)

    @http.route("/overdue")
    def overdue(self, **kw):
        highest_rent = request.env['library.rental'].search([], order="overdue_fee desc", limit=1)
        return "%s" % highest_rent.overdue_fee
