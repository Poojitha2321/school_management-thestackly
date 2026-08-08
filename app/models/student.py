from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    gender = Column(String(10))
    dob = Column(Date)
    address = Column(String(255))
    grade = Column(String(20))