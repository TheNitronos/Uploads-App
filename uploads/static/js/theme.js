$( document ).on( "pagebeforecreate", function() {
    $("*").attr('data-theme', 'a');
    $("*").attr('data-track-theme', 'a');
    $("button").addClass('ui-btn-a');
    $(".button").addClass('ui-btn-a');
});