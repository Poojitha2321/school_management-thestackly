from pydantic import BaseModel, EmailStr
from typing import Optional


class TeacherCreate(BaseModel):
    teacher_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    subject: Optional[str] = None
    qualification: Optional[str] = None
    experience: Optional[int] = None


class TeacherUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    subject: Optional[str] = None
    qualification: Optional[str] = None
    experience: Optional[int] = None


class TeacherResponse(BaseModel):
    id: int
    teacher_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    subject: Optional[str]
    qualification: Optional[str]
    experience: Optional[int]

    class Config:
        from_attributes = True