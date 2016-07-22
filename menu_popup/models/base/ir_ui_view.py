# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo Menu Popup
#    Copyright (C) 2016- XUBI.ME (http://www.xubi.me)
#    @author binhnguyenxuan (https://www.linkedin.com/in/binhnguyenxuan)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#    
#
##############################################################################

from openerp import api
from openerp.osv import osv
from openerp import SUPERUSER_ID


class view(osv.osv):
    _inherit = "ir.ui.view"

    @api.cr_uid_ids_context
    def render(self, cr, uid, id_or_xml_id, values=None, engine='ir.qweb', context=None):
        if context is None:
            context = {}
        if not values:
            values = {}

        # Menu popup
        menu_popup_ids = self.pool['menu.popup'].search(cr, SUPERUSER_ID, [('active', '=', True)])
        if menu_popup_ids:
            menu_popup = self.pool['menu.popup'].browse(cr, SUPERUSER_ID, menu_popup_ids[0])
            values.update({'menu_popup': menu_popup})
        return super(view, self).render(cr, uid, id_or_xml_id, values=values, engine=engine, context=context)
