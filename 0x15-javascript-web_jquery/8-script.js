$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
      function(data, status) {
	  console.log(data);
	  $.each(data.results, function(i, info) {
	      $("UL#list_movies").append(`<li>${info.title}</li>`);
	  });
      });
