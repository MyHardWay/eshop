


// Добавляет товар в корзину
function makePurchase(id) {
	var csrftoken = getCookie('csrftoken');
	 $.ajax({
		    method: "POST",
		    url: "/makepurchase/",
		    data: {'id': id},
		    contentType:"application/x-www-form-urlencoded; charset=UTF-8",
  		    dataType:"json",
                    success: function(data, textStatus, jqXHR) {
			if (data['result'] == 'success')
				{
				alert('Товар добавлен в корзину');}
			if (data['result'] == 'redirect')
				{
				window.location.href = "/auth/login";}},
                    error: function( xhr, textStatus ) {
    		        alert( [ xhr.status, textStatus ] )},
		
		    crossDomain: false,
		    headers: {"X-CSRFToken": csrftoken, "HTTP_X_REQUESTED_WITH": "XMLHttpRequest"},

	 	});
	}
	
// Получает параметр из куки.
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Удаляет товар из корзины
function delete_order_product(product_order_id){
		var csrftoken = getCookie('csrftoken');
		 $.ajax({
		    method: "POST",
		    url: "/delete-order-product/",
		    data: {'product_order_id': product_order_id},
		    contentType:"application/x-www-form-urlencoded; charset=UTF-8",
  		    dataType:"json",
                    success: function(data, textStatus, jqXHR) {
			if (data['result'] == 'success')
				{
				window.location.href = "/basket/";}
			if (data['result'] == 'fail')
				{
				alert('Продукт с таким id не числится в бд')}},
                    error: function( xhr, textStatus ) {
    		        alert( [ xhr.status, textStatus ] )},
		
		    crossDomain: false,
		    headers: {"X-CSRFToken": csrftoken, "HTTP_X_REQUESTED_WITH": "XMLHttpRequest"},

	 	});
	}

// Добавляет товар в отложенные. ЕЩЁ НЕРЕАЛИЗОВАННО!
function add_delayed_order_product(product_order_id) {
    var csrftoken = getCookie('csrftoken');
		 $.ajax({
		    method: "POST",
		    url: "/add-delay-order-product/",
		    data: {'product_order_id': product_order_id},
		    contentType:"application/x-www-form-urlencoded; charset=UTF-8",
  		    dataType:"json",
                    success: function(data, textStatus, jqXHR) {
			if (data['result'] == 'success')
				{
				window.location.href = "/basket/";}
			if (data['result'] == 'fail')
				{
				alert('Продукт с таким id не числится в бд')}},
                    error: function( xhr, textStatus ) {
    		        alert( [ xhr.status, textStatus ] )},
		
		    crossDomain: false,
		    headers: {"X-CSRFToken": csrftoken, "HTTP_X_REQUESTED_WITH": "XMLHttpRequest"},

	 	});
	}	

	

// Уменьшение количества товара в заказе на 1.
function delete_one(productSelector) {
	    value = parseInt($(productSelector).val());
	    if (value >= 1) {
	    	value = parseInt($(productSelector).val()) - 1;
	    	$(productSelector).val(value);
	     };
	    $(productSelector).trigger('onchange');	
	}

// Изменение количества товаров в заказе.
function change_order(productSelector) {
            value = $(productSelector).val();
	    if (value == '' || value == '0'){
		$('#dialog').dialog('option', 'buttons', {
			'Отмена': function() {
				set_product_num_to_one(productSelector);
				$('#dialog').dialog('close');},
			'Ок': function(){
				delete_order_product($(productSelector).next().val());
				$('#dialog').dialog('close');}});
		$('#dialog').dialog('open');}
	}

// Устанавливает количество товаров в заказе на 1.
function set_product_num_to_one(productSelector){
		$(productSelector).val(1);	
	}

// Увеличение количества товара в заказе на 1.	
function add_one(productSelector) {
	    value = parseInt($(productSelector).val()) + 1;
	    $(productSelector).val(value);
	    $(productSelector).trigger('onchange');	
	}

