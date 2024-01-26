use major_project;

create table if not exists login
(
username varchar(100) primary key NOT NULL,
password varchar(15) NOT NULL,
security_question varchar(100),
security_answer varchar(100),
role enum("admin","student","faculty"),
login_count int
);