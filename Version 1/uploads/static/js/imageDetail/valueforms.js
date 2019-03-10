$( document ).on( "pagecreate", function() {
    //récupération de la description
    var description = $("#description").text();
    //écriture de celle-ci dans le 'textarea'
    $("#id_description").val(description);
});