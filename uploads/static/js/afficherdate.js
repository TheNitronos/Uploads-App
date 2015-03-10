$( document ).on( "pagebeforecreate", function() {
    $(".liste").each(function () {
        var date = $(this).data('date');
        $(this).before('<li data-role="list-divider">' + date + '</li>');
    });
});