$( document ).on( "pagebeforecreate", function() {
    $("*").attr('data-theme', 'h');
    $("*").attr('data-track-theme', 'h');
    $("button").addClass('ui-btn-h');
    $(".button").addClass('ui-btn-h');
});