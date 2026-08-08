from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.crud.student import (
    create_student,
    get_students,
    get_student,
    update_student,
    delete_student,
)

from app.schemas.student import StudentCreate, StudentUpdate


def add_student_service(db: Session, student: StudentCreate):
    return create_student(db, student)


def list_students_service(db: Session):
    return get_students(db)


def get_student_service(db: Session, student_id: int):
    student = get_student(db, student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


def update_student_service(
    db: Session,
    student_id: int,
    student: StudentUpdate,
):
    updated = update_student(db, student_id, student)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return updated


def delete_student_service(db: Session, student_id: int):
    deleted = delete_student(db, student_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}