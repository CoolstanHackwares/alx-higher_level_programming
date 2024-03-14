-- Select the id of California from the states table
SELECT id FROM states WHERE name = 'California';

-- Use the id obtained from the previous query to select cities of California
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
