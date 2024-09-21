# -*- coding: utf-8 -*-
from odoo import models, fields, _, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_group_id = fields.Many2one(comodel_name='calyx_technical_test.credit_group', string=_('Credit group'))