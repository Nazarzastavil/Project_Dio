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
    format: 'dd.mm.yyyy',
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

  $('#confirm_password#deg').on('keyup', function () {
    if ($('#password').val() == $('#confirm_password#deg').val()) {
      $('.helper-text').html('Rigth').css('color', 'green');
    } else 
      $('.helper-text').html('Wrong').css('color', 'red');
  });

  