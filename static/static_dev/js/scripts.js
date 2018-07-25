$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        // ajax
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;

        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_nmb);
                if (data.products_total_nmb){
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                }
                // $('#likes_list').html();
                // $.each(data, function (key, value) {
                //    $('#likes_list').append('<p>'+value.username+'</p>');
                // });
                // $('#modal_messge_likes').modal('show');
                },
            error: function () {
                console.log('error')
                }
        });
        // end ajax



        $('.basket-item ul').append('<li>'+product_name+', '+nmb+' шт. по '+product_price+' Руб. '+
            '<a class="delete-item" href="">x</a>'+'</li>');
    });

    function shovingBasket(){
        $('.basket-item').removeClass('hidden');
        // $('.basket-item').toggleClass('hidden');
    }

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        shovingBasket()
    });

    $('.basket-container').mouseover(function () {
        shovingBasket()
    });

    $('.basket-container').mouseout(function () {
        $('.basket-item').addClass('hidden');
    })

    $(document).on('click', '.delete-item', function () {
        $(this).closest('li').remove();
    })
});
