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

import json
from urlparse import urljoin

import werkzeug.utils

from openerp import http
from openerp.addons.web.http import request
from openerp import SUPERUSER_ID


class MenuPopup(http.Controller):

    @http.route('/menupopup/load_menu_popup_active', type='json', auth="user")
    def load_menu_popup_active(self, **kw):
        
        cr, uid = request.cr, SUPERUSER_ID
        menu_popup = request.registry['menu.popup']
        menu_popup_line = request.registry['menu.popup.line']
        list_item = False

        menu_popup_id = menu_popup.search(cr, uid, [('active', '=', True)])
        if menu_popup_id and len(menu_popup_id) > 0 and menu_popup_id[0]:
            base_url = request.registry['ir.config_parameter'].get_param(cr, uid, 'web.base.url')
            menu_popup_id = menu_popup_id[0]
            menu_popup_line_ids = menu_popup_line.search(cr, uid, [('menu_popup_id', '=', menu_popup_id)])

            if menu_popup_line_ids:
                list_item = []
                for line in menu_popup_line.browse(cr, uid, menu_popup_line_ids):
                    item = {
                        'desc': line.description or ''
                    }
                    if line.video_link:
                        if line.is_web_link:
                            item.update({
                                'url': line.video_link,
                                'image': urljoin(base_url, "/web/binary/image?model=%s&field=%s&id=%s" % ('menu.popup.line', 'image', line.id)),
                                'type': 'website'
                            })  
                        else:
                            item.update({
                                'url': line.video_link,
                                'type': 'video'
                            })
                    else:
                        item.update({
                            'url': urljoin(base_url, "/web/binary/image?model=%s&field=%s&id=%s" % ('menu.popup.line', 'image', line.id)),
                            'type': 'image'
                        })
                    list_item.append(item)
            
        return list_item
