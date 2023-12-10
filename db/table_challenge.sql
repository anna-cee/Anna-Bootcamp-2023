DROP TABLE STUDENTS;
DROP TABLE TEACHERS;
DROP TABLE SUBJECTS;
DROP TABLE ENROLMENTS; 

CREATE TABLE STUDENTS (
    student_id serial primary key,
    f_name varchar(50) not null, 
    l_name varchar(50) not null,
    dob date not null
);

CREATE TABLE TEACHERS (
    teacher_id serial primary key,
    name varchar(50) not null
);

CREATE TABLE SUBJECTS (
    subject_id serial primary key,
    subject_name varchar(100) not null,

    teacher_id integer,
    FOREIGN KEY (teacher_id) REFERENCES TEACHERS (teacher_id) ON DELETE SET NULL
);

CREATE TABLE ENROLMENTS (
    enrolment_id serial primary key,
    enrolment_date date DEFAULT CURRENT_DATE,

    student_id integer not null,
    FOREIGN KEY (student_id) REFERENCES STUDENTS (student_id) ON DELETE CASCADE,
    subject_id integer not null,
    FOREIGN KEY (subject_id) REFERENCES SUBJECTS (subject_id) ON DELETE CASCADE

);

ALTER TABLE STUDENTS
ADD COLUMN email text NOT NULL;

ALTER TABLE TEACHERS
RENAME COLUMN name TO f_name;

ALTER TABLE TEACHERS
ADD COLUMN l_name text NOT NULL;

ALTER TABLE SUBJECTS
ADD COLUMN area text DEFAULT 'Databases';