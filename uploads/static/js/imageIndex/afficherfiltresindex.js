$( document ).on( "pagebeforecreate", function() {
    $(".liste").each(function () {
        var contraste = "contrast(" + $(this).data('contrast') + ")";
        var saturation = "saturate(" + $(this).data('saturate') + ")";
        var luminosite = "brightness(" + $(this).data('brightness') + ")";
        
        var attribut = contraste + luminosite + saturation;
        
        var re = /,/gi;
        attribut= attribut.replace(re, ".");
        
        $(this).find("#image").css("-webkit-filter", attribut);
    });
    
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