function finalurl2() {
    console.log("hiii")
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('search', document.getElementById("search").value);
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url  
  }