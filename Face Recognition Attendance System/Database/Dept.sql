use major_project;

-- drop table if exists Dept;
CREATE TABLE IF NOT EXISTS Dept
(
Dept_id int PRIMARY KEY,
Dept_name VARCHAR(20) NOT NULL
);

desc Dept;