-- Lists all genres not linked to show "Dexter"
-- This syntax does exactly that
SELECT DISTINCT name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE id NOT IN (SELECT genre_id
FROM tv_show_genres
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE title = "Dexter")
ORDER BY name;
