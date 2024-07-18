$(document).ready(function(){
	$('.order').on('click', function(){
        console.log("hii")
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