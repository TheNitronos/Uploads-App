var loadFile = function(event, input) {
    var output = document.getElementById('output');
    var img = URL.createObjectURL(input.files[0]);
    output.src = img;
    var hauteur = $( window ).height()*0.6;
    $("#output").css("max-height", hauteur)
};



$( document ).on( "pagecreate", function() {
    $( "#contraste" ).on( 'slidestart', function(event) {
        $( "#contraste" ).on( 'slidestop', function(event) {
            var valeurcontraste = $("#contraste").val();
            var contraste = 'contrast(' + valeurcontraste + ')';
            
            var valeurluminosite = $("#luminosite").val();
            var luminosite = 'brightness(' + valeurluminosite + ')';
            
            var valeursaturation = $("#saturation").val();
            var saturation = 'saturate(' + valeursaturation + ')';
            
            var attribut =  contraste + luminosite +  saturation;
            $("#output").css("-webkit-filter", attribut);
        });
    });
    $( "#luminosite" ).on( 'slidestart', function(event) {
        $( "#luminosite" ).on( 'slidestop', function(event) {
            var valeurcontraste = $("#contraste").val();
            var contraste = 'contrast(' + valeurcontraste + ')';
            
            var valeurluminosite = $("#luminosite").val();
            var luminosite = 'brightness(' + valeurluminosite + ')';
            
            var valeursaturation = $("#saturation").val();
            var saturation = 'saturate(' + valeursaturation + ')';
            
            var attribut =  contraste + luminosite +  saturation;
            $("#output").css("-webkit-filter", attribut);
        });
    });
    $( "#saturation" ).on( 'slidestart', function(event) {
        $( "#saturation" ).on( 'slidestop', function(event) {
            var valeurcontraste = $("#contraste").val();
            var contraste = 'contrast(' + valeurcontraste + ')';
            
            var valeurluminosite = $("#luminosite").val();
            var luminosite = 'brightness(' + valeurluminosite + ')';
            
            var valeursaturation = $("#saturation").val();
            var saturation = 'saturate(' + valeursaturation + ')';
            
            var attribut =  contraste + luminosite +  saturation;
            $("#output").css("-webkit-filter", attribut);
        });
    });
});