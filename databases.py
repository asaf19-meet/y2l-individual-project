# Database related imports
# Make sure to import your tables!
from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///Project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


# Your database functions are located under here (querying, adding items, etc.)
def auth_student(student_username, student_password):
    session = DBSession()
    student = session.query(Student).filter_by(username = student_username, password= student_password).first()
    print(student)
    return student

def delete_all_students():
    session = DBSession()
    session.query(Student).delete()
    session.commit()

def add_student(student_username, student_password, student_name, student_location, student_phone_number, student_nationality):
    print("Added a student!")
    session = DBSession()
    student = Student(username=student_username,password=student_password, name=student_name, location=student_location, phone_number = student_phone_number, nationality = student_nationality)
    session.add(student)
    session.commit()

def get_student_by_username(username):
    session = DBSession()
    student = session.query(Student).filter_by(username = username).first()
    return studentudent

def get_students():
    session = DBSession()
    students = session.query(Student).all()
    return students    


def connect_student_student(student_username,other_stu):
    session = DBSession()
    student = session.query(Student).filter_by(username= student_username).first()
    student.other_stu.append(other_stu)
    session.commit()

