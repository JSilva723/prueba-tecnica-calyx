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
    company_id = fields.Many2one(comodel_name='res.company', string=_('Company'), required=True, default=lambda self: self.env.company)
    company_currency_id = fields.Many2one(comodel_name='res.currency', string=_('Company Coin'), related='company_id.currency_id', readonly=True, store=True)
    credit_global = fields.Monetary(string=_('Global credit'), currency_field='company_currency_id', required=True)
    credit_used = fields.Monetary(string=_('Credit used'), compute='_compute_credit_used', currency_field='company_currency_id')
    credit_available = fields.Monetary(string=_('Credit available'), compute='_compute_credit_available', currency_field='company_currency_id')

    @api.constrains('code')
    def _check_code_restriction(self):
        for rec in self:
            if '026' in rec.code:
                raise ValidationError('The code cannot contain the sequence 026.')

    def _get_customers_ids(self):
        customers = self.env['res.partner'].search([('credit_group_ids', '=', self.id)])
        return customers.ids
    
    @api.depends('channel_id')
    def _compute_credit_used(self):
        for rec in self:
            total_sales = 0.0
            total_not_paid_invoices = 0.0

            sales_orders = self.env['sale.order'].search([
                ('state', 'in', ['sale', 'done']),
                ('channel_id', '=', rec.channel_id.id),
                ('partner_id', 'in', rec._get_customers_ids())
            ])

            for order in sales_orders:
                if order.currency_id != rec.company_currency_id:
                    total_sales += order.currency_id._convert(order.amount_total, rec.company_currency_id, rec.company_id, order.date_order)
                else:
                    total_sales += order.amount_total

            unpaid_not_paid_invoices = self.env['account.move'].search([
                ('state', '=', 'posted'),
                ('payment_state', 'in', ['not_paid']),
                ('partner_id', 'in', rec._get_customers_ids())
            ])

            for invoice in unpaid_not_paid_invoices:
                if invoice.currency_id != rec.company_currency_id:
                    total_not_paid_invoices += invoice.currency_id._convert(invoice.amount_residual, rec.company_currency_id, rec.company_id, invoice.invoice_date)
                else:
                    total_not_paid_invoices += invoice.amount_residual

            rec.credit_used = total_sales + total_not_paid_invoices

    @api.depends('credit_global', 'credit_used')
    def _compute_credit_available(self):
        for record in self:
            record.credit_available = record.credit_global - record.credit_used
