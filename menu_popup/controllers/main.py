# -*- coding: utf-8 -*-
import json
from itertools import islice
import base64
import logging
import time
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
        menu_popup_items = []
        list_item = []

        base_url = request.registry['ir.config_parameter'].get_param(cr, uid, 'web.base.url')
        menu_popup_id = menu_popup.search(cr, uid, [('active', '=', True)])[0]
        if menu_popup_id:
            menu_popup_line_ids = menu_popup_line.search(cr, uid, [('menu_popup_id', '=', menu_popup_id)])
            
        
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