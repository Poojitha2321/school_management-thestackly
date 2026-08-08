from datetime import date
from typing import Optional

from pydantic import BaseModel


class AttendanceBase(BaseModel):
    student_id: int
    course_id: int
    date: date
    status: str


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    student_id: Optional[int] = None
    course_id: Optional[int] = None
    date: Optional[date] = None
    status: Optional[str] = None


class AttendanceResponse(AttendanceBase):
    id: int

    class Config:
        from_attributes = True