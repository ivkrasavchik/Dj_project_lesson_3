$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);

    // ajax
    function basketUpdating(product_id, nmb, is_delete){
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;

        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true;
        }

        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                console.log("OK");
                console.log(data.products_total_nmb);

                if (data.products_total_nmb || data.products_total_nmb == 0){
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                      console.log(data.products);
                      $('.basket-item ul').html("");
                      $.each(data.products, function (i, elem) {
                        $('.basket-item ul').append('<li>'+elem.name+', '+elem.nmb+' шт. по '+elem.price_per_item+' Руб. '+
                        '<a class="delete-item" href="" data-product_id="'+elem.id+'">x</a>'+
                        '</li>');
                    })
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
    }

    form.on('submit', function (e) {
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);


        basketUpdating(product_id, nmb, is_delete=false)

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

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true)
    });

    function calculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function () {
            total_order_amount += parseFloat($(this).text());
        });
        $('#total_order_amount').text(total_order_amount)

    }

    $(document).on('change', ".product-in-basket-nmb", function(){
        var current_nmb = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        var total_amount = current_nmb*current_price;
        current_tr.find('.total-product-in-basket-amount').text(total_amount);

        calculatingBasketAmount();
    });
    calculatingBasketAmount();
});
