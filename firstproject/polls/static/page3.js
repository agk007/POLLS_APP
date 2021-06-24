$(function (){
$.ajax({
        type:'GET',
        url: '/pollvotes/',
        success:function(polls){


            $.grep(polls, function( n, i ) {
          //filter by question
      console.log(n.Question);
      $("#quest").html(n.Question)
        for(var x in n.OptionVote ){
        var newTextBoxDiv = $(document.createElement('div'))
         .attr("id", 'TextBoxDiv');
        console.log(x)
    newTextBoxDiv.after().html(
          '<input type="radio"  id="textbox" name="option" value="'+x+'">'+'<label>'+ x + '</label>');

    newTextBoxDiv.appendTo("#TextBoxesGroup");

                    }

});


}



        })


$("#submit").click(function() {
        selcted_choice=[];
        $.each($("input[name='option']:checked"), function() {
        selcted_choice.push($(this).val());
        });
        console.log(selcted_choice);

        $.ajax({
        type:'PUT',
        url: '/upvotes/',
         contentType: 'application/json; charset=UTF-8',
    data:JSON.stringify(selcted_choice),
        success:function(polls){
        console.log("hel")
        }


    });
      });
            });