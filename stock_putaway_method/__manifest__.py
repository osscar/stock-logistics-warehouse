# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Putaway strategy method',
    'summary': 'Add the putaway strategy method back, '
               'removed from the stock module in Odoo 11',
    'version': '11.0.1.0.1',
    'category': 'Inventory',
    'website': 'https://github.com/OCA/stock-logistics-warehouse',
    'author': 'Camptocamp SA, '
              'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'product',
        'stock'
    ],
    'data': [
        'views/product_strategy_views.xml'
    ],
    'demo': []
}
