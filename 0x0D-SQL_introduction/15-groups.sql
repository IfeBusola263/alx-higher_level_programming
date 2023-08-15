-- The script displays the scores and number of entires with the score
-- The syntax counts the number of entries with the same score
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score ORDER BY score DESC;
