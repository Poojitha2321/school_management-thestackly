from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.course import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
)

from app.services.course_service import (
    add_course,
    get_all_courses,
    get_course,
    edit_course,
    remove_course,
)

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post("/", response_model=CourseResponse)
def create_new_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    return add_course(db, course)


@router.get("/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return get_all_courses(db)


@router.get("/{course_id}", response_model=CourseResponse)
def get_course_by_id(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = get_course(db, course_id)

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@router.put("/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int,
    course: CourseUpdate,
    db: Session = Depends(get_db)
):
    updated_course = edit_course(
        db,
        course_id,
        course
    )

    if not updated_course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return updated_course


@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    deleted_course = remove_course(
        db,
        course_id
    )

    if not deleted_course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {
        "message": "Course deleted successfully"
    }