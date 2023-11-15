-- script that creates the database hbtn_0d_usa and the table cities on your MySQL server.
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
