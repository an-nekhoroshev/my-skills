;(function($, undefined) {

    // Всплывающее уведомление на сайте
    setTimeout(function() {
        $('.alert').fadeOut('fast');
    }, 2000);


    // Список дел
    // Деактивация кнопки, если нет задач
    function getTasks() {
        let tasks = $(".tasks").children();
        if(tasks.length == 0)
            $(".tasks-btn").prop("disabled", true);
        else
            $(".tasks-btn").prop("disabled", false);
        return tasks;
    }
    getTasks();

    function doneTasks() {
        let done = $(':checkbox:checked').length;
        return done;
    }

    function sendTask() {
        let task = $('.task').val();
        if(task != "") {

            // Добавить строку с задачей
            $("<p class='" + (getTasks().length + 1) + " task-p'/><input class='form-check-input' type='checkbox' " +
                "id='flexCheckDefault" + (getTasks().length + 1) + "'/><label class='form-check-label' " +
                "for='flexCheckDefault" + (getTasks().length + 1) + "'/>Задача #" + (getTasks().length + 1) + ": " +
                task + "</label/></p/>").appendTo(".tasks");

            // Показать сообщение "Задача добавлена"
            $(".task-add-info").slideDown("fast");
            setTimeout(function() { $(".task-add-info").slideUp('fast') }, 2000);

            // Отобразить количество задач на кнопке
            $("input").val("");
            document.getElementById("tasks").innerHTML = (getTasks().length - doneTasks()) + " из " + getTasks().length;

            // Меняем стиль задачи, если она отмечена выполненной
            $('input:checkbox').click(function() {
                if ($(this).is(':checked')) {
                    document.getElementById("tasks").innerHTML = (getTasks().length - doneTasks()) + " из " + getTasks().length;
                    $(this).parent().css({
                        "text-decoration": "line-through",
                        "font-style": "italic",
                        "color": "#555",
                    });
                } else {
                    document.getElementById("tasks").innerHTML = (getTasks().length - doneTasks()) + " из " + getTasks().length;
                    $(this).parent().css({
                        "text-decoration": "none",
                        "font-style": "normal",
                        "color": "black",
                    });
                }
            });
            doneTasks();
        }
    }

    $(".show-task-add-info").on("click", function() { sendTask() });

    $(".form-control").keypress(function(event) {
        if (event.which == 13) {
            event.preventDefault();
            sendTask();
        }
    });

    $(".tasks-btn").on("click", function() { $(".tasks").slideToggle("fast") });

})(jQuery);
