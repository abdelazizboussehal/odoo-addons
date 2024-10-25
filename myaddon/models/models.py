# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MyOder(models.Model):
    _name = 'my.order'
    _description = 'this is my order model for my own business'
    name = fields.Char(required=True)
    order_date = fields.Datetime()
    total_amount = fields.Float()
    quantity = fields.Integer(default=30)
    selection = fields.Selection([('1', 'csc'), ('2', 'mokkkkc'), ('3', 'ask')], default='2')
    order_line_ids = fields.One2many('my.order.line', 'order_id', domain=[('quantity', '>', 30)])
    html = fields.Html(string='html test', default='<p> aziz text </p>')
    minus = fields.Float(string="minus", compute='_compute_minus')
    app_barre_status = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')],
                                        default="draft")

    @api.depends('quantity', 'total_amount')
    def _compute_minus(self):
        for record in self:
            record.minus = record.total_amount - record.quantity

    def change_to_completed(self):
        self.app_barre_status = "confirmed"

    def add_new_order_line(self):
        self.env['my.order.line'].create({
            'order_id': self.id,
            'unit_price': 1200.00,
            'quantity': 53
        })

    def remove_all_order_line(self):
        self.env['my.order.line'].search([('order_id', '=', self.id)]).unlink()

    def empty_quantity(self):
        self.env['my.order.line'].search([('order_id', '=', self.id)]).write({'quantity': 50})


class OrderLine(models.Model):
    _name = 'my.order.line'
    _description = 'this is my order model for my own business'

    order_id = fields.Many2one('my.order', ondelete='cascade')
    quantity = fields.Integer()
    unit_price = fields.Float()
    subtotal = fields.Float(string='Subtotal')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
