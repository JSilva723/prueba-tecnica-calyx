# -*- coding: utf-8 -*-
from odoo import models, fields, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    channel_id = fields.Many2one('xxxxx_company.channels_of_sale', string=_('Channel of sale'))