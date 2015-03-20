$( document ).on( "pagebeforecreate", function() {
    var theme = $("#theme").text();
    $(".panel").attr('data-theme', theme);
    $(".page").attr('data-theme', theme);
    $(".header").attr('data-theme', theme);
    $(".content").attr('data-theme', theme);
    $(".footer").attr('data-theme', theme);
});