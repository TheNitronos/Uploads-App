$( document ).on( "pagecreate", function() {
    $("#btnCompression").click(function() {
        var input = $("#imageInput").val();
        
        if (input == "") {
            $( "#popupNoImage" ).popup( "open", {transition: "slide"});
            
        }
        else {
            var sourceImage = document.getElementById('output');
            
            var cvs = document.createElement('canvas');
            var quality = 10;
            cvs.width = sourceImage.naturalWidth;
            cvs.height = sourceImage.naturalHeight;
            var newImageData = cvs.toDataURL("image/jpeg", quality/100);
            var result_image = new Image();
            result_image.src = newImageData;
            
            var output = document.getElementById('output');
            var source = result_image.src;
            output.src = source;
        }
    });
});