-- Displays the rating of the shows based on the rating
-- The syntax does exactly that
SELECT name, SUM(rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
NATURAL JOIN tv_show_ratings
GROUP BY name
ORDER BY rating DESC;
