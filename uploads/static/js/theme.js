$( document ).on( "pagebeforecreate", function() {
    var theme = $("#theme").text();
    $(".panel").attr('data-theme', theme);
    $(".page").attr('data-theme', theme);
    $(".header").attr('data-theme', theme);
    $(".content").attr('data-theme', theme);
    $(".footer").attr('data-theme', theme);
    
    $(".liste").attr('data-theme', theme);
    $(".popup").attr('data-theme', theme);
    $(".popup").attr('data-overlay-theme', theme);
    
    var titre = 'ui-bar-' + theme;
    $(".titre").addClass(titre);
    
    var paragraphe = 'ui-body-' + theme;
    $(".paragraphe").addClass(paragraphe);
    
    var bouton = 'ui-btn-' + theme;
    $(".button").addClass(bouton);
    
    var page = 'ui-page-theme-' + theme;
    $(".page").addClass(page);
    
    var panel = 'ui-page-theme-' + theme;
    $(".panel").addClass(panel);
    
});