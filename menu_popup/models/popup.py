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


from openerp import models, fields, api


class popup(models.Model):
    _name = 'menu.popup'

    name = fields.Char('Name', required=True)
    active = fields.Boolean('Active', default=True)
    lines = fields.One2many(
        'menu.popup.line', 'menu_popup_id', string='Popup lines')

    @api.model
    def create(self, vals):
        if vals and vals.get('active', False):
            self._auto_deactive_menu()
        return super(popup, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals and vals.get('active', False):
            self._auto_deactive_menu()
        return super(popup, self).write(vals)

    @api.model
    def _auto_deactive_menu(self):
        query = """ update menu_popup
                    set active = 'f'
                """
        self._cr.execute(query)
        return True


class popup_line(models.Model):
    _name = 'menu.popup.line'

    video_link = fields.Char(
        'URL', help="""* Video: Supported youtube, vimeo.
                       \n* URL (web page): display a iframe base on URL input.
                      """)
    image = fields.Binary('Image',
                          help="""* Image: used for thumbnail.
                       \n* Video: not required.
                       \n* URL (web page): used for thumbnail.
                      """)
    description = fields.Text('Description')
    sequence = fields.Integer('Sequence')
    menu_popup_id = fields.Many2one('menu.popup', string='Popup')
    is_web_link = fields.Boolean('Is Website Link', default=False)
    
    _order = 'sequence asc'
