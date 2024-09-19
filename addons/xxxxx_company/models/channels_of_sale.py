# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class ChannelsOfSale(models.Model):
    _name = 'xxxxx_company.channels_of_sale'
    _description = 'xxxxx_company.channels_of_sale'

    name = fields.Char(string=_('Name'), required=True)
    code = fields.Char(string=_('Code'), readonly=True, copy=False, default='New')
    warehouse_id = fields.Many2one("stock.warehouse", string=_('Warehouse'))

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('xxxxx_company.channels_of_sale') or 'New'
        return super(ChannelsOfSale, self).create(vals)