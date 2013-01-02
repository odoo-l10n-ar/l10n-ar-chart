# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv
import netsvc

class account_modules_ar_installer(osv.osv_memory):
    _name = 'account.modules.ar.installer'
    _inherit = 'res.config.installer'
    _columns = {
        'l10n_ar_invoice': fields.boolean(u'Facturación Argentina', required=True),
        'l10n_ar_bank': fields.boolean(u'Bancos de la Argentina', required=True),
        'l10n_ar_base_vat': fields.boolean(u'Verificación de CUIT', required=True),
        'l10n_ar_partner_title': fields.boolean(u'Denominaciones de Relaciones Comerciales', required=True),
        'l10n_ar_states': fields.boolean(u'Provincias Argentinas', required=True),
        'treasury': fields.boolean(u'Cartera de Cheques', required=True),
    }

    _defaults= {
        'l10n_ar_invoice': True,
        'l10n_ar_bank': True,
        'l10n_ar_base_vat': True,
        'l10n_ar_partner_title': True,
        'l10n_ar_states': True,
        'treasury': True,
    }

account_modules_ar_installer()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
