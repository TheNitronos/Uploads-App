$( document ).on( "pagecreate", function() {
    $( ".popupIMG" ).on({
        popupbeforeposition: function() {
        var maxHeight = $( window ).height() - 60 + "px";
        $( ".popupIMG img" ).css( "max-height", maxHeight );
        }
    });
});