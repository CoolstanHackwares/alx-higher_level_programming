-- A script that lists all genres in the database hbtn_0d_tvshows_rate
-- by their rating.
-- 	Each record should display: tv_genres.name - rating sum
-- 	Results must be sorted in descending order by their rating
-- 	You can use only one SELECT statement
-- 	The database name will be passed as an argument of the mysql command

SELECT tv_genres.name, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_genres
JOIN hbtn_0d_tvshows ON tv_genres.id = hbtn_0d_tvshows.genre_id
JOIN hbtn_0d_tvshows_rate ON hbtn_0d_tvshows.id = hbtn_0d_tvshows_rate.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
