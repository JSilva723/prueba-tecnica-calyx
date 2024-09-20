# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    channel_id = fields.Many2one(comodel_name='xxxxx_company.sale_channel', string=_('Sale channel'), compute='_compute_channel_id')

    @api.depends('origin')
    def _compute_channel_id(self):
        SaleOrder = self.env['sale.order'].sudo()
        for rec in self:
            channel_id = False
            if rec.origin:
                sale_order_id = SaleOrder.search([('name', '=', rec.origin)])
                if sale_order_id and sale_order_id.channel_id:
                    channel_id = sale_order_id.channel_id.id
            rec.channel_id = channel_id
