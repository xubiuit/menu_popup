'use strict';

$(document).ready(function() {
	
	$('.menu_popup').on('click', function(e) {
		
		load_menu_popup_active();
	});
	
	function load_menu_popup_active() {
		
		openerp.jsonRpc(

			    '/menupopup/load_menu_popup_active', 'call', {}

			).then(function (results) {
				
				if (results) {
					
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
				}
			});
	}
	
});
