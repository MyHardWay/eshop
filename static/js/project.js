


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

function make_search(inputForm, inputField) {
			document.getElementById("searchForm").action = '/search?param=';
			var formAction = $(inputForm).attr('action');
			var paramValue = $(inputForm).find('input')[0].value;
			
			alert(paramValue);
			$(inputForm).attr('action', formAction +  paramValue);
		}	


function check_for_prizes_valid(minPrize, maxPrize) {
			var minPrizeVal = parseInt($(minPrize).val());
			var maxPrizeVal = parseInt($(maxPrize).val());
			if(minPrizeVal > maxPrizeVal){
				$(minPrize).val(maxPrizeVal);}
			}
			

function change_visibility(element_id, element_img, hide_img, show_img) {			
			if ($(element_id).is(':visible')){
				$(element_id).hide(300);
				$(element_img).attr('src', hide_img);		
			}
			else {
				$(element_id).show(300);
				$(element_img).attr('src', show_img);								
			};}
		
// Ввод только целых чисел.			
function check_key_is_number(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}			

// Запрещаем вставлять из буффера строку содержащую не только цифры.
function validate_paste_numbers(e){
	 var pastedText = undefined;
    if (window.clipboardData && window.clipboardData.getData) { // IE
        pastedText = window.clipboardData.getData('Text');
    } else if (e.clipboardData && e.clipboardData.getData) {
        pastedText = e.clipboardData.getData('text/plain');
    }
    if (!$.isNumeric(pastedText)){
      e.preventDefault();
    }

}				
				
			

