$(function() {
    $('button[type=submit]').click(function (event) {
        event.preventDefault();
        $('#output').empty();
        var form = this.form;

        var data = new FormData(form);
        var url = form.action;
        $.ajax({
            type: 'POST',
            url: url,
            data: data,
            processData: false,
            contentType: false,
            dataType: 'json',
            success: function(data) {
                //console.log(data);
                $('#output').html(JSON.stringify(data, null, 2));
                Prism.highlightAll();
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });
    });
    $("#btnString").on('submit','form', function(event) {
        event.preventDefault(event);
        $('#output').empty();
        var string = $('#input-string').val();
        analyze(string);
    });
    $("#input-string").on('change keyup paste', function() {
        $('#output').empty();
        stringAnalyze($(this).val());
    });

    $("#input-string").focus();
});

function stringAnalyze(inputString) {
    $.getJSON('/api/string/analyzer', {string: inputString}, function(data) {
        //console.dir(JSON.stringify(data));
        $('#output').html(JSON.stringify(data, null, 2));
        Prism.highlightAll();
    });
}

function fileAnalyze(file) {
    $.getJSON('/api/file/analyzer', {file: file}, function(data) {
        $('#output').html(JSON.stringify(data, null, 2));
        Prism.highlightAll();
    });
}