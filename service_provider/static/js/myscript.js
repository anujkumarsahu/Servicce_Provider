$('#slider1, #slider2, #slider3, #slider4, #slider5, #slider6').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: false,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: false,
        },
        1000: {
            items: 4,
            nav: true,
            loop: true,
            autoplay: false,
        }
    }
})


$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:'/plus_cart',
        data:{
            prod_id:id
        },
        success: function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("total_amount").innerText=data.total_amount

        }
    })
});
$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:'/minus_cart',
        data:{
            prod_id:id
        },
        success: function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("total_amount").innerText=data.total_amount

        }
    })
});

$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type:"GET",
        url:'/remove_cart',
        data:{
            prod_id:id
        },
        success: function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("total_amount").innerText=data.total_amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            // alert("Succesfully ! your cart  Remove.")

        }
    })
});