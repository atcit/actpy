# Part of actpy See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Indent',
    'version': '1.0',
    'category': 'Purchase',
    'sequence': 10,
    'summary': 'Purchase Indent',
    'description': """
        Purchase Indent and Agreements""",
    'author': 'actpy',
    'website': 'https://www.actpy.com/',
    'depends': [
        'purchase',
        'purchase_requisition',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/purchase_indent_security.xml',
        'wizard/wiz_requisition_request_view.xml',
        'views/purchase_indent_view.xml',
        'report/purchase_indent_reports.xml',
        'report/purchase_indent_template.xml',
    ],
    'demo': [
        'demo/puchase_indent_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
