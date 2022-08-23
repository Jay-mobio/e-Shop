function RemoveImg(id) {
    $.ajax({
        type: 'DELETE',
        url: '/remove_image/'+id+'/',
        data: {product:id},
        success: function(req){
            RmvImg.innerText = "Removed";

    }
})
}
