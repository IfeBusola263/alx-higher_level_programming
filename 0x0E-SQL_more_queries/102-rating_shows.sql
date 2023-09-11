-- Display the show by their summed rating
-- The syntax does exactly that
SELECT tv_shows.title AS title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;