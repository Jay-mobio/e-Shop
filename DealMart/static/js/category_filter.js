function finalurl4() {
    console.log("hii")
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('categories', document.getElementById("categroy").value);
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url
  }