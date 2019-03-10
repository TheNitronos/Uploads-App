$(document).delegate('.ui-navbar a', 'click', function () {
    //annulation de l'apparence 'active' des boutons
    $("#btnmodifier").removeClass("ui-btn-active");
    $("#btnsupprimer").removeClass("ui-btn-active");
    $("#btnimage").removeClass("ui-btn-active");
    
    //bouton cliqué rendu 'active'
    $(this).addClass('ui-btn-active');
    
    //tout le contenu est caché
    $("#image").hide();
    $("#modifier").hide();
    $("#supprimer").hide();
    
    //seul le contenu correspondant au bouton cliqué est affiché
    $('#' + $(this).attr("data-href")).show("swing");
    
});