odoo.define('menu_popup.menu_popup_active', function (require) {
"use strict";

	var core = require('web.core');
	var ajax = require('web.ajax');
	var Dialog = require('web.Dialog');

	var QWeb = core.qweb;
	var _t = core._t;

	$(document).ready(function() {
		
		$('.menu_popup').on('click', function(e) {
			
			load_menu_popup_active();
		});
		
		function load_menu_popup_active() {
			
			return ajax.jsonRpc(
	
				    '/menupopup/load_menu_popup_active', 'call', {}
	
				).then(function (results) {
					
					if (results || results.length > 0) {
						
						var html = '';
						_.each(results, function(item) {
							if (item['type'] == 'image') {
								html += '<a href="'+ item['url'] +'" title="'+ item['desc'] +'">'+ item['desc'] +'</a>';
							} else if (item['type'] == 'video') {
								html += '<a class="swipebox-video" href="'+ item['url'] +'" title="'+ item['desc'] +'">'+ item['desc'] +'</a>';
							} else if (item['type'] == 'website') {
								html += '<a class="swipebox-video" href="'+ item['url'] +'" title="'+ item['desc'] +'" data-image-url="'+ item['image'] +'">'+ item['desc'] +'</a>';
							}
						});
						
						$('.menu_popup_image').html(html);
						
						$( '.menu_popup_image a' ).swipebox();
						
						$(".menu_popup_image a").first().trigger( "click" );
					} else {

						var dialog = new Dialog(self, {
			                title: _t("Warning !!!"),
			                buttons: [{text: _t("OK"), close: true}],
			                $content: '<div>Please config your content at Popup menu</div>',
			            }).open();
					}
				});
		}
		
	});

});
