var loadFile = function(event) {
    var output = document.getElementById('output');
    output.src = URL.createObjectURL(event.target.files[0]);
};

$( document ).on( "pagecreate", function() {
    $( "#contraste" ).on( 'slidestart', function(event) {
        $( "#contraste" ).on( 'slidestop', function(event) {
            var valeurcontraste = $("#contraste").val();
            var contraste = 'contrast(' + valeurcontraste + '%)';
            $("#output").css("-webkit-filter", contraste);
        });
    });
    $( "#luminosite" ).on( 'slidestart', function(event) {
        $( "#luminosite" ).on( 'slidestop', function(event) {
            var valeurluminosite = $("#luminosite").val();
            var luminosite = 'brightness(' + valeurluminosite + '%)';
            $("#output").css("-webkit-filter", luminosite);
        });
    });
    $( "#saturation" ).on( 'slidestart', function(event) {
        $( "#saturation" ).on( 'slidestop', function(event) {
            var valeursaturation = $("#saturation").val();
            var saturation = 'saturate(' + valeursaturation + '%)';
            $("#output").css("-webkit-filter", saturation);
        });
    });
});