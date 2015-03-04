var loadFile = function(input) {
    var output = document.getElementById('output');
    var srcImg = URL.createObjectURL(input.files[0]);
    output.src = srcImg;
    var hauteurpage = $( window ).height()*0.6;
    $("#output").css("max-height", hauteurpage)
};

$( document ).on( "pagecreate", function() {
    $( "#contraste" ).on( 'slidestop', function() {
            var valeurcontraste = $("#contraste").val();
            var contraste = 'contrast(' + valeurcontraste + ')';
            
            var valeurluminosite = $("#luminosite").val();
            var luminosite = 'brightness(' + valeurluminosite + ')';
            
            var valeursaturation = $("#saturation").val();
            var saturation = 'saturate(' + valeursaturation + ')';
            
            var attribut =  contraste + luminosite +  saturation;
            $("#output").css("-webkit-filter", attribut);
    });
    $( "#luminosite" ).on( 'slidestop', function() {
            var valeurcontraste = $("#contraste").val();
            var contraste = 'contrast(' + valeurcontraste + ')';
            
            var valeurluminosite = $("#luminosite").val();
            var luminosite = 'brightness(' + valeurluminosite + ')';
            
            var valeursaturation = $("#saturation").val();
            var saturation = 'saturate(' + valeursaturation + ')';
            
            var attribut =  contraste + luminosite +  saturation;
            $("#output").css("-webkit-filter", attribut);
    });
    $( "#saturation" ).on( 'slidestop', function() {
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