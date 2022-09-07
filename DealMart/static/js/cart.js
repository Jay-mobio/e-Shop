$(document).ready(function(){
	$('.addtocart').on('click', function(){
		product_id = $(this).attr('data-id')
		data = {
			product_id: product_id
		}

		$.ajax({
			// type:'POST',
			url: "/customer/add_to_cart/" + product_id+'/',
			data: data,
			success: function(response){
				alert("Product has been added successfully")
			}

		})
	})
});

// var updateBtns = document.getElementsByClassName('update-cart')

// for (i = 0; i < updateBtns.length; i++) {
// 	updateBtns[i].addEventListener('click', function(){
// 		var productId = this.dataset.product
// 		var action = this.dataset.action
// 		console.log('productId:', productId, 'Action:', action)
// 		console.log('USER:', user)

//         updateUserOrder(productId, action)
		
// 	})
// }

// $('.addtocart').click(function(e){

	
// 	// var subcat = $(this).closest('.product_data').find('.subcat_id').val();
// 	var productID = $(this).closest('.product_data').find('.product_id')
// 	var token = $('input[name=carfmiddlewaretoken]').val();
// 	$.ajax({
// 		method:"POST",
// 		url:"/add_to_cart",
// 		data:{
// 			'productID':productID,
// 			csrfmiddlewaretoken:token
// 		},
// 		success:function(response)	{
// 			alertify.success(response.status)
// 		}
// 	})
// })