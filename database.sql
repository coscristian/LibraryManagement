CREATE DATABASE library_management;
USE library_management;

CREATE TABLE Faculty(
    id varchar(20) PRIMARY KEY,
    name varchar(50) NOT NULL,
    building_number varchar(5) NOT NULL,
    code_snies2 varchar(20),
    --FOREIGN KEY code_snies2 REFERENCES Degree(code_snies) Added
);

CREATE TABLE IF NOT EXISTS Degree(
    code_snies varchar(20) PRIMARY KEY,
    name varchar(50) NOT NULL,
    total_length_in_semesters int NOT NULL,
    faculty_id1 varchar(20)  NOT NULL,
    student_id1 varchar(10) NOT NULL
    --FOREIGN KEY faculty_id1 REFERENCES Faculty(id) Added
    --FOREIGN KEY student_id1 REFERENCES Student(num_id), Added
);

CREATE TABLE IF NOT EXISTS Student (
    num_id varchar(10) PRIMARY KEY,
    name varchar(50) not null,
    last_name varchar(50) not null,
    age varchar(2) not null,
    address varchar(50),
    phone_number varchar(10),
    code_snies1 varchar(20),
    book_id2 int
    --FOREIGN KEY code_snies1 REFERENCES Degree(code_snies), Added
    --FOREIGN KEY book_id2 REFERENCES Book(id) Added
);


CREATE TABLE IF NOT EXISTS Book(
    id int AUTO_INCREMENT PRIMARY KEY,
    title varchar(50) NOT NULL,
    amount int NOT NULL,
    amount_available int NOT NULL,
    topic varchar(50),
    fk_library_employe_id int NOT NULL,
    fk_student_id int NOT NULL,
    fk_author_id int NOT NULL,
    fk_topic_id int NOT NULL,
    fk_professor_id varchar(10) NOT NULL
    --FOREIGN KEY fk_library_employe_id REFERENCES LibraryEmployee(num_id) Added
    --FOREIGN KEY fk_student_id REFERENCES Student(num_id) Added
    --FOREIGN KEY fk_author_id REFERENCES Author(id) Added
    --FOREIGN KEY fk_topic_id REFERENCES Topic(id) Added
    --FOREIGN KEY fk_professor_id REFERENCES Professor(num_id) Added
);


CREATE TABLE IF NOT EXISTS LibraryEmployee(
    num_id int PRIMARY KEY,
    name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    age varchar(2) NOT NULL,
    address varchar(50),
    phone_number varchar(10),
    salary FLOAT,
    fk_book_id5 int
    --FOREIGN KEY fk_book_id5 REFERENCES Book(id) Added
);

CREATE TABLE IF NOT EXISTS Professor(
    num_id varchar(10) PRIMARY KEY,
    name varchar(50) not null,
    last_name varchar(50) not null,
    age varchar(2) not null,
    address varchar(50),
    phone_number varchar(10),
    salary FLOAT,
    fk_book_id4 int
    --FOREIGN KEY fk_book_id4 REFERENCES Book(id) Added
);


CREATE TABLE IF NOT EXISTS Author(
    id int AUTO_INCREMENT PRIMARY KEY,
    name varchar(50) NOT NULL,
    fk_book_id1 int NOT NULL,
    --FOREIGN KEY fk_book_id1 REFERENCES Book(id) Added
);

CREATE TABLE IF NOT EXISTS Topic(
    id int AUTO_INCREMENT PRIMARY KEY,
    name varchar(50) NOT NULL,
    fk_book_id3 int NOT NULL
    --FOREIGN KEY fk_book_id3 REFERENCES Book(id) Added
);