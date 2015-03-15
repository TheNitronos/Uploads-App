$( document ).ready(function() {
    $( "#modifContraste" ).on( 'slidestop', function() {
        var valeurmodifContraste = $("#modifContraste").val();
        var modifContraste = 'contrast(' + valeurmodifContraste + ')';
        
        var valeurmodifLuminosite = $("#modifLuminosite").val();
        var modifLuminosite = 'brightness(' + valeurmodifLuminosite + ')';
        
        var valeurmodifSaturation = $("#modifSaturation").val();
        var modifSaturation = 'saturate(' + valeurmodifSaturation + ')';
        
        var attribut =  modifContraste + modifLuminosite +  modifSaturation;
        $("#output").css("-webkit-filter", attribut);
    });
    $( "#modifLuminosite" ).on( 'slidestop', function() {
        var valeurmodifContraste = $("#modifContraste").val();
        var modifContraste = 'contrast(' + valeurmodifContraste + ')';
        
        var valeurmodifLuminosite = $("#modifLuminosite").val();
        var modifLuminosite = 'brightness(' + valeurmodifLuminosite + ')';
        
        var valeurmodifSaturation = $("#modifSaturation").val();
        var modifSaturation = 'saturate(' + valeurmodifSaturation + ')';
        
        var attribut =  modifContraste + modifLuminosite +  modifSaturation;
        $("#output").css("-webkit-filter", attribut);
    });
    $( "#modifSaturation" ).on( 'slidestop', function() {
        var valeurmodifContraste = $("#modifContraste").val();
        var modifContraste = 'contrast(' + valeurmodifContraste + ')';
        
        var valeurmodifLuminosite = $("#modifLuminosite").val();
        var modifLuminosite = 'brightness(' + valeurmodifLuminosite + ')';
        
        var valeurmodifSaturation = $("#modifSaturation").val();
        var modifSaturation = 'saturate(' + valeurmodifSaturation + ')';
        
        var attribut =  modifContraste + modifLuminosite +  modifSaturation;
        $("#output").css("-webkit-filter", attribut);
    });
});