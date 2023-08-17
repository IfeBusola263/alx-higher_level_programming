-- The scripts displays all the shows in the database linked to a genre
-- The syntax does exactly that
SELECT tv_shows.title AS title, tsg.genre_id AS genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres AS tsg
ON tv_shows.id = tsg.show_id
ORDER BY title, genre_id;
