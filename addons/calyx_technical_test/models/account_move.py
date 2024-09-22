# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    channel_id = fields.Many2one(comodel_name='calyx_technical_test.sale_channel', string=_('Sale channel'))

    @api.model_create_multi
    def create(self, vals_list):
        res = super(AccountMove, self).create(vals_list)
        # Get channel from sale order
        channel_id = res.line_ids.sale_line_ids.order_id.channel_id
        # Set channel in invoice
        res.channel_id = channel_id
        # If journal exist in channel and type is sale, set journal in invoice
        journal_id = channel_id.journal_id
        if journal_id and journal_id.type == 'sale': 
            res.journal_id = journal_id.id

        return res