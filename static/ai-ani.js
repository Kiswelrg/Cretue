function r(str,index){
    if(index<0)
        index=0-index;
    if(str[0]=="-")
        str="+=" + (b*index) + "px";
    else
        str="-=" + (b*index) + "px";
    return str;
}

function scrollto(j,index,bool){
    var w_width = $(window).width();
    var change = (j-b_size+0.5)*b + w_width/2 + parseInt($(".block").css("left").substring(0,$(".block").css("left").indexOf("p")));
    if(change>0)
        change += w_width/8;
    else if(change <0)
        change -= w_width/8;
    if(change < 0 || change > w_width){
        if($(".block").css("left") != "auto"){
            var origin = parseFloat($(".block").css("left").substring(0,$(".block").css("left").indexOf('p')));
            origin = (-origin-change%w_width);
            var str;
            if(origin < 0)
                str = "-=" + (0-origin) + "px";
            else
                str = "+=" + (origin) + "px";
            $(".block").animate({
                left: str,
            }, { duration: index, queue: bool } );
        }else
            $(".block").animate({
                left: (0-change%w_width) + "px",
            }, { duration: index, queue: bool } );            
    }
}

function findnp(id){
    var i,ss,sum;
    if(opt == 0){
        ss = '.np-';
        sum = n_size*n_size;
        
    }else{
        ss = '.bl-';
        sum = b_size*2+1;
    }
    for(i=1;i<sum+1;i++){
        if($(ss+i).html() == id) return i;
    }
}

function target(id){
    var zero;
    if(opt == 0){
        zero = board.indexOf('0');
        if(id == '0' && (zero-n_size)>-1 ) {
            board[zero] = [board[zero-n_size], board[zero-n_size] = board[zero]][0];
        }
        if(id == '2' && zero%n_size != 0 ) {
            board[zero] = [board[zero-1], board[zero-1] = board[zero]][0];
        }
        if(id == '3' && (zero+1)%n_size!=0 ) {
            board[zero] = [board[zero+1], board[zero+1] = board[zero]][0];
        }
        if(id == '1' && (zero+n_size)<n_size*n_size ) {
            board[zero] = [board[zero+n_size], board[zero+n_size] = board[zero]][0];
        }
        return zero;
    }else{
        zero = blocks.indexOf(0);
        scrollto(zero+id,250,false);
        blocks[zero] = [blocks[zero+id], blocks[zero+id] = blocks[zero]][0];
        return zero;
    }
}

function move(id){
    var ss = '';
    if(opt == 0){
        ss = '.np-';
        drt = ss + findnp(board[target(id)]);
        console.log(drt);
        // 上左右下
        if(id == '1')
          $(drt).animate({ 
            top: a[0],
        }, 500 );
        else if(id == '3')
          $(drt).animate({ 
            left: a[0],
        }, 500 );
        else if(id == '2')
          $(drt).animate({ 
            left: a[1],
        }, 500 );
        else
          $(drt).animate({ 
            top: a[1],
        }, 500 );
    }else{
        var mv;
        if(id>0)
            mv = '+' + b + "px";
        else
            mv = '-' + b + "px";
        ss = ".bl-";
        drt = ss + blocks[target(id)].toString();
        $(drt).animate({ 
            top: mv,
        }, c );
        scrollto(blocks.indexOf(0)-id,c*1.6,false);
        $(drt).animate({ 
            left: r(mv,id),
        }, c );
        $(drt).animate({
            top: "0px",
        }, c );
    }
}

$( "h4.headline div").click(function(event) {
    $( "h4.headline div").toggleClass("is-active");
    reset();
    opt ^= 1;
    $(".block").toggle();
    $(".puzzle").toggle();
});


function doSetTimeout(i) {
    if(opt==0)
        setTimeout(function() { move(plain[i]);
            }, (i-n_size*n_size*2-2-(parseInt(n_size/4)*6))*160 );
    else if(opt==1)
        setTimeout(function() {
            if(plain.indexOf("-") == -1){
                move(b_actions[i]-blocks.indexOf(0));
            }
            else{
                move(b_actions[i]);
            }
            }, c*3*i);

}

$( ".commit").click(function(event) {
    reset();
    var i;
    var str = $(".unit-copy-wrapper .control .input").val();
    var length;
    length = (str.length-1)/2*2+1;
    if(str[1] == " " || str[2] == " "){
        plain = str;
        base64code = btoa(str);            
    }else{
        base64code = str;
        plain = atob(str);
    }
    if(opt == 0) {
        n_size = parseInt(plain[0]);
        $(".puzzle").empty();
        var j;
        for(i=0;i<n_size;i++){
            $(".puzzle").append('<div class="columns is-mobile"></div>');
            for(j=0;j<n_size;j++){
                //
                $(".puzzle .columns:nth-child(" + (i+1) + ")").append('<div class="column button is-hovered np-' + (i*n_size+j+1) + '" index="' + (i*4+j+1) + '">' + (i*4+j+1) +  '</div>');
            }
        }
        for(i=0;i<n_size*n_size*2+2+(n_size/4*6);i++){
            if(plain[i] == " ")
              blank_position[blank_position.indexOf(-1)] = parseInt(i);
        }
        for(i=1; i<n_size*n_size+1; i++){
            var s = plain.substring( blank_position[i-1]+1,blank_position[i]);
            $(".np-"+ i).html(s);
            board[i-1]=s;
            if(s == "0") {$(".np-"+ i).addClass('is-blank');$(".np-"+ i).html('');}
        }
        for(i=n_size*n_size*2+2+(parseInt(n_size/4)*6); i<length; i+=2){
            doSetTimeout(i);
        }
    }
    if(opt == 1){
        plain+=" ";
        var blank1=0;
        var one="";
        do{
            one += plain[blank1];
            blank1++;
        }while(plain[blank1]!=" ")
        b_size = parseInt(one);
        $(".block .columns").empty();
        for(i=0;i<b_size;i++){
            var k = '<div class="column button is-hovered blk bl-' + (i+1) +   '" index="' + (i+1) + '">B</div>';
            $(".block .columns").append(k);
        }
        for(i=b_size;i<b_size*2;i++){
            var k = '<div class="column button is-hovered wht bl-' + (i+1) +   '" index="' + (i+1) + '">W</div>';
            $(".block .columns").append(k);
        }
        $(".block .columns").append('<div class="column button is-hovered is-blk bl-' + (2*b_size+1) +   '" index="' + (2*b_size+1) + '"></div>');
        blocks = new Array(b_size*2+1);
        b_actions = new Array(  parseInt(plain.length/2));
        for(i=0;i<b_actions.length;i++) b_actions[i]=null;
        for(i=0;i<b_size*2;i++)   blocks[i] = i+1;
        blocks[b_size*2] = 0;
        var sum=0;
        var index = blank1+1;
        var act="";
        while(index<plain.length){
            if(plain[index] != " ")   act+=plain[index];
            else{
                b_actions[sum] = parseInt(act);
                sum++;
                act="";
            }
            index++;
        }
        for(i=0;i<sum;i++){
            doSetTimeout(i);
        }
    }

});

$( ".copy").click(function(event) {
    var el = document.createElement('textarea');
    var str = $(".unit-copy-wrapper .control .input").val();
    if(str[1] != " " && str[2] != " "){
        base64code = str;
        plain = atob(str);
    }else {
        plain = str;
        base64code = btoa(str);
    }
    el.value = base64code;
    el.setAttribute('readonly', '');
    el.style = {position: 'absolute', left: '-9999px'};
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
});

$("h4 div:nth-child(2)").click();