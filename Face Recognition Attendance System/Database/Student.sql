USE major_project;

-- -- Drop table if exists Student;
-- DROP TABLE IF EXISTS Student;

-- Create table Student
CREATE TABLE IF NOT EXISTS Student (
    Class ENUM('FE Comps A', 'FE Comps B', 'FE Comps C', 'SE Comps A', 'SE Comps B', 'SE Comps C', 'TE Comps A', 'TE Comps B', 'TE Comps C', 'BE Comps A', 'BE Comps B', 'BE Comps C', 'FE I.T A', 'FE I.T B', 'FE I.T C', 'SE I.T A', 'SE I.T B', 'SE I.T C', 'TE I.T A', 'TE I.T B', 'TE I.T C', 'BE I.T A', 'BE I.T B', 'BE I.T C', 'FE Mech A', 'FE Mech B', 'FE Mech C', 'SE Mech A', 'SE Mech B', 'SE Mech C', 'TE Mech A', 'TE Mech B', 'TE Mech C', 'BE Mech A', 'BE Mech B', 'BE Mech C', 'FE Civil A', 'FE Civil B', 'FE Civil C', 'SE Civil A', 'SE Civil B', 'SE Civil C', 'TE Civil A', 'TE Civil B', 'TE Civil C', 'BE Civil A', 'BE Civil B', 'BE Civil C', 'FE EXTC A', 'FE EXTC B', 'FE EXTC C', 'SE EXTC A', 'SE EXTC B', 'SE EXTC C', 'TE EXTC A', 'TE EXTC B', 'TE EXTC C', 'BE EXTC A', 'BE EXTC B', 'BE EXTC C', 'FE Electrical A', 'FE Electrical B', 'FE Electrical C', 'SE Electrical A', 'SE Electrical B', 'SE Electrical C', 'TE Electrical A', 'TE Electrical B', 'TE Electrical C', 'BE Electrical A', 'BE Electrical B', 'BE Electrical C') NOT NULL,
    Student_id VARCHAR(20) PRIMARY KEY,
    Student_name VARCHAR(20) NOT NULL,
    Roll_no TINYINT,
    Email VARCHAR(100) UNIQUE,
    phone_no VARCHAR(10)
);

-- Describe the table
DESC Student;
