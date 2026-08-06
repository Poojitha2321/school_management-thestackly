from sqlalchemy.orm import Session

from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate, AttendanceUpdate


def create_attendance(db: Session, attendance: AttendanceCreate):
    db_attendance = Attendance(**attendance.model_dump())

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)

    return db_attendance


def get_attendance(db: Session):
    return db.query(Attendance).all()


def get_attendance_by_id(db: Session, attendance_id: int):
    return db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()


def update_attendance(
    db: Session,
    attendance_id: int,
    attendance: AttendanceUpdate
):
    db_attendance = get_attendance_by_id(db, attendance_id)

    if not db_attendance:
        return None

    update_data = attendance.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_attendance, key, value)

    db.commit()
    db.refresh(db_attendance)

    return db_attendance


def delete_attendance(db: Session, attendance_id: int):
    db_attendance = get_attendance_by_id(db, attendance_id)

    if not db_attendance:
        return None

    db.delete(db_attendance)
    db.commit()

    return db_attendance