  $( "#sb").on( "click", function( event){
    //Transcipt
    $.ajax({
      method: 'POST',
      url: $( '#mainform').attr('action'),
      data: $( "#mainform").serialize(),
      success: function( data ){
        if (data != 'error' && data != 'wrong number'){
          var table = '';
          if($( '#mainform').attr('action')=='/ems/transc'){
            table = "<table class='table is-striped is-hoverable is-fullwidth' style='font-size:12px;''>" + data + "</table>";
          }
          else{
            result = JSON.parse(data);
            table += '<table class="table is-striped is-hoverable is-fullwidth" style="font-size:12px;"><thead><tr>\
        <td width="6%">序号</td>\
        <td width="8%">投币</td>\
        <td width="36%" style="text-align: center;">学号</td>\
        <td width="20%" style="text-align: center;">姓名</td>\
        <td width="15%" style="text-align: center;">性别</td>\
        <td width="15%" style="text-align: right;">状态</td>\
       </tr></thead><tbody>';
            var a=0;
            for(var i=0;i<Object.keys(result).length;i++){
              a++;
              table += '<tr>';
              table += '<td style="text-align: left;">' + a.toString() + '</td>';
              table += '<td style="text-align: center;">' + result[i][0].toString() + '</td>';
              table += '<td style="text-align: center;">' + result[i][1].toString() + '</td>';
              table += '<td style="text-align: center;">' + result[i][2].toString() + '</td>';
              table += '<td style="text-align: center;">' + result[i][3].toString() + '</td>';
              table += '<td style="text-align: right;">' + result[i][4].toString() + '</td>';
              table += '</tr>';
            }
            table += '</tbody></table>';
          }
          $( "#prod").append(table);
        }
        else
          $( "#prod").append(data);
      }
    });
  });
  $( "#outinput").on( "click", function( event){
    $.ajax({
    method: "GET",
    url: "/logout",
    data: $( "#loginForm").serialize(),
    success: function( data ) {
      $( "#loginForm")[0].reset();
      $( "#status").removeClass("is-success");
      $( "#status").addClass("is-warning");
      $( "#exit").hide();
      $( "#log").show();
      
    }
  });
  });

  function dologin(){

//$( "#loginForm").attr( "action","/login");
var info = $( "#loginForm").serialize();
$.ajax({
  method: "POST",
  url: "/login",
  data: $( "#loginForm").serialize(),
  success: function( ) {
      window.location.reload(false);
    
    }
});
}

function dologout(){
    $.ajax({
    method: "GET",
    url: "http://jwgl.ouc.edu.cn/DoLogoutServlet",
    data: $( "#loginForm").serialize(),
    success: function( data ) {
      if (data == "ok"){
      $( "#status").removeClass("is-success");
      $( "#status").addClass("is-warning");
      $( "#exit").show();
      $( "#log").hide();
    }
  }
  });
}
$( ".act.menu .tip").on( "click", function (event) {
   $( "#wowf").attr("action",$(this).attr("value"));
   $( ".act.txt").val($(this).html());
});

$( ".xq.menu .tip").on( "click", function (event) {
    $( "#nq").val($(this).attr("value"));
    $( ".txt.xq").val($(this).attr("value"));
    if ($( "#nq").val()=='all')
      $( "#sjxz").val('sjxz1');
    else
      $( "#sjxz").val('sjxz3');
});

$( ".frd").on( "click", function (event) {
    $( ".opts.op").prev().addClass("gp");
    $( ".op.gp").removeClass("gp");
});
$( ".menu.act .tip:not(.frd)").on( "click", function (event) {
    $( ".opts.op").prev().removeClass("gp");
    $( ".op").addClass("gp");
});
$( ".menu.act .tip:not(.ts)").on( "click", function (event) {
    $( ".opts.op").prev().addClass("gp");
});
$( ".menu.sl .tip").on( "click", function ( event) {
   $( "#sel").val($(this).attr("value"));
   $( ".txt.xx").val($(this).html());
});


