use major_project;

-- drop table if exists subject_allocation
create table if not exists subject_allocation
(
allocation_id int primary key,
Faculty_id int,
Class_id int,
Subject_id int
);

desc subject_allocation;
