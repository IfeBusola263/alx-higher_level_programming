document.addEventListener("DOMContentLoaded", function() {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr",
      function(data, status) {
	  $("DIV#hello").text(data.hello);
      });
});
