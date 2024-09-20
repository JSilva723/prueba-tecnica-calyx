# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    channel_id = fields.Many2one(comodel_name='calyx_technical_test.sale_channel', string=_('Sale channel'), required=True)

    @api.onchange('channel_id')
    def _onchange_channel_id(self):
        self.warehouse_id = self.channel_id.warehouse_id