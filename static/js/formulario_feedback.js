$(document).ready(function() {
    $(document).on('submit', '#ajax-contact', function(e) {
        e.preventDefault();
        req = $.ajax({
            url : '/formulario',
            type : 'GET',
            data:{name:$("#name").val(),
                  email:$("#email").val(),
                  message:$("#message").val()},
        });
    });
});