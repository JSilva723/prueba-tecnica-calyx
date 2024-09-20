# -*- coding: utf-8 -*-
{
    'name': "calyx_technical_test",
    'summary': "system to manage different sales channels in order to control the sales made",
    'author': "Jonatan Silva",
    'website': "https://www.linkedin.com/in/jsilva723",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'account',
        'base',
        'l10n_ar',
        'sale_management',
        'sale',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sale_channel_sequence.xml',
        'views/sale_channel.xml',
        'views/credit_group.xml',
        'views/stock_picking.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
}
