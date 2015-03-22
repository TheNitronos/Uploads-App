$( document ).on( "pagecreate", function() {
    var description = $("#description").text();
    $("#id_description").val(description);
});