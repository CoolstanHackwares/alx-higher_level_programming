-- A script that lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating.
-- 	Each record should display: tv_genres.name - rating sum
-- 	Results must be sorted in descending order by their rating
-- 	You can use only one SELECT statement
-- 	The database name will be passed as an argument of the mysql command

SELECT name, SUM(tv_shows_ratings.rate) AS 'rating'
FROM tv_genres
INNER JOIN tv_shows_genres ON tv_genres.id = tv_shows_genre.genre_id
INNER JOIN tv_shows_ratings ON tv_shows_genres.show_id = tv_shows_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
