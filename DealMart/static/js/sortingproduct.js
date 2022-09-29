function finalurl() {
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('ordering', document.getElementById("sort").value);
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url
  }