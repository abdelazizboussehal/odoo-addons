from odoo import models, fields, api, _
from datetime import date
from odoo.exceptions import ValidationError


class Person(models.Model):
    _name = 'my.person'
    _description = 'this is my order model for my own business'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    fullname = fields.Char(string="full name", required=True)
    email = fields.Char(string="Email Pro")
    phone = fields.Char(string="phone Number", default="+9112345678")
    address = fields.Char(string="address", tracking=True)
    date_of_birth = fields.Date(string="date of birth")
    age = fields.Integer(string="age")
    _sql_constraints = [
        ("my_person_name_not_null", "unique(fullname)", "fullname must be unique")
    ]

    @api.constrains("age")
    def my_person_age_under_one_hundred(self):
        if self.age > 100:
            raise ValidationError(_("age must be less than 100"))

    @api.onchange("date_of_birth")
    def onchange_date_of_birth(self):
        today = date.today()
        if self.date_of_birth:
            self.age = today.year - self.date_of_birth.year
