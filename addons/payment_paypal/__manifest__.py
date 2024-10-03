# -*- coding: utf-8 -*-

{
    'name': 'Paypal Payment Acquirer',
    'author': 'Odoo S.A',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Paypal Implementation',
    'version': '1.0',
    'description': """Paypal Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_paypal_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
}