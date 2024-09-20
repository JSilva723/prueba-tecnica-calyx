# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class SaleChannel(models.Model):
    _name = 'calyx_technical_test.sale_channel'
    _description = 'calyx_technical_test.sale_channel'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string=_('Name'), required=True, track_visibility='onchange')
    code = fields.Char(string=_('Code'), readonly=True, copy=False, default='New')
    warehouse_id = fields.Many2one(comodel_name='stock.warehouse', string=_('Warehouse'))
    journal_id = fields.Many2one(comodel_name='account.journal', string=_('Journal'))

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('calyx_technical_test.sale_channel') or 'New'
        return super(SaleChannel, self).create(vals)