$(document).ready(function(){
    // get the language from the input element with id-> language_code
    // $("INPUT#language_code").val();

    // make request on two basis: if input element with id->btn_translate is pressed
    // or if the enter key is press when the focus is on the input element with
    // id->language_code

    $("INPUT#btn_translate").click(function () {
	makeRequest($("INPUT#language_code").val());
    });
    $("INPUT#language_code").on("keypress", function (event){
	// check for the enter key, whose code is key code is 13
	if (event.which === 13){
	    makeRequest($("INPUT#language_code").val());
	}
    });

    // function to make the request
    function makeRequest(language) {
	if (language){
	    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, function(data, status){
		$("DIV#hello").text(data.hello);
	    });
	}
    }
});
