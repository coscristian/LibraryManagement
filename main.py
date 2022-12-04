import mysql.connector
import model.author as author
import model.book as book
import model.student as student
import model.degree as degree


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

    carrera1 = degree.Degree("Ingeniería de sistemas", "123", 10)

    estudiante1 = student.Student("1087489628", "Cristian", "Quesada Cossio", "20", "Manzana 7 Casa 5 Tinajas", "3207101556", 5, carrera1)
    estudiante2 = student.Student("35586755", "Yuldavis", "Cossio Perea", "47", "Manzana 7 Casa 5 Tinajas", "3104131241", 8, carrera1)

    autor1 = author.Author("Oscár Ramirez")
    autor2 = author.Author("Luis Ruelas")

    libro1 = book.Book("978-958-778-722-1", "Python a fondo", 5, 3, "Tecnologia", [autor1])
    libro2 = book.Book("978-958-778-722-2", "Unity y C#", 5, 3, "Tecnologia", [autor2])
    libro3 = book.Book("978-958-778-722-3", "Aprender PHP, MySQL y JavaScript", 5, 3, "Tecnologia", [])
    libro4 = book.Book("978-958-778-722-4", "Python a fondo", 5, 3, "Tecnologia", [])

    estudiante1.lend_book(libro1)
    estudiante2.lend_book(libro2)
    estudiante2.lend_book(libro3)

    print(f"Name: {estudiante1.get_name()} \n\t Books: {estudiante1.get_books()}")

except:
    print("BBDD ha fallado")
