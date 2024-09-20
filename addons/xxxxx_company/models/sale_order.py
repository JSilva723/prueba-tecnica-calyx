# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    channel_id = fields.Many2one(comodel_name='xxxxx_company.sale_channel', string=_('Sale channel'), required=True)

    @api.onchange('channel_id')
    def _onchange_channel_id(self):
        self.warehouse_id = self.channel_id.warehouse_id

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        for order in self:
            order._create_delivery()

    def _create_delivery(self):
        pickings = self.env['stock.picking']
        for order in self:
            picking_vals = order._prepare_picking()
            picking = pickings.create(picking_vals)
            picking.action_confirm()

    def _prepare_picking(self):
        self.ensure_one()
        picking_type = self.warehouse_id.out_type_id
        return {
            'picking_type_id': picking_type.id,
            'partner_id': self.partner_shipping_id.id,
            'origin': self.name,
            'location_dest_id': self.partner_shipping_id.property_stock_customer.id,
            'location_id': picking_type.default_location_src_id.id,
            'channel_id': self.channel_id.id,
        }