from app.routers import students
from app.database import Base, engine

app.include_router(students.router)