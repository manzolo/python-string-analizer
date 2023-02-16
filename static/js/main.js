$('form').on('submit', function(event) {
    event.preventDefault();
    var inputString = $('#input-string').val();
    $.getJSON('/api/string/analyzer', {string: inputString}, function(data) {
        console.dir(JSON.stringify(data));
        $('#output').empty();
        $('#output').html(JSON.stringify(data, null, 2));
        Prism.highlightAll();
    });
});