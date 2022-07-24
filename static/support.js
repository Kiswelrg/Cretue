function dologin(){

//$( "#loginForm").attr( "action","/login");
var info = $( "#loginForm").serialize();
console.log(info);
$.ajax({
  method: "POST",
  url: "/login",
  data: $( "#loginForm").serialize(),
  success: function( result ) {

    if(result == "ok"){

      $( "#status").removeClass("is-warning");
      $( "#status").addClass("is-success");
      $( "#log").hide();
      $( "#exit").show();
    }
  }
});
}
function dologout(){
  $.ajax({
    method: "GET",
    url: "http://jwgl.ouc.edu.cn/DoLogoutServlet",
    data: {
      'Cookie': 'JSESSIONID='+ $( "#ssinput").innerHTML,
    }
    success: function( result ) {
      $( "#status").removeClass("is-success");
      $( "#status").addClass("is-warning");
      $( "#exit").show();
      $( "#log").hide();
    }
  });
}


function setXnxq(obj){
  $( "#nq").val($( "#xnxq option:selected").val());
}
function showLogin(){
  document.getElementsByClassName("field")[0].classList.add("is-active");
}
function modeChange(){
  var mode = document.getElementById("mode");
  var user = document.getElementById("us");
  var word = document.getElementById("pw");
  var ssid = document.getElementById("ss");
  if(mode.innerHTML=="User/P"){
    mode.innerHTML = "Cookie";
    word.setAttribute("hidden","");
    ssid.removeAttribute("hidden");

  }
  else{
    mode.innerHTML = "User/P";
    ssid.setAttribute("hidden","");
    word.removeAttribute("hidden");
//document.getElementById("pwinput").setAttribute("placeholder","username");
}
var set = document.getElementById("setmode");

var index = parseInt(set.value)
index = 1-index;
set.setAttribute("value",index.toString());

}
function logchange(obj){
  var tr1,tr2,tr3;
  tr1 = document.getElementById("log");
  tr2 = document.getElementById("exit");
  if(obj.value=="Lout"){
    tr3 =tr1;
    tr1 =tr2;
    tr2 =tr3;
  }
  tr1.setAttribute("hidden","");
  tr2.removeAttribute("hidden");

  tr2.removeAttribute("disabled");
  tr1.setAttribute("disabled","");
}