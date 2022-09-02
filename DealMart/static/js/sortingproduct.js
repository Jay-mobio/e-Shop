// function sort()
// {
//     console.log('hii')
//     var sortId = $('#sort').val()
//     $.ajax({
//     type: 'GET',
//     url: 'sort/ ',
//     datatype:'json',
//     data: {'sortId':sortId}
//     }).done(function(data){
//         $html(data.products);
//     });
// }

function finalurl() {
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('ordering', document.getElementById("sort").value);
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url
  }