function multiplyBy(id, action){
  var price = parseInt(document.getElementById(`price${id}`).innerHTML);
  var qty = parseInt(document.getElementById(`quantity${id}`).value)
  if (action === "subtract") {
    qty = qty - 1
  }
  else {
    qty = qty + 1
  }
  console.log(qty*price)
  document.getElementById(`quantity${id}`).setAttribute("value", qty)
  
  var total = qty*price
    document.getElementById(`result${id}`).innerText =total; 
  }