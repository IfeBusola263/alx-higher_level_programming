-- Lists all show not linked to genre "Comedy"
-- This syntax does exactly that
-- Get the genre ID for comedy on tv_genre Table
-- Get the show_id linked to the genre_id
-- Display all the shows not that set, those would be the shows not linked
-- to commedy

SELECT DISTINCT title
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
-- INNER JOIN tv_genres
-- ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.id NOT IN (SELECT show_id
      FROM tv_show_genres
      INNER JOIN tv_genres
      ON tv_show_genres.genre_id = tv_genres.id
      WHERE name = "Comedy")
ORDER BY title;
