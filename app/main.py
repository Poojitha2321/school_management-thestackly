from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, students, teachers, courses, attendance

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(students.router)
app.include_router(teachers.router)
app.include_router(courses.router)
app.include_router(attendance.router)