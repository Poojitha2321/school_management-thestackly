from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth
from app.routers import students
from app.models.student import Student


app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(students.router)


@app.get("/")
def home():
    return {"message": "School Management API is running"}