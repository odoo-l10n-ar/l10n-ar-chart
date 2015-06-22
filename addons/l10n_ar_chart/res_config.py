# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class account_config_settings(osv.osv_memory):
    _name = 'account.config.settings'
    _inherit = 'account.config.settings'

    _columns = {
        'module_l10n_ar_invoice': fields.boolean(
            'Argentine Basic Invoice',
            help='Basic invoce data, logic and printing for Argentine.'
            ' This installs the module l10n_ar_invoice'),
        'module_l10n_ar_wsafip_fe': fields.boolean(
            'Argentine Electronic Invoice',
            help='Enable invoices to be generated using AFIP web services.'
            ' This installs the module l10n_ar_wsafip_fe'),
        'module_l10n_ar_bank': fields.boolean(
            'Argentine Banks',
            help='Complete the bank database, and let you complete the'
            ' argentine bank list using BNA list by internet.'
            ' This install the module l10n_ar_banks'),
    }

account_config_settings()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
