$(document).ready(function(){
    $("INPUT#btn_translate").click(function(){
	$.get(`https://hellosalut.stefanbohacek.dev/?lang=${$("INPUT#language_code").val()}`, function(data, status) {
	    $("DIV#hello").text(data.hello);
	});
    });
});
	
