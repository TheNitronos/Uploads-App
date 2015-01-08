var templatePanel = document.querySelector('.panel');
var panel = templatePanel.import.querySelector('#panelContent');

$( document ).on( "pagebeforecreate", "#page", function() {
    $("#panel").prepend(panel);
    
    $( document ).on( "swiperight", "#page", function( e ) {
        if ( $( ".ui-page-active" ).jqmData( "panel" ) !== "open" ) {
            if ( e.type === "swiperight" ) {
                $( "#panel" ).panel( "open" );
            }
        }
    });
});
