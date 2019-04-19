$(".hover").mouseleave(
    function () {
        
      $(this).removeClass("hover");
    }
  );



$(".snip1273").click(function() {
    
    $(".flex.flex-2").hide();
    $(".flex.flex-2." + $(this).attr("class").split(" ")[1]).show();
 });

 $(document).ready(function(){
    $(".flex.flex-2").hide();
    $(".flex.flex-2.deg").show()
  });