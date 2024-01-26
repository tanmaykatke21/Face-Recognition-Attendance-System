use major_project;

-- drop table if exists master_class
create table if not exists master_class
(
Class_id int primary key,
Dept_id int,
Year enum("FE","SE","TE","BE"),
Division enum("A","B","C"),
Term enum("I","II"),
Class_name varchar(20) unique not null,
Subject_1 varchar(20),
Subject_2 varchar(20),
Subject_3 varchar(20),
Subject_4 varchar(20),
Subject_5 varchar(20),
Subject_6 varchar(20)
);

desc master_class;
