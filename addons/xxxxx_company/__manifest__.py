# -*- coding: utf-8 -*-
{
    'name': "xxxxx_company",
    'summary': "system to manage different sales channels in order to control the sales made",
    'author': "Jonatan Silva",
    'website': "https://www.linkedin.com/in/jsilva723",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'sale',
        'stock',
        'account',
        'l10n_ar',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/channels_of_sale_sequence.xml',
        'views/channels.xml',
        'views/sale_order.xml',
    ],
    'demo': [],
    'application': True,
}
