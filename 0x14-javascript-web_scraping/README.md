# JavaScript - Web scraping
This project is about querrying data from a server using an API in JavaScript.

* 0-readme.js
```
A script that reads and prints the content of a file.

  The first argument is the file path
  The content of the file must be read in utf-8	
  If an error occurred during the reading, print the error object
```

* 1-writeme.js
```
A script that writes a string to a file.

  The first argument is the file path
  The second argument is the string to write
  The content of the file must be written in utf-8
  If an error occurred during while writing, print the error object
```

* 2-statuscode.js
```
A script that display the status code of a GET request.

  The first argument is the URL to request (GET)
  The status code must be printed like this: code: <status code>
  Uses the module request
```

* 3-starwars_title.js
```
A script that prints the title of a Star Wars movie where the episode number matches a given integer.

  The first argument is the movie ID
  You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
  Uses the module request
```

* 4-starwars_count.js
```
A script that prints the number of movies where the character 'Wedge Antilles' is present.

  The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
  Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
  Uses the module request
```

* 5-request_store.js
```
A script that gets the contents of a webpage and stores it in a file.

  The first argument is the URL to request
  The second argument the file path to store the body response
  The file must be UTF-8 encoded
  Uses the module request
```

* 6-completed_tasks.js
```
A script that computes the number of tasks completed by user id.

  The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
  Only print users with completed task
  You must use the module request
```

* 100-starwars_characters.js
```
A script that prints all characters of a Star Wars movie:

  The first argument is the Movie ID - example: 3 = "Return of the Jedi"
  Displays one character name by line
  Used the Star wars API
  Uses the module request
```

* 101-starwars_characters.js
```
A script that prints all characters of a Star Wars movie:

  The first argument is the Movie ID - example: 3 = "Return of the Jedi"
  Display one character name by line in the same order of the list "characters" in the /films/ response
  Using the Star wars API
  Uses the module request
```
[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)
