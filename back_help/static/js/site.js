
/*add usuarios*/

 	$(document).ready(function(){
		$(".aba").click(function(){
			$(".aba").removeClass("selected");
  			$(this).addClass("selected");
 			var indice = $(this).parent().index();
     			indice++;
     			$("#content div").hide();
     			$("#content div:nth-child("+indice+")").show();
    		});

     		
     	});

 
  
  /*add usuarios*/
  /*atendimento*/
  function refresh(){
    var div = "{% url 'chat' values.id %}"
    $.ajax({
      url: div,
      success: function(data) {
      $('#text').html(data)
      
    }
  });
  }
  
  $(document).ready(function($) {
    refresh();
    setInterval("refresh()", 3000);
  })
  /*atendimento*/
      


