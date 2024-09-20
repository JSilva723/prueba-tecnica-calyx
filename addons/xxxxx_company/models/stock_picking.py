# -*- coding: utf-8 -*-
from odoo import models, fields, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    channel_id = fields.Many2one(comodel_name='xxxxx_company.sale_channel', string=_('Sale channel'))