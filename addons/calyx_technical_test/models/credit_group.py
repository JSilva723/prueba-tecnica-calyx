# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class CreditGruop(models.Model):
    _name = 'calyx_technical_test.credit_group'
    _description = 'calyx_technical_test.credit_group'

    name = fields.Char(string=_('Name'), required=True)
