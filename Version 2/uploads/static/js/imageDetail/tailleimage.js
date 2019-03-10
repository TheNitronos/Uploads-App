$( document ).on( "pagecreate", function() {
    //largeur de l'image est de 50% à la base
    $("#imagePrincipale").css("width", "50%");
    
    //à l'arrêt du curseur, la valeur est récuperée et attribuée comme valeur de largeur en
    //pourcentage
    $( "#largeur" ).on( 'slidestop', function() {
        $("#imagePrincipale").css("width", $("#largeur").val()+"%");
   });
});