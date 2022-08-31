from odoo import api, fields, models
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import datetime

class LibraryRental(models.Model):
    _name = "library.rental"

    # renter = fields.Char("Renter")
    renter = fields.Many2one("res.partner", "Renter")
    book = fields.Many2one("library.book")
    date_rent = fields.Date("Rental Date")
    date_end = fields.Date("Max Return Date")

    overdue_fee = fields.Float("Overdue Fee", compute="_compute_overdue_fee")

    def _compute_overdue_fee(self):
        today = fields.Date.today()
        for rec in self:
            rec['overdue_fee'] = 0
            if rec.date_end and today > rec.date_end:
                days_overdue = (today - rec.date_end).days
                rec['overdue_fee'] = days_overdue * 2

    @api.constrains('date_rent', 'date_end')
    def _constraint_date(self):
        for rec in self:
            if rec.date_rent and rec.date_end and rec.date_end < rec.date_rent:
                raise ValidationError("End date should be later than the start date")

    @api.model
    def create(self, vals):
        today = fields.Date.today()
        end_day = today + relativedelta(months=1)
        vals['date_rent'] = today
        vals['date_end'] = end_day
        return super().create(vals)
