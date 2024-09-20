# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    channel_id = fields.Many2one(comodel_name='calyx_technical_test.sale_channel', string=_('Sale channel'))

    @api.model_create_multi
    def create(self, vals_list):
        res = super(StockPicking, self).create(vals_list)

        SaleOrder = self.env['sale.order'].sudo()
        for rec in res:
            if rec.origin:
                sale_order_id = SaleOrder.search([('name', '=', rec.origin)])
                if sale_order_id and sale_order_id.channel_id:
                    rec.channel_id = sale_order_id.channel_id

        return res
