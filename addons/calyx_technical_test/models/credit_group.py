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

    partner_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='res_partner_credit_group_rel',
        column1='credit_group_id',
        column2='partner_id',
        string=_('Custmers'),
    )

    @api.constrains('code')
    def _check_code_restriction(self):
        for rec in self:
            if '026' in rec.code:
                raise ValidationError('The code cannot contain the sequence 026.')

    @api.depends('channel_id')
    def _compute_credit_used(self):
        for rec in self:
            total_sales = 0.0
            total_not_paid_invoices = 0.0

            sales_orders = self.env['sale.order'].search([
                ('state', 'in', ['sale', 'done']),
                ('channel_id', '=', rec.channel_id.id),
                ('partner_id', 'in', rec.partner_ids.ids)
            ])

            for order in sales_orders:
                if order.currency_id != rec.company_currency_id:
                    total_sales += order.currency_id._convert(order.amount_total, rec.company_currency_id, rec.company_id, order.date_order)
                else:
                    total_sales += order.amount_total

            not_paid_invoices = self.env['account.move'].search([
                ('state', '=', 'posted'),
                ('payment_state', 'in', ['not_paid']),
                ('channel_id', '=', rec.channel_id.id),
                ('partner_id', 'in', rec.partner_ids.ids)
            ])

            for invoice in not_paid_invoices:
                if invoice.currency_id != rec.company_currency_id:
                    total_not_paid_invoices += invoice.currency_id._convert(invoice.amount_residual, rec.company_currency_id, rec.company_id, invoice.invoice_date)
                else:
                    total_not_paid_invoices += invoice.amount_residual

            rec.credit_used = total_sales + total_not_paid_invoices

    @api.depends('credit_global', 'credit_used')
    def _compute_credit_available(self):
        for record in self:
            record.credit_available = record.credit_global - record.credit_used

    def get_report_data(self):
        self.ensure_one()

        partners_data = []
        for partner in self.partner_ids:
            partners_data.append({
                'name': partner.name,
                'document_number': partner.vat,
                'phone': partner.phone if partner.phone else '--',
                'email': partner.email if partner.email else '--',
            })

        sale_orders_data = []
        sale_orders = self.env['sale.order'].search([
            ('partner_id', 'in', self.partner_ids.ids),
            ('state', '=', 'sale')
        ])
        for order in sale_orders:
            sale_orders_data.append({
                'name': order.name,
                'date_order': order.date_order,
                'amount_total': order.amount_total,
            })

        invoices_data = []
        invoices = self.env['account.move'].search([
            ('partner_id', 'in', self.partner_ids.ids),
            ('move_type', '=', 'out_invoice'),
            ('payment_state', '!=', 'paid')
        ])
        for invoice in invoices:
            invoices_data.append({
                'name': invoice.name,
                'invoice_date': invoice.invoice_date,
                'amount_residual': invoice.amount_residual,
            })

        return {
            'group_name': self.name,
            'group_code': self.code,
            'channel': self.channel_id.name,
            'partners': partners_data,
            'sale_orders': sale_orders_data,
            'invoices': invoices_data,
        }
