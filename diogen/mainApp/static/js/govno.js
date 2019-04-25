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
    $(".flex.flex-2.deg").show();
    $('.datepicker').datepicker({
    format: 'yyyy-mm-dd',
    autoClose: true,
    i18n: {months: ['Январь','Февраль','Март','Апрель','Май','Июнь', 
    'Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
    monthsShort: ['Янв','Фев','Мар','Апр','Май','Июн', 
    'Июл','Авг','Сен','Окт','Ноя','Дек'],
    weekdays: ['Воскресенье','Понедельник','Вторник','Среда','Четверг','Пятница','Суббота'],
    weekdaysShort: ['Вск','Пнд','Втр','Срд','Чтв','Птн','Сбт'],
    weekdaysAbbrev: [ 'В', 'П', 'В', 'С', 'Ч', 'П', 'С' ],},
  });
  });

  $('#confirm_password, #password').on('keyup', function () {
    if ($('.' + $(this).attr("class").split(" ")[1] +'#password').val() == 
        $( '.' + $(this).attr("class").split(" ")[1] +'#confirm_password').val()) {
      $('.helper-text.' + $(this).attr("class").split(" ")[1]).html('Rigth').css('color', 'green');
    } else 
      $('.helper-text.' + $(this).attr("class").split(" ")[1]).html('Wrong').css('color', 'red');
  });

  