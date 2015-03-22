function loadFile(input) {
    var output = document.getElementById('output');
    var srcImg = URL.createObjectURL(input.files[0]);
    output.src = srcImg;
    var hauteurpage = $( window ).height()*0.4;
    $("#output").css("height", hauteurpage);
}