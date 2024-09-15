# -*- coding: utf-8 -*-
# Part of Odoo, actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'PayuMoney Payment Acquirer',
    'author': 'Odoo S.A',
    'category': 'Payment Acquirer',
    'summary': 'Payment Acquirer: PayuMoney Implementation',
    'description': """
    PayuMoney Payment Acquirer for India.

    PayUmoney payment gateway supports only INR currency.
    """,
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_payumoney_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
}
