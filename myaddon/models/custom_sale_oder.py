from odoo import models, fields, api


class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'
    shopy_url = fields.Char(string='Shopy URL', default='http://shopy')

    @api.onchange('shopy_url')
    def _shopy_url(self):
        for order in self:
            order.incoterm_location = self.shopy_url

