from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(100), nullable=False)
    course_code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    duration = Column(String(50), nullable=False)

    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)

    teacher = relationship("Teacher", back_populates="courses")
    attendances = relationship(
        "Attendance",
        back_populates="course",
        cascade="all, delete-orphan"
    )