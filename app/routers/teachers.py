from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.teacher import (
    TeacherCreate,
    TeacherUpdate,
    TeacherResponse,
)

from app.services.teacher_service import (
    add_teacher_service,
    list_teachers_service,
    get_teacher_service,
    update_teacher_service,
    delete_teacher_service,
)

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"],
)


@router.post(
    "/",
    response_model=TeacherResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return add_teacher_service(db, teacher)


@router.get("/", response_model=list[TeacherResponse])
def get_all_teachers(db: Session = Depends(get_db)):
    return list_teachers_service(db)


@router.get("/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return get_teacher_service(db, teacher_id)


@router.put("/{teacher_id}", response_model=TeacherResponse)
def update_teacher(
    teacher_id: int,
    teacher: TeacherUpdate,
    db: Session = Depends(get_db),
):
    return update_teacher_service(db, teacher_id, teacher)


@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return delete_teacher_service(db, teacher_id)