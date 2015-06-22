# -*- coding: utf-8 -*-
{
    'name': 'Argentina - Plan Contable General',
    'version': '8.0.1.1',
    'author':   'Otra localización argentina de Odoo.',
    'category': 'Localization/Account Charts',
    'website':  'https://launchpad.net/~openerp-l10n-ar-localization',
    'license': 'AGPL-3',
    'description': """
Plan contable genérico para la Argentina.

Incluye:
  - Wizard de configuración.
  - Plantilla del plan contable genérico.

""",
    'depends': [
        'account',
        'base_vat',
        'base_iban',
        'account_chart',
        'l10n_ar_states',
        'l10n_ar_base_vat',
    ],
    'init_xml': [],
    'demo_xml': [],
    'test': [],
    'data': [
        'data/account_types.xml',
        'data/account_chart_respinsc.xml',
        'data/res_config_view.xml',
        'data/res_partner.xml',
    ],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
