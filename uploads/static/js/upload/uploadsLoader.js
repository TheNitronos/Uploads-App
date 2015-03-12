$( document ).ready(function() {
    var $this = $(".buttonLoad"),
    theme = $this.jqmData( "theme" ) || $.mobile.loader.prototype.options.theme,
    msgText = $this.jqmData( "msgtext" ) || $.mobile.loader.prototype.options.text,
    textVisible = $this.jqmData( "textvisible" ) || $.mobile.loader.prototype.options.textVisible,
    textonly = !!$this.jqmData( "textonly" );
    
    $( ".buttonLoad" ).click(function() {
        $.mobile.loading( "show", {
            text: msgText,
            textVisible: textVisible,
            theme: theme,
            textonly: textonly,
        });
    });
});

$( document ).on( "pagechange", function() {
    $.mobile.loading( "hide", {
    });
});


    
