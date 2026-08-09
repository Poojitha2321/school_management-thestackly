from pydantic import BaseModel
from typing import Optional


class CourseBase(BaseModel):
    course_name: str
    course_code: str
    description: Optional[str] = None
    duration: str
    teacher_id: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    course_name: Optional[str] = None
    course_code: Optional[str] = None
    description: Optional[str] = None
    duration: Optional[str] = None
    teacher_id: Optional[int] = None


class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True