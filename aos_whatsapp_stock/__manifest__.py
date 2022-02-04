# See LICENSE file for full copyright and licensing details.

{
    'name': 'Whatsapp Stock',
    'version': '14.0.0.1.0',
    'license': 'OPL-1',
    'author': "Alphasoft",
    'sequence': 1,
    'website': 'https://www.alphasoft.co.id/',
    'images':  ['images/main_screenshot.png'],
    'summary': 'This module is used for Whatsapp Stock',
    'category': 'Extra Tools',
    'depends': ['base_automation', 'stock', 'aos_whatsapp'],
    'data': [
        'data/stock_data.xml',
    ],
    'external_dependencies': {'python': ['html2text']},
    'demo': [],
    'test': [],
    'css': [],
    'js': [],
    'price': 0,
    'currency': 'EUR',
    'installable': True,
    'application': False,
    'auto_install': False,
}
