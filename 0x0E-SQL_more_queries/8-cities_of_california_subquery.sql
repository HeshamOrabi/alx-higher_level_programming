-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id AS id, cities.name AS name 
FROM cities
WHERE (SELECT states.id FROM states WHERE name == 'California') == state_id
ORDER BY cities.id ASC;
