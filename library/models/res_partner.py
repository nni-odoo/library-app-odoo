from odoo import api, fields, models

class ResParnter(models.Model):
    _inherit = "res.partner"

    rented_books = fields.One2many("library.rental", "renter")
