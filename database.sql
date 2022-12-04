CREATE DATABASE library_management;
USE library_management;

CREATE TABLE IF NOT EXISTS Employee (
    num_id varchar(10) PRIMARY KEY,
    name varchar(50) not null,
    last_name varchar(50) not null,
    age varchar(2) not null,
    address varchar(50),
    phone_number varchar(10),
    salary float
);

CREATE TABLE IF NOT EXISTS Student (
    num_id varchar(10) PRIMARY KEY,
    name varchar(50) not null,
    last_name varchar(50) not null,
    age varchar(2) not null,
    address varchar(50),
    phone_number varchar(10),
    semester int 
);