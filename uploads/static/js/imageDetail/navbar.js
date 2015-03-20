$(document).delegate('.ui-navbar a', 'click', function () {
    $("#btnmodifier").removeClass("ui-btn-active");
    $("#btnsupprimer").removeClass("ui-btn-active");
    $("#btnimage").removeClass("ui-btn-active");
    
    $(this).addClass('ui-btn-active');
    
    $("#image").hide();
    $("#modifier").hide();
    $("#supprimer").hide();
    
    $('#' + $(this).attr("data-href")).show("swing");
    
});