use major_project;

-- drop table if exists Attendance;
CREATE TABLE IF NOT EXISTS Attendance
(
Attendance_id int primary key,
Subject_id int,
Faculty_id int,
Attendance enum("A","P"),
Date varchar(10),
Timeslot varchar(15),
Student_id int,
Class_id int
);

desc Attendance;