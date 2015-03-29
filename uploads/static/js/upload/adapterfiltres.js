$( document ).ready(function() {
    //chaque fois qu'un curseur s'arrête : 
    $( "#contraste" ).on( 'slidestop', function() {
        //chaque fois qu'un curseur s'arrête : 
        var valeurcontraste = $("#contraste").val();
        var contraste = 'contrast(' + valeurcontraste + ')';
        
        var valeurluminosite = $("#luminosite").val();
        var luminosite = 'brightness(' + valeurluminosite + ')';
        
        var valeursaturation = $("#saturation").val();
        var saturation = 'saturate(' + valeursaturation + ')';
        
        var attribut =  contraste + luminosite +  saturation;
        //récupération de la valeur de chaque curseur
        $("#output").css("-webkit-filter", attribut);
    });
    $( "#luminosite" ).on( 'slidestop', function() {
        var valeurcontraste = $("#contraste").val();
        var contraste = 'contrast(' + valeurcontraste + ')';
        
        var valeurluminosite = $("#luminosite").val();
        var luminosite = 'brightness(' + valeurluminosite + ')';
        
        var valeursaturation = $("#saturation").val();
        var saturation = 'saturate(' + valeursaturation + ')';
        
        var attribut =  contraste + luminosite +  saturation;
        $("#output").css("-webkit-filter", attribut);
    });
    $( "#saturation" ).on( 'slidestop', function() {
        var valeurcontraste = $("#contraste").val();
        var contraste = 'contrast(' + valeurcontraste + ')';
        
        var valeurluminosite = $("#luminosite").val();
        var luminosite = 'brightness(' + valeurluminosite + ')';
        
        var valeursaturation = $("#saturation").val();
        var saturation = 'saturate(' + valeursaturation + ')';
        
        var attribut =  contraste + luminosite +  saturation;
        $("#output").css("-webkit-filter", attribut);
    });
});