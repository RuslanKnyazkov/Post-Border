const butSubmit = document.getElementById('test');

butSubmit.addEventListener('click', () => {
    console.log('push');

    const name = document.getElementById('id_username').value; // получаем значение поля
    const pass = document.getElementById('id_password').value; // получаем значение поля

    $.post('login/test', { 'username': name, 'password': pass })
        .done((response) => {
        console.log('Success:', response); // обрабатываем успешный ответ
    })
        .fail((jqXHR, textStatus, errorThrown) => {
        console.error('Error:', textStatus, errorThrown); // обрабатываем ошибку
    });
});




$(document).ready(function() {
    $('#myForm').on('submit', function(event) {
        event.preventDefault(); // Предотвращает отправку формы
        const name = document.getElementById('id_username').value; // получаем значение поля
        const pass = document.getElementById('id_password').value; // получаем значение поля


        $.ajax({
            type: 'POST',
            url: 'login/test',
            data: { 'username': name, 'password': pass }, // Данные формы
            //            beforeSend: function(xhr) {
            //                xhr.setRequestHeader("X-CSRFToken", csrftoken); // Устанавливаем CSRF-токен в заголовок
            //            },
            success: function(response) {
                console.log('Успешно отправлено:', response);
            },
            error: function(xhr, status, error) {
                console.error('Ошибка при отправке:', error);
            }
        });
    });
});
