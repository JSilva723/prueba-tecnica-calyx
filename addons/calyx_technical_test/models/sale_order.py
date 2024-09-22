# -*- coding: utf-8 -*-
from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    _CREDIT_STATUS = [
        ('no_limit',  _('No limit')),
        ('available', _('Available')),
        ('blocked', _('Blocked')),
    ]

    channel_id = fields.Many2one(comodel_name='calyx_technical_test.sale_channel', string=_('Sale channel'), required=True)
    credit_status = fields.Selection(
        selection=_CREDIT_STATUS,
        string=_('Credit'),
        compute='_check_credit_status',
        default='no_limit',
        readonly=True,
    )

    @api.onchange('channel_id')
    def _onchange_channel_id(self):
        self.warehouse_id = self.channel_id.warehouse_id
 
    @api.depends('partner_id', 'channel_id', 'order_line')
    def _check_credit_status(self):
        self.credit_status = 'no_limit'

        if self.partner_id and self.channel_id:
            # Filter groups by channel
            credit_groups = self.partner_id.credit_group_ids.filtered(lambda g: g.channel_id == self.channel_id)
            
            if credit_groups:
                is_available = False

                # Search credit available in group
                for group in credit_groups:
                    if self.amount_total <= group.credit_available:
                        is_available = True
                        break

                self.credit_status = 'available' if is_available else 'blocked'

    def action_confirm(self):
        for order in self:
            if order.credit_status == 'blocked':
                raise ValidationError(_('You cannot confirm the sale order because the customer\'s credit is blocked.'))
        return super(SaleOrder, self).action_confirm()