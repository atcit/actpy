# Part of actpy. See LICENSE file for full copyright and licensing details.

{
    'name': 'REST API For actpy',
    'version': '1.0.0',
    'category': 'API',
    'author': 'actpy',
    'website': 'https://www.actpy.com',
    'summary': 'REST API For actpy',
    'description': """
REST API For actpy
====================
With use of this module user can enable REST API in any actpy applications/modules

For detailed example of REST API refer *readme.md*
""",
    'depends': [
        'web',
    ],
    'data': [
        'data/ir_configparameter_data.xml',
        'views/ir_model_view.xml',
        'views/res_user_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
