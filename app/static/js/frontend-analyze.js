$(document).ready(function(){
	$(document).on('submit','form', function(event) {
        event.preventDefault();
        var inputString = $('#input-string').val();
        analyze(inputString);
    });

    $("#input-string").on('change keyup paste', function() {
        analyze($(this).val());
    });

    $("#input-string").focus();

});

function analyze(inputString) {
    $.getJSON('/api/string/analyzer', {string: inputString}, function(data) {
        //console.dir(JSON.stringify(data));
        $('#output').empty();
        $('#output').html(JSON.stringify(data, null, 2));
        Prism.highlightAll();
    });
}