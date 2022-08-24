const category = document.querySelector('#id_category');
var sub_category = document.querySelector('#id_sub_category')
category.addEventListener('change', (e) => {
    var categoryId = category.value;
    fetch("/products/select_cat/" + categoryId + "/", {

    })
        .then((res) => res.json())
        .then((context) => {
            const data = context.data;
            console.log("data", data)
            // var innerHTML = `<option value="${item.id}">${item.name}</option>`
            var select = "<select>"
            for (let i = 0; i < data.length; i++) {
                console.log(data[i])
                select += "<option>" + data[i].id + "</option>"
                
            }
            select += "</select>"
            document.getElementById("id_sub_category").innerHTML = select
            // data.forEach((item) => {
            //     console.log("itme",item)
            //     sub_category.innerHTML = `<option value="${item.id}">${item.name}</option>`

            // });

        })
})
// $("#id_category").change(function () {


//     var categoryId = $(this).val();
//     fetch("/products/select_cat/"+categoryId+"/",{
//         // url:
//         // success: function (data) {
//         //     console.log(data.subcategory)
//         //     $("#id_sub_category").html(`
//         //     `);
//         // }
//     }),
//     .then()

// });