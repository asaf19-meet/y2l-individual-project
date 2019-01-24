# Database related imports
# Make sure to import your tables!
from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///Project.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
dession = DBSession()


# Your database functions are located under here (querying, adding items, etc.)
def auth_student(student_username, student_password):
    student = dession.query(Student).filter_by(username = student_username, password= student_password).first()
    print(student)
    return student

def delete_all_students():
    dession.query(Student).delete()
    dession.commit()

def add_student(student_username, student_password, student_name, student_location, student_phone_number, student_nationality):
    print("Added a student!")
    student = Student(username=student_username,password=student_password, name=student_name, location=student_location, phone_number = student_phone_number, nationality = student_nationality, other_stu = [])
    dession.add(student)
    dession.commit()

def get_student_by_username(username):
    student = dession.query(Student).filter_by(username = username).first()
    return student

def get_students():
    students = dession.query(Student).all()
    return students    



def connect_student_student(student_username,other_stu_username):
    print("connecting",student_username,other_stu_username)
    print(student_username,"the USErNAME")
    student = dession.query(Student).filter_by(username= student_username).first()
    student.other_stu = student.other_stu+[other_stu_username]
    print("students other stu list",student.other_stu)
    dession.add(student)
    dession.commit()

print([(a.other_stu,a.name) for a in get_students()])