-- Lists all genres linked to one show "Dexter"
-- This syntax does exactly that
SELECT DISTINCT title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE name = "Comedy"
ORDER BY title;