function setXnxq(){
  $( "#nq").val($( "#xnxq option:selected").val());
  if ($( "#nq").val()=='all')
    $( "#sjxz").val('sjxz1');
  else
    $( "#sjxz").val('sjxz3');
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

$('#wowf').submit(function( event ){
    event.preventDefault();
    var prep = "";
    prep = `<div class="result-can">
        <div class="item-dust ">

              <div class="info">
                Info
              </div>
              <div class="undo">
                Show
              </div>

        </div>
        <div class="item-body">
            <div class="item-controller">
                <div class="info">
                    <div class="search-type">
    `;
    var act = $( "#wowf").attr("action");
    if( act == "/ems/coins"){
        prep += '<i class="fas fa-coins"></i>投币';
    }
    else if( act == "/ems/transc"){
        prep += '<i class="fas fa-scroll"></i>成绩';
    }
    else if( act == "/ems/frd"){
        prep += '<i class="fas fa-user-circle"></i>学生';
    }
    else if( act == "/ems/alstd"){
        prep += '<i class="fas fa-archive"></i>已选';
    }
    prep += '</div><div class="search-keyword">' + $("#stu").val();
    prep += `
                    </div>
                </div>
                <div class="ctrl-button">
                    <span class="navbar-burger burger stay" data-target="navbarMenuHeroA">
                        <span></span>
                        <span></span>
                        <span></span>
                    </span>
                </div>
            </div>

            <div class="wait button is-loading is-fullwidth"></div>
        </div>
    </div>
    `;
    var tom = $(prep);
    $( ".srch-result").prepend(tom);
    $.ajax({
      url: $('#wowf').attr('action'),
      type: 'POST',
      data : $('#wowf').serialize(),
      success: function( data ){
        //console.log(data);
        if( data.substring(0,2) == 'no' ) {
            tom.empty();
            tom.append(`
           <div class="notification is-warning">
             <button class="delete"></button>
             无查询结果，请检查选项或输入信息。<div style="font-size: 8px;position: absolute">若登陆失效，请在右下角或点击<a href="/signin">这里</a>重新登陆。</div>
           </div>`);
            tom.attr("style","font-size:12px;");
        }else if(data.substring(0,3) == 'plz' || data.substring(0,3) == "<!D" || (data.substring(0,4) != "\n<th" && data.substring(0,1) != "[")){
            tom.empty();
            tom.append(`
           <div class="notification is-danger">
              <button class="delete"></button>
                登陆失效，请在右下角或点击<a href="/signin">这里</a>重新登陆。
            </div>`);
            tom.attr("style","font-size:12px;");
            $( "#log").show();
            $( "#exit").hide();
        }
        else {
            if (act == "/ems/coins") {
                var rag = JSON.parse(data);
                var adg = `
            <div class="srch-item course-item">
                <table class="courselist table is-fullwidth">
                    <thead style="display: none;">
                    </thead>
                    <tbody>
            `;
                    for (var pr in rag) {
                        console.log(rag[pr][5]);
                        adg += `<tr><th class="list-index"><div class="ball"><div>` + (parseInt(pr) + 1).toString() + `</div></div></th><td class="selecter"><div class="cname">` + rag[pr][2] + `</div><div class="cid">` + rag[pr][1] + `</div></td><td class=""><input type="checkbox" `;
                        if(rag[pr][5] == true)
                          adg += 'checked';
                        adg += ` disabled></td><td class="status">` + rag[pr][4] + `</td><td class="coin"><span class="tag">` + rag[pr][0] + `</span></td></tr>`;
                    }
                    adg += '</tbody></table></div>';

            }
            else if (act == "/ems/grades") {
                var rag = JSON.parse(data);
                var adg = `
            <div class="srch-item course-item">
                <table class="courselist table is-fullwidth">
                    <thead style="display: none;">
                    </thead>
                    <tbody>
            `;
                    for (var pr in rag) {
                        adg += `<tr><th class="list-index"><div class="ball"><div>` + (parseInt(pr) + 1).toString() + `</div></div></th><td class="selecter"><div class="cname">` + rag[pr][2] + `</div><div class="cid">` + rag[pr][1] + `</div></td><td class="status">` + rag[pr][3] + `</td><td class="coin"><span class="tag">` + rag[pr][0] + `</span></td></tr>`;
                    }
                    adg += '</tbody></table></div>';
                    console.log("grades got!");
            }
            else if (act == "/ems/transc") {
                var adg = `
            <div class="srch-item transcipt-item">
                <table class="table is-striped is-hoverable is-fullwidth" style="font-size: 10px;">
            ` + data + '</table></div>';
            }
            else if (act == "/ems/frd") {
                if (data != "no such person!") {
                    var rag = JSON.parse(data);
                    console.log(rag);
                    var adg = "";
                    for (var pr in rag) {
                        adg += `<div class="srch-item stuinfo-item off-` + (rag.length - pr).toString() + `">
                <div class="stu-info">
                    <div class="stu-avatar">
                        <figure class="image is-96x96">
                            <img src="/static/favicon.ico">
                        </figure>
                    </div>
                    <div class="basicinfo">
                        <p class="name">` + rag[pr][1] + `
</p>
                        <div class="xueji">
                            <div class="tags has-addons">
                              <span class="tag">
` + rag[pr][0] + `
</span>
                              <span class="tag is-primary">学院Unknown</span>
                            </div>
                        </div>
                        <div class="stu-signature">
                            Eastern region of the San Francisco Bay Area, California, US
                        </div>
                    </div>
                </div>

                <a class="button">Contact</a>

            </div>`;
                        //tom.addClass("fixh");
                    }
                }
            }
            else if (act == "/ems/alstd") {
                var rag = JSON.parse(data);
                var adg = `<div class="srch-item slted-item">
            <table class="selectedlist table is-fullwidth">
                    <thead style="display: none;">
                    </thead>
                    <tbody>`;
                var a = [2, 3, 4, 5, 14, 13];
                for (var pr in rag) {
                    adg += `<tr><th class="list-index"><div class="ball"><div>` + rag[pr][0] + `</div></div></th><td class="selection"><div class="cname">` + rag[pr][1].substring(rag[pr][1].indexOf("]") + 1) + `</div><div class="cid">` + rag[pr][6] + `</div></td>`;
                    for (var i in a) { //2, 3, 4, 5, 14, 13
                        adg += '<td>' + rag[pr][a[i]] + '</td>';
                    }
                    adg += `<td class=""><input type="checkbox" disabled></td><td class="coin"><span class="tag">` + rag[pr][8] + `</span></td><td class="ctrl">操作</td></tr>`;
                }
                adg += '</tbody></table></div>';
            }
        }
        tom.find('.wait').remove();
        tom.find('.item-body').append(adg);
      }
    });
});