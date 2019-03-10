$( document ).ready(function() {
    //chaque fois qu'un curseur s'arrête : 
    $( "#modifContraste" ).on( 'slidestop', function() {
        //récupération de la valeur de chaque curseur
        var valeurmodifContraste = $("#modifContraste").val();
        var modifContraste = 'contrast(' + valeurmodifContraste + ')';
        
        var valeurmodifLuminosite = $("#modifLuminosite").val();
        var modifLuminosite = 'brightness(' + valeurmodifLuminosite + ')';
        
        var valeurmodifSaturation = $("#modifSaturation").val();
        var modifSaturation = 'saturate(' + valeurmodifSaturation + ')';
        
        var attribut =  modifContraste + modifLuminosite +  modifSaturation;
        //ajout du code CSS avec -webkit-filter sur l'image d'aperçu
        $("#output").css("-webkit-filter", attribut);
    });
    //idem
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
    //idem
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