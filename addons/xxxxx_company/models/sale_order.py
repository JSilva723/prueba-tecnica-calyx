# -*- coding: utf-8 -*-
from odoo import models, fields, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    channel_id = fields.Many2one('xxxxx_company.sale_channel', string=_('Sale channeñ'))