from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class StudentCreate(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    address: Optional[str] = None
    grade: Optional[str] = None


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    address: Optional[str] = None
    grade: Optional[str] = None


class StudentResponse(BaseModel):
    id: int
    student_id: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str]
    gender: Optional[str]
    dob: Optional[date]
    address: Optional[str]
    grade: Optional[str]

    class Config:
        from_attributes = True