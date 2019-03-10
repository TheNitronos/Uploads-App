$( document ).on( "pagebeforecreate", function() {
    //pour chaque élément de la liste :
    $(".listeDate").each(function () {
        //tag (séparateur) = sa valeur (texte)
        var tag = $(this).data('tag');
        //HTML à ajouter = balise + valeur du tag
        var tagToAdd = '<li data-role="list-divider" id="' + tag + '">' + tag + '</li>';
        //booléen de contrôle si la balise éxiste déjà
        var boolean = $.contains( document.body, document.getElementById(tag));
        //si non (False): on ajoute cela avant comme un élément de la liste
        //avant celui de l'image concernée
        if (boolean === false) {
            $(this).before(tagToAdd);
        }
    });
});