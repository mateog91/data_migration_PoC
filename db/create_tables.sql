CREATE TABLE departments (
	id int NOT NULL,
	department varchar NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE jobs (
	id int NOT NULL,
	job varchar NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE hired_employees (
	id int NOT NULL,
	name varchar,
	datetime varchar,
	department_id int,
	job_id int,
	PRIMARY KEY (id)
);

ALTER TABLE hired_employees ADD CONSTRAINT hired_employees_fk0 FOREIGN KEY (department_id) REFERENCES departments(id);

ALTER TABLE hired_employees ADD CONSTRAINT hired_employees_fk1 FOREIGN KEY (job_id) REFERENCES jobs(id);




