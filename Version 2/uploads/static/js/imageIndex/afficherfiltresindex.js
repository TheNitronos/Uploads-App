//avant la création de la page :
$( document ).on( "pagebeforecreate", function() {
    //pour chaque élément de la liste : 
    $(".listeDate").each(function () {
        //récupération de la valeu des filtres
        var contraste = "contrast(" + $(this).data('contrast') + ")";
        var saturation = "saturate(" + $(this).data('saturate') + ")";
        var luminosite = "brightness(" + $(this).data('brightness') + ")";
        //variable composée de tous les filtres
        var attribut = contraste + luminosite + saturation;
        //remplacement des virgules par des points
        var re = /,/gi;
        attribut= attribut.replace(re, ".");
        //attribution du code CSS
        $(this).find("#image").css("-webkit-filter", attribut);
    });
    //idem pour les popup correspondantes
    $(".popup").each(function () {
        var contraste = "contrast(" + $(this).data('contrast') + ")";
        var saturation = "saturate(" + $(this).data('saturate') + ")";
        var luminosite = "brightness(" + $(this).data('brightness') + ")";
        
        var attribut = contraste + luminosite + saturation;
        
        var re = /,/gi;
        attribut= attribut.replace(re, ".");
        
        $(this).find("#image").css({"-webkit-filter": attribut, "max-height": "512px"});
    });
    
});