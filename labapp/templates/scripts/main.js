$(document).ready(function() {
    var scale = 1.3;
    $('.object').hover(function() {  //наведение курсора на элемент класса "object"
       width_scale = $(this).width() * scale;  //рассчитывается новая высота и ширина
       height_scale = $(this).height() * scale;
       shift_left = ($(this).width() - width_scale)/2; //рассчитывается сдвиг изображения, чтобы оно оставалось по центру
       shift_top = ($(this).height() - height_scale)/2;
   
       $(this).find('img').stop(false,true).animate({'width':width_scale, 
       'height':height_scale, 'top':shift_top, 'left':shift_left}, {duration:333}); //изменение значений
    },
    function() { // возвращение к исходному
       $(this).find('img').stop(false,true).animate({'width':$(this).width(),
       'height':$(this).height(), 'top':'0', 'left':'0'}, {duration:333});
    });
});

$(document).ready(function() {
    let faqQuestionContainers = document.querySelectorAll(`[unique-script-id="w-w-dm-id"] .faq-question-container`); //возвращаем коллекцию всех элементов на странице, удовлетворяющих селектору  `[unique-script-id="w-w-dm-id"] .faq-question-container`
    faqQuestionContainers.forEach(function(faqQuestionContainer) { //перебор каждого элемента из коллекции 
      faqQuestionContainer.onclick = function() { //устанавливаем для элемента обработчик события клика
        this.parentElement.classList.toggle("active"); // при каждом клике на элемент будет добавляться или удаляться класс "active"
      };
    });
})