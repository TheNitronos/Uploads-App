$( document ).on( "pagecreate", function() {
    var tag = $("#tag").text();
    $("#id_tag").val(tag);
    
    var description = $("#description").text();
    $("#id_description").val(description);
});