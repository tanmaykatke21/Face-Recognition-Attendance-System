use major_project;

-- drop table if exists Faculty;
CREATE TABLE IF NOT EXISTS Faculty
(
Faculty_id int PRIMARY KEY,
Faculty_first_name VARCHAR(20) NOT NULL,
Faculty_last_name VARCHAR(20) NOT NULL,
Email varchar(100) unique,
phone_no tinyint
);

desc Faculty;