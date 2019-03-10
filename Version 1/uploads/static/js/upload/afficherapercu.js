function loadFile(input) {
    //récupération de l'image
    var output = document.getElementById('output');
    //création d'une URL vers cet objet image
    var srcImg = URL.createObjectURL(input.files[0]);
    //attribution de cette URL comme source de sorti (output)
    output.src = srcImg;
    //hauteur = 40% de celle de la page
    var hauteurpage = $( window ).height()*0.4;
    $("#output").css("height", hauteurpage);
}