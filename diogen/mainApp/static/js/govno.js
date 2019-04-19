$(".hover").mouseleave(
    function () {
        
      $(this).removeClass("hover");
    }
  );

$(".snip1273").click(function() {
    var myClass = $(this).attr("class").split(" ");
    $(".row.textbox").hide();
    $(".row." + myClass[1]).show();
 });