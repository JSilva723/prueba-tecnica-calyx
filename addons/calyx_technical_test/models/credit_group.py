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

    @api.constrains('code')
    def _check_code_restriction(self):
        for record in self:
            if '026' in record.code:
                raise ValidationError('The code cannot contain the sequence 026.')
