from sqlalchemy.orm import Session
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate


def create_teacher(db: Session, teacher: TeacherCreate):
    db_teacher = Teacher(**teacher.model_dump())

    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)

    return db_teacher


def get_teachers(db: Session):
    return db.query(Teacher).all()


def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()


def update_teacher(db: Session, teacher_id: int, teacher: TeacherUpdate):
    db_teacher = get_teacher(db, teacher_id)

    if not db_teacher:
        return None

    update_data = teacher.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_teacher, key, value)

    db.commit()
    db.refresh(db_teacher)

    return db_teacher


def delete_teacher(db: Session, teacher_id: int):
    db_teacher = get_teacher(db, teacher_id)

    if not db_teacher:
        return None

    db.delete(db_teacher)
    db.commit()

    return db_teacher