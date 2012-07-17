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
        'install_invoice': fields.boolean('Facturación Argentina', required=True),
        'install_bank': fields.boolean('Bancos de la Argentina', required=True),
        'install_vat': fields.boolean('Verificación de CUIT', required=True),
        'install_partner_title': fields.boolean('Denominaciones de Relaciones Comerciales', required=True),
        'install_states': fields.boolean('Provincias Argentinas', required=True),
        'install_treasury': fields.boolean('Cartera de Cheques', required=True),
    }

    _defaults= {
        'install_invoice': True,
        'install_bank': True,
        'install_vat': True,
        'install_partner_title': True,
        'install_states': True,
        'install_treasury': True,
    }

    def modules_to_install(self, cr, uid, ids, context=None):
        modules = super(account_modules_ar_installer, self).modules_to_install(
            cr, uid, ids, context=context)

        modules_ar = set()
        for res in self.read(cr, uid, ids, context=context):
            modules_ar |= set(['l10n_ar_invoice']) if res['install_invoice'] else set()
            modules_ar |= set(['l10n_ar_bank']) if res['install_bank'] else set()
            modules_ar |= set(['l10n_ar_base_vat']) if res['install_vat'] else set()
            modules_ar |= set(['l10n_ar_partner_title']) if res['install_partner_title'] else set()
            modules_ar |= set(['l10n_ar_states']) if res['install_states'] else set()
            modules_ar |= set(['treasury']) if res['install_treasury'] else set()

        self.logger.notifyChannel(
            'installer', netsvc.LOG_DEBUG,
            'Installing modules %s'%modules_ar)
        return modules | modules_ar

account_modules_ar_installer()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
