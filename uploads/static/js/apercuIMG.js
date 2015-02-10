$( document ).on( "pagecreate", function() {
    var width = $("#imageInput").width();
    var height = width/16*9;
    $("#imageInput").css("height", height)
});

    
var loadFile = function(event, input) {
    var output = document.getElementById('output');
    var img = URL.createObjectURL(input.files[0]);
    output.src = img;
    
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
            
            var attribut =  contraste + luminosite +  saturation
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
            
            var attribut =  contraste + luminosite +  saturation
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
            
            var attribut =  contraste + luminosite +  saturation
            $("#output").css("-webkit-filter", attribut);
        });
    });
});