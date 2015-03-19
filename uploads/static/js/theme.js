$( document ).on( "pagebeforecreate", function() {
    var theme = $("#theme").text();
    $("*").attr('data-theme', theme);
    $("*").attr('data-track-theme', theme);
    var themebtn = 'ui-btn-' + theme +"'";
});