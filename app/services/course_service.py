from sqlalchemy.orm import Session

from app.crud.course import (
    create_course,
    get_courses,
    get_course_by_id,
    update_course,
    delete_course,
)

from app.schemas.course import CourseCreate, CourseUpdate


def add_course(db: Session, course: CourseCreate):
    return create_course(db, course)


def get_all_courses(db: Session):
    return get_courses(db)


def get_course(db: Session, course_id: int):
    return get_course_by_id(db, course_id)


def edit_course(db: Session, course_id: int, course: CourseUpdate):
    return update_course(db, course_id, course)


def remove_course(db: Session, course_id: int):
    return delete_course(db, course_id)