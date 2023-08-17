-- Lists all genres linked to one show "Dexter"
-- This syntax does exactly that
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows
LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name;
