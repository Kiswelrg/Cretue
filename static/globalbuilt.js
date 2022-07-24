
$( document ).ready(function() {
    if ( window.location.href.substr(window.location.href.length - 6) === '?mes=1' ){
      console.log('ready!');
      $( "#status").removeClass("is-warning");
      $( "#status").addClass("is-success");
      $( "#log").hide();
      $( "#exit").show();
    }
});
$( document).on( "click", function ( event) {
	    if(!$(event.target).closest('.tooltip').length) {
            if(!$(event.target).hasClass("burger")) {
                $('.tooltip').prev().removeClass('is-active');
                $('.tooltip').remove();
            }
        }

        if(!$(event.target).closest('.menu.show').length || $(event.target).hasClass('tip')) {
            if(!$(event.target).closest('.panel-button').length ) {
                $('.menu.show').removeClass('show');
            }
        }
    });


    //nav--
    $( "#ac-globalnav").on( "click", function( event){
      var state = $(this).attr("state");
      if (state == '0'){
        $( ".is-fixed-top").addClass("menu-opening");
        $( ".navbar.is-fixed-top").addClass("opened");
        $( this).attr("state","1");
        setTimeout(
          function(){
            $( ".is-fixed-top").removeClass("menu-opening");
          } , 640);
      }
      else
      {
        $( ".navbar.is-fixed-top").removeClass("opened");
        $( ".is-fixed-top").addClass("menu-closing");
        $( this).attr("state","0");
        setTimeout(
          function(){
            $( ".is-fixed-top").removeClass("menu-closing");
          } , 640);
      }
    });

    // = x
$( ".oftwo").on( "click", function( event){
    var scroll = $( "html").hasClass("ac-gn-noscroll");
    if (scroll == true)
    {
        $( "html").removeClass("ac-gn-noscroll");
        $( "html").removeClass("ac-gn-noscroll-long");
    }
    else {
        $( "html").addClass("ac-gn-noscroll");
        $( "html").addClass("ac-gn-noscroll-long");
    }

    $(this).toggleClass("is-active");

    });


    //new ---------------------------------------------------------------------------
    $( "#srchid" ).on( "input" , function( event ){
        if ($( "#srchid").val() != "" ){
            $( this).parent().prev().removeClass("head-off");
        }
        else{
            $( this).parent().prev().addClass("head-off");
        }
        $( "#stu").val($( this).val());
    });

    $(".srch-result").on("click",".navbar-burger", function (event) {
        if ($(this).hasClass("is-active")) {
            $(".tooltip").remove();
            $(this).removeClass("is-active");
        }
        else {
            $(".burger").removeClass("is-active");
            $(".tooltip").remove();
            $( this).addClass("is-active");
            var position = $(this).offset();
            if ((position.left + $(this).width() + 70.56) > $("body").width()) {

                var tooltip = '\
                                       <div class="tooltip fade cc-tooltip-left show" role="tooltip" id="" style="position: relative; transform: translate3d(' + (0 - $(this).width()).toString() + 'px, ' + (0 - $(this).height()).toString() + 'px, 0px); top: 0px; left: 0px; will-change: transform;" x-placement="right">\
                           <div class="arrow" style="top: 18.9px;"></div>\
                           <div class="tooltip-inner">\
                               <div class="tip tip-h">Hide</div>\
                               <div class="tip tip-d">Delete</div>\
                           </div>\
                       </div>\
                   '
            }
            else {
                var tooltip = '\
                                       <div class="tooltip fade cc-tooltip-right show" role="tooltip" id="" style="position: relative; transform: translate3d(' + 70.56 + 'px, ' + (0 - $(this).height()).toString() + 'px, 0px); top: 0px; left: 0px; will-change: transform;" x-placement="right">\
                           <div class="arrow" style="top: 18.9px;"></div>\
                           <div class="tooltip-inner">\
                               <div class="tip tip-h">Hide</div>\
                               <div class="tip tip-d">Delete</div>\
                           </div>\
                       </div>\
                   '
            }
            $(this).parent().append(tooltip);
        }
    });

    $(".srch-result").on("click",".tip-h", function (event) {
                if($(this).closest(".fixh").length){
                    $(this).closest(".fixh").removeClass("fixh");
                }
                $(this).parent().parent().parent().parent().parent().prev().addClass("show");
                //$(this).parent().parent().parent().parent().parent().slideUp(400);
                $(this).parent().parent().parent().parent().parent().addClass("close");
                //reletive
                $(this).parent().parent().parent().parent().parent().prev().css("position", "relative");
                //close toolbar
                $(this).parent().parent().prev().removeClass("is-active");
                $(this).parent().parent().remove();
            });
            $(".srch-result").on("click",".tip-d", function (event) {
                //close toolbar
                $(this).parent().parent().prev().removeClass("is-active");
                $(this).parent().parent().hide();
                $(this).parent().parent().parent().parent().parent().parent().slideUp(400, function () {
                    $(this).parent().parent().parent().parent().parent().parent().remove();
                });
            });
            $( ".srch-result").on( "click", ".undo", function( event ) {
                $(this).parent().removeClass("show");
                $(this).parent().next().removeClass("close");
                $(this).parent().css("position","absolute");
            });
            $( ".srch-result").on( "click", ".tip", function ( event ) {
                 $(".menu.show").removeClass("show");
            });


	$( ".opts .panel-button").on( "click", function ( event) {
        if( !$(this).parent().next().find(".menu").hasClass("show"))
            $(".menu").removeClass("show");
        $(this).parent().next().find(".menu").toggleClass("show");
    });
	//old -----------------------------------------------------------------


