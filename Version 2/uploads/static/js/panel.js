$( document ).on( "pagecreate", "#page", function() {
    //en cas de swipe a droite
    $( document ).on( "swiperight", "#page", function( e ) {
        //ouverture du panel
        if ( $( ".ui-page-active" ).jqmData( "panel" ) !== "open" ) {
            if ( e.type === "swiperight" ) {
                $( "#panel" ).panel( "open" );
            }
        }
    });
});