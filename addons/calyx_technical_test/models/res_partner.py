# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_group_ids = fields.Many2many(comodel_name='calyx_technical_test.credit_group', string=_('Credit group'))
    credit_control = fields.Boolean(string=_('Credit control'))