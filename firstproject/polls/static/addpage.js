alert("page 4")
$(function (){
console.log("documentisready")
var flag=0;
var c="option "
var x=0;
var max=5;
var ar=[];



$("#addRow").click(function (e) {
            e.preventDefault();


            flag=1;
            var html = '';
            if (x < max){
            if(x==0){
            html += '<input type="option" placeholder="option 3" id="choice3" style="width: 500px;">';
            html += '<br>';
            html += '<br>';
            $('#newRow').append(html);
            }
            if(x==1){
            html += '<input type="option" placeholder="option 4" id="choice4" style="width: 500px;">';
            html += '<br>';
            html += '<br>';
            $('#newRow').append(html);
            }
            if(x==2){
            html += '<input type="option" placeholder="option 5" id="choice5" style="width: 500px;">';
            html += '<br>';
            html += '<br>';
            $('#newRow').append(html);
            }
            if(x==3){
            html += '<input type="option" placeholder="option 6" id="choice6" style="width: 500px;">';
            html += '<br>';
            html += '<br>';
            $('#newRow').append(html);
            }
            if(x==4){
            html += '<input type="option" placeholder="option 7" id="choice7" style="width: 500px;">';
            html += '<br>';
            html += '<br>';
            $('#newRow').append(html);
            }
            x++;
            }

        });


$('#submit').on('click',function(){

    var question=$('#question').val();
    var choice1=$('#choice1').val();
    var choice2=$('#choice2').val();
    var choice3=$('#choice3').val();
    var choice4=$('#choice4').val();
    var choice5=$('#choice5').val();
    var choice6=$('#choice6').val();
    var choice7=$('#choice7').val();
    var choice8=$('#choice8').val();
    var tg=$('#tag').val();
    var tag=tg.split(',')
     console.log(flag);

    var polldetails={
    "Question":question,
    "OptionVote":{
       [choice1]:"0",
       [choice2]:"0",[choice3]:"0",[choice4]:"0",[choice5]:"0",[choice6]:"0",[choice7]:"0" },
       "Tags": tag

    };
    delete polldetails["OptionVote"]["undefined"];
    console.log(polldetails)
    $.ajax({
    type:'POST',
    url:'/createpost/',
    contentType: 'application/json; charset=UTF-8',
    data:JSON.stringify(polldetails),
    dataType: 'json',

    success:function(){
        alert('saved ');
        },
    error:function(){
        alert('error in saving');}

    });
});
});
