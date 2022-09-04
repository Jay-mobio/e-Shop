const category = document.querySelector('#id_category');
var sub_category = document.querySelector('#id_sub_category')
category.addEventListener('change', (e) => {
    var categoryId = category.value;
    fetch("/products/select_cat/" + categoryId + "/", {

    })
        .then((res) => res.json())
        .then((context) => {
            const data = context.data;

            var select = `<select value='${sub_category}'>`
            for (let i = 0; i < data.length; i++) {
                select += `<option value='${data[i].id}'>` + data[i].name + `</option>`
                
            }
            select += "</select>"
            document.getElementById("id_sub_category").innerHTML = select


        })
})
