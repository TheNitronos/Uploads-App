$( document ).on( "pagecreate", function() {
    $("#imagePrincipale").css("width", "50%");
    
    $( "#largeur" ).on( 'slidestop', function() {
        $("#imagePrincipale").css("width", $("#largeur").val()+"%");
   });
});