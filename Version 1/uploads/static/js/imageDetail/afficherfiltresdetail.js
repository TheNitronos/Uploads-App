//avant la création de la page :

$( document ).on( "pagebeforecreate", function() {
    //recupération de la valeur de chaque filtre
    var valeurcontraste = $(".contraste").text();
    //balise CSS pour les filtres correspondants
    var contraste = 'contrast(' + valeurcontraste + ') ';
    
    var valeursaturation = $(".saturation").text();
    var saturation = 'saturate(' + valeursaturation + ')';
    
    var valeurluminosite = $(".luminosite").text();
    var luminosite = 'brightness(' + valeurluminosite + ') ';
    
    //mise en commun des attributs pour le CSS
    var attribut =  contraste + luminosite +  saturation;
    
    //remplacement des virgules des valeurs par des points 
    var re = /,/gi;
    attribut= attribut.replace(re, ".");
    
    //ajout du code CSS avec -webkit-filter
    $("img").css("-webkit-filter", attribut);
});