$( ".srch-result").on( "click", ".delete" , function ( event ) {
   $(this).parent().parent().hide('slow', function(){ $(this).remove(); });
});

$( ".panel-tabs a" ).on( "click", function( event ) {
    var currentAct = $( ".panel-tabs .is-active" );
    currentAct.removeClass("is-active");
    $(this).addClass("is-active");
});
$( "ul li" ).on( "click", function( event ){
    var currentAct = $( "ul .is-active");currentAct.removeClass("is-active");
    $(this).addClass("is-active");
});
$( ".panel a").on( "click", function( event ) {
    var currentAct = $( ".panel .is-active" );
    currentAct.removeClass("is-active");
    $(this).addClass("is-active");
});

//l,t
    $( "#l").on( "click",function(event){
      $( '#mainform').attr("action","/coins");
    });
    $( "#t").on( "click",function(event){
      $( '#mainform').attr("action","/transc");
    });
    $( "#stuinput").on( "input",function(event){
      $( "#stu").val($( "#stuinput").val());
    });


  $( "#mode").on( "click", function(event){
  var mode = $( "#mode");
  var word = $( "#pw");
  var ssid = $( "#ss");
  if(mode.html() =="User/P"){
    mode.html("Cookie");
    word.hide();
    ssid.show();

  }
  else{
    mode.html("User/P");
    ssid.hide();
    word.show();
  }
  var set = document.getElementById("setmode");

var index = parseInt(set.value)
index = 1-index;
$( "#loginForm")[0].reset();
set.setAttribute("value",index.toString());
});

  $( "#status").on( "click", function( event){
      $( ".column.is-three-fifths").empty();
  });
  var lastScrollTop = 0;
  $(window).scroll(function(event){
      var st = $(this).scrollTop();
      if (st > lastScrollTop)
          $( '.navbar.is-fixed-bottom').css('box-shadow','rgba(0, 0, 0, 0.13) 0px -.1px 15px 0px');
      else
          $( '.navbar.is-fixed-bottom').css('box-shadow','rgba(0, 0, 0, 0.13) 0px -.1px 15px 2px');
      lastScrollTop = st;
  });