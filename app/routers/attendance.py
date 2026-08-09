from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
    AttendanceResponse,
)

from app.services.attendance_service import (
    mark_attendance,
    get_all_attendance,
    get_attendance_record,
    edit_attendance,
    remove_attendance,
)


router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# =========================
# CREATE ATTENDANCE
# =========================
@router.post("/", response_model=AttendanceResponse)
def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):
    return mark_attendance(db, attendance)


# =========================
# GET ALL ATTENDANCE
# =========================
@router.get("/", response_model=list[AttendanceResponse])
def get_attendance(
    db: Session = Depends(get_db)
):
    return get_all_attendance(db)


# =========================
# GET ATTENDANCE BY ID
# =========================
@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_attendance_by_id(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    attendance = get_attendance_record(
        db,
        attendance_id
    )

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance not found"
        )

    return attendance


# =========================
# UPDATE ATTENDANCE
# =========================
@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(
    attendance_id: int,
    attendance: AttendanceUpdate,
    db: Session = Depends(get_db)
):
    updated_attendance = edit_attendance(
        db,
        attendance_id,
        attendance
    )

    if not updated_attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance not found"
        )

    return updated_attendance


# =========================
# DELETE ATTENDANCE
# =========================
@router.delete("/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):
    deleted_attendance = remove_attendance(
        db,
        attendance_id
    )

    if not deleted_attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance not found"
        )

    return {
        "message": "Attendance deleted successfully"
    }