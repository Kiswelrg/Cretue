$( "#ar").on( "click", function( event){
	console.log($( '#addrecord').attr('action'));
	$.ajax({
      method: 'POST',
      url: $( '#addrecord').attr('action'),
      data: $( "#addrecord").serialize(),
      success: function( data ){
      	console.log(data);
      }
  });
});

$( "#sgl").on( "click", function( event){
	$( '#ouput').html('');
	console.log($( '#ssingle').attr('action'));
	$.ajax({
      method: 'POST',
      url: $( '#ssingle').attr('action'),
      data: $( "#ssingle").serialize(),
      success: function( data ){
      	$( '#ouput').append('<table>' + data + '</table>');
      	
      }
  });
});

$( "#lic").on( "click", function( event){
	$( '#ouput').html('');
	console.log($( '#listC').attr('action'));
	$.ajax({
      method: 'POST',
      url: $( '#listC').attr('action'),
      data: $( "#listC").serialize(),
      success: function( data ){
      	$( '#ouput').append('<table>' + data + '</table>');

      }
  });
});