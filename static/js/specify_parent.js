$(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#specify-parent-modal").modal("show");
            },
            success: function (data) {
                $("#specify-parent-modal .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    if (data.user_exist) {
                        $("#parent-block").html(data.parent_html);

                        $("#current-month-amount-block").html(data.current_month_amount_html);

                        $("#amount-block").html(data.amount_html);

                        $("#accumulate-block").html(data.accumulate_html);

                        $("#specify-parent-modal").modal("hide");
                    }
                    else {
                        $(".specify-parent-alert").show();
                         setTimeout(function(){
                             $('.specify-parent-alert').hide();
                         }, 5000);
                    }
                }
                else {
                    $("#specify-parent-modal .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

    $(".specify-parent-btn").click(loadForm);
    $("#specify-parent-modal").on("submit", ".specify-parent-form", saveForm);
});