-- Select the id of California from the states table
-- Use the id obtained from the previous query to select cities of California

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
