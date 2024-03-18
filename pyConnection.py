iimport psycopg2
from psycopg2 import sql

# Function to connect to the PostgreSQL database
def connect():
    conn = psycopg2.connect(
        dbname="SchoolApplication",
        user="postgres",
        password="7685",
        host="localhost",
        port="5432"
    )
    return conn
    
def getAllStudents():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows
    
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, email, enrollment_date)
    )
    conn.commit()
    conn.close()


def updateStudentEmail(student_id, new_email):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s",
        (new_email, student_id)
    )
    conn.commit()
    conn.close()

def deleteStudent(student_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM students WHERE student_id = %s",
        (student_id,)
    )
    conn.commit()
    conn.close()

def main():
  print("All students listed: ")
  displayAllStudents()

  print("\n Adding student Nitika to the school:")
  addStudent("Nitika", "Bhardwaj", "nitikabhardwaj@cmail.carleton.ca", "2024-03-17")
  print("\n All students in the school after adding Nitika: ")
  displayAllStudents()

  print("\n Updating the email for student with student_id 1")
  updateStudentEmail(1, "john_new_email@example.com")
  print("\n All the students in this school after updating the email for student with student_id 1: ")
  displayAllStudents()

  print("\n Deleting the student with student_id 2")
  deleteStudent(2)
  print("\n All the students in this school after deleting the student with student_id 2: ")
  displayAllStudents()

main()
