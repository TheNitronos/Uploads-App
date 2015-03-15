$( document ).on( "pagecreate", function() {
    $( "#largeur" ).on( 'slidestop', function() {
        $("#imagePrincipale").css("width", $("#largeur").val()+"%");
   });
});
