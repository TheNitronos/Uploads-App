$( document ).ready(function() {
    var valeurcontraste = $(".contraste").text();
    var contraste = 'contrast(' + valeurcontraste + ') ';
    
    var valeursaturation = $(".saturation").text();
    var saturation = 'saturate(' + valeursaturation + ')';
    
    var valeurluminosite = $(".luminosite").text();
    var luminosite = 'brightness(' + valeurluminosite + ') ';
    
    var attribut =  contraste + luminosite +  saturation;
    
    var re = /,/gi;
    attribut= attribut.replace(re, ".");
    
    $("img").css("-webkit-filter", attribut);
});