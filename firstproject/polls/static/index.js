alert('welcome')


$(function (){
    var $orders=$('#orders');
    $.ajax({
        type:'GET',
        url: '/polls/',
        success:function(orders){
            $.each(orders,function(i,order){
            console.log(order.Tags[order])
                });
        }
        });

});