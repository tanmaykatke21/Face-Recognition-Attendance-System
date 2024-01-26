use major_project;

drop table if exists Subject;
CREATE TABLE IF NOT EXISTS Subject (
Subject_id int PRIMARY KEY,
Subject_name VARCHAR(20) NOT NULL
);

desc Subject;