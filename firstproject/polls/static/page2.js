$(function (){
$.ajax({
        type:'GET',
        url: '/details/',
        success:function(polls){
            var table_body = '<table border="5">';
            table_body+='<tr>';
                    table_body +='<th>';
                    table_body +='SI.NO';
                    table_body +='</th>';
                    table_body +='<th>';
                    table_body +='OPTION';
                    table_body +='</th>';
                    table_body +='<th>';
                    table_body +=' VOTES';
                    table_body +='</th>';

                    table_body+='</tr>';
                    var j=1

            $.grep(polls, function( n, i ) {
          //filter by question
                     var tag='<p>';
                     tag +='Tags:';
                      for(var x in n.Tags ){

                    if(x==((n.Tags).length)-1)
                    {
                    tag +=''+n.Tags[x];
                    }
                    else{
                    tag +=''+n.Tags[x]+',';
                    }
                    tag +='</p>'
                    }
                    $( "#tags" ).html(tag);
                    $("#one").html(n.Question)
                    for(var key in n.OptionVote){
                    j=j+1;

                    table_body+='<tr>';



                    table_body +='<td>';
                    table_body +=''+j;
                    table_body +='</td>';

                    table_body +='<td>';
                    table_body +=''+key;
                    table_body +='</td>';

                    table_body +='<td>';
                    table_body +=''+n.OptionVote[key];
                    table_body +='</td>';

              table_body+='</tr>';

                    }

});


table_body+='</table>';
                 $('#tableDiv').html(table_body);



        }
        });
      });