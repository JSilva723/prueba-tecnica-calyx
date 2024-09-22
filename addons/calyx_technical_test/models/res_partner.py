# -*- coding: utf-8 -*-
from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_control = fields.Boolean(string=_('Credit control'))
    credit_group_ids = fields.Many2many(
        comodel_name='calyx_technical_test.credit_group',
        relation='res_partner_credit_group_rel',
        column1='partner_id',
        column2='credit_group_id',
        string=_('Credit group'),
    )

    @api.constrains('credit_control', 'credit_group_ids')
    def _check_credit_group(self):
        for rec in self:
            if rec.credit_control and not rec.credit_group_ids:
                raise ValidationError('You must assign at least one credit group if credit control is enabled.')

    @api.onchange('credit_control')
    def remove_credit_group_ids(self):
        for rec in self:
            if not rec.credit_control:
                rec.credit_group_ids = None