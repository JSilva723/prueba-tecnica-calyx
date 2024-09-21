# -*- coding: utf-8 -*-
from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_group_ids = fields.Many2many(comodel_name='calyx_technical_test.credit_group', string=_('Credit group'))
    credit_control = fields.Boolean(string=_('Credit control'))

    @api.constrains('credit_control', 'credit_group_ids')
    def _check_credit_group(self):
        for partner in self:
            if partner.credit_control and not partner.credit_group_ids:
                raise ValidationError('You must assign at least one credit group if credit control is enabled.')