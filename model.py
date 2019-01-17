from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, BLOB, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    username = Column(String, primary_key = True)
    name = Column(String)
    password = Column(String)
    location = Column(String)
    phone_number = Column(String)
    nationality = Column(String)
    other_stu = Column(PickleType)

    def __repr__(self):
        return ("Student name: {}, Student's password: {}, Student's Location:{}, Phone number: {}, Nationality: {}, Other student: {}".format(self.name, self.password, self.location, self.phone_number, self.nationality, self.other_stu))
