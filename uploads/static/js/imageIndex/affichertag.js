$( document ).on( "pagebeforecreate", function() {
    $(".listeDate").each(function () {
        var tag = $(this).data('tag');
        var tagToAdd = '<li data-role="list-divider" id="' + tag + '">' + tag + '</li>';
        var boolean = $.contains( document.body, document.getElementById(tag));
        if (boolean === false) {
            $(this).before(tagToAdd);
        };
    });
});