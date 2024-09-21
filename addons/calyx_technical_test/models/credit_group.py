# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CreditGruop(models.Model):
    _name = 'calyx_technical_test.credit_group'
    _description = 'calyx_technical_test.credit_group'

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'The code must be unique.')
    ]

    name = fields.Char(string=_('Name'), required=True)
    code = fields.Char(string=_('Code'), required=True)
    channel_id = fields.Many2one(comodel_name='calyx_technical_test.sale_channel', string=_('Sale channel'), required=True)
    company_id = fields.Many2one('res.company', string=_('Company'), required=True, default=lambda self: self.env.company)
    company_currency_id = fields.Many2one(comodel_name='res.currency', string=_('Company Coin'), related='company_id.currency_id', readonly=True, store=True)
    credit_global = fields.Monetary(string=_('Global credit'), currency_field='company_currency_id', required=True)

    @api.constrains('code')
    def _check_code_restriction(self):
        for record in self:
            if '026' in record.code:
                raise ValidationError('The code cannot contain the sequence 026.')
