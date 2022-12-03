import mysql.connector
from model.Person import *

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Quesada-123",
    database = "Library"
)

def create_employee_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            num_id varchar(10) PRIMARY KEY,
            name varchar(50) not null,
            last_name varchar(50) not null,
            age varchar(2) not null,
            address varchar(50),
            phone_number varchar(10),
            salary float
        );
    """
    ) 

def create_student_table(cursor):    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            num_id varchar(10) PRIMARY KEY,
            name varchar(50) not null,
            last_name varchar(50) not null,
            age varchar(2) not null,
            address varchar(50),
            phone_number varchar(10),
            semester int 
        );
    """
    ) 
    
try:
    cursor = database.cursor() #Permite ejecutar sentencias sql desde python
    create_employee_table(cursor)
    create_student_table(cursor)

except:
    print("BBDD ha fallado")