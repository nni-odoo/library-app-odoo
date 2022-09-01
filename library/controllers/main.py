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
