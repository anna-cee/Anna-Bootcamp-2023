drop table DEPARTMENTS CASCADE ;
drop table PROJECTS CASCADE;
drop table EMPLOYEES CASCADE;
drop table HOUR_ASSIGNMENTS CASCADE;

CREATE TABLE DEPARTMENTS (
dept_id integer PRIMARY KEY,
dept_name text NOT NULL);

CREATE TABLE PROJECTS(
proj_id integer PRIMARY KEY,
proj_name text NOT NULL,
proj_location text DEFAULT 'Online'
);

CREATE TABLE EMPLOYEES(
emp_id integer PRIMARY KEY,
first_name text NOT NULL,
last_name text NOT NULL,
dob date,
department_id integer NOT NULL,
FOREIGN KEY (department_id) REFERENCES DEPARTMENTS(dept_id));

CREATE TABLE HOUR_ASSIGNMENTS(
hour_assignment_id serial PRIMARY KEY,
project_id integer NOT NULL,
employee_id integer NOT NULL,
hours decimal (6,2) NOT NULL CHECK (hours > 0),
FOREIGN KEY(project_id) REFERENCES PROJECTS(proj_id) ON DELETE CASCADE,
FOREIGN KEY(employee_id) REFERENCES EMPLOYEES(emp_id) ON DELETE CASCADE);

ALTER TABLE EMPLOYEES 
ADD COLUMN position text DEFAULT 'Software developer';

INSERT INTO DEPARTMENTS (dept_id, dept_name) VALUES (10, 'IT');
INSERT INTO DEPARTMENTS VALUES (11, 'Marketing');
INSERT INTO EMPLOYEES VALUES (1, 'Susan', 'McDonald', '12/03/1995', 12, 'Project manager');