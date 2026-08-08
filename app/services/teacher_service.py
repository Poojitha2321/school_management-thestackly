from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.crud.teacher import (
    create_teacher,
    get_teachers,
    get_teacher,
    update_teacher,
    delete_teacher,
)

from app.schemas.teacher import TeacherCreate, TeacherUpdate


def add_teacher_service(db: Session, teacher: TeacherCreate):
    return create_teacher(db, teacher)


def list_teachers_service(db: Session):
    return get_teachers(db)


def get_teacher_service(db: Session, teacher_id: int):
    teacher = get_teacher(db, teacher_id)

    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found"
        )

    return teacher


def update_teacher_service(
    db: Session,
    teacher_id: int,
    teacher: TeacherUpdate,
):
    updated = update_teacher(db, teacher_id, teacher)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found"
        )

    return updated


def delete_teacher_service(db: Session, teacher_id: int):
    deleted = delete_teacher(db, teacher_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found"
        )

    return {"message": "Teacher deleted successfully"}