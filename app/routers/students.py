from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
)

from app.services.student_service import (
    add_student_service,
    list_students_service,
    get_student_service,
    update_student_service,
    delete_student_service,
)

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return add_student_service(db, student)


@router.get("/", response_model=list[StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    return list_students_service(db)


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return get_student_service(db, student_id)


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db),
):
    return update_student_service(db, student_id, student)


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return delete_student_service(db, student_id)