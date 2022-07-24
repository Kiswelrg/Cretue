$( ".yzm" ).prev().focus(function() {
  $('.yzm img').attr('src','');$('.yzm img').attr('src','/ems/code');
});

    $( ".idim").on( "input",function(event){
      console.log('!');
      if ($( ".idim").val().toString().length == 11 && $.isNumeric($( ".idim").val()))
      {
        $( ".idim").addClass("is-success");
        $( ".us").removeClass("hide");
      }
      else
      {
        $( ".idim").removeClass("is-success");
        $( ".us").addClass("hide");
      }
    });

    $( document ).ready(function() {
    if ( window.location.href.substr(window.location.href.length - 1) == '1'){
      console.log('?');
      $( "#status").removeClass("is-warning");
      $( "#status").addClass("is-success");
      $( "#log").hide();
      $( "#exit").show();
    }
});

    $( "#ckbt").on( "click", function(event){
      $( this).addClass("hide");
      $( "#pwbt").removeClass("hide");
      $( "#setmode").attr("value","1");
      $( "#ckbt").prev().html("Cookie");
      $( "#pinput").attr("name","ssid");
      $( "#uinput").prop("disabled",true);
      $( "#uinput").val("");
    });
    $( "#pwbt").on( "click", function(event){
      $( this).addClass("hide");
      $( "#ckbt").removeClass("hide");
      $( "#setmode").attr("value","0");
      $( "#ckbt").prev().html("Password");
      $( "#pinput").attr("name","password");
      $( "#uinput").prop("disabled",false);
    });