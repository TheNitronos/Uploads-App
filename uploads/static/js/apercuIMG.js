var loadFile = function(event) {
    var output = document.getElementById('output');
    output.src = URL.createObjectURL(event.target.files[0]);
};

var changecontrast = function(event) {
    var valeurcontraste = $("#contraste").val();
    var contraste = "contrast({})".format(valeurcontraste);
    
    $("#output").css("-webkit-filter", contraste);
};