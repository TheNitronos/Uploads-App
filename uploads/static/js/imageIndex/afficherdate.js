$( document ).on( "pagebeforecreate", function() {
    $(".listeDate").each(function () {
        var date = $(this).data('date');
        var dateToAdd = '<li data-role="list-divider" id="' + date + '">' + date + '</li>';
        var boolean = $.contains( document.body, document.getElementById(date));
        if (boolean === false) {
            $(this).before(dateToAdd);
        };
    });
});