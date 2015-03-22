$( document ).on( "pagecreate", "#page", function() {
    $( document ).on( "swiperight", "#page", function( e ) {
        if ( $( ".ui-page-active" ).jqmData( "panel" ) !== "open" ) {
            if ( e.type === "swiperight" ) {
                $( "#panel" ).panel( "open" );
            }
        }
    });
});