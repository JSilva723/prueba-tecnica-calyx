# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model_create_multi
    def create(self, vals_list):
        res = super(AccountMove, self).create(vals_list)
        journal_id = res.line_ids.sale_line_ids.order_id.channel_id.journal_id
        if journal_id and journal_id.type == 'sale': 
            res.journal_id = journal_id

        return res