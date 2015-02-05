var loadFile = function(event) {
    var output = document.getElementById('output');
    output.src = URL.createObjectURL(event.target.files[0]);
};

var changecontrast = function(event) {
    var contraste = document.getElementById('contraste');
    contraste += ")";
    var valeurcontraste = "contrast(";
    valeurcontraste += contraste
    
    $("#output").css("-webkit-filter",valeurcontraste);
};




