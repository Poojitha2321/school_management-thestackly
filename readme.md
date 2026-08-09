**Project Name:** School Management System API  
**Date:** 6 August, 2026

## About the Project

This project is a School Management System API developed using Python and FastAPI. The main purpose of this project is to manage different school-related activities through REST APIs.

The system includes modules for authentication, students, teachers, courses, and attendance. We used MySQL as the database and SQLAlchemy to connect and work with the database.

The APIs can be tested using Swagger UI and Postman.

## Technologies Used

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Password Hashing
- Uvicorn
- Swagger UI
- Postman
- Git and GitHub

## Project Modules

### 1. Authentication

The authentication module is used for user registration and login.

Features:
- User Registration
- User Login
- JWT Authentication
- Password Hashing

### 2. Student Management

The student module is used to manage student information.

Features:
- Add Student
- Get All Students
- Get Student by ID
- Update Student
- Delete Student

### 3. Teacher Management

The teacher module is used to manage teacher information.

Features:
- Add Teacher
- Get All Teachers
- Get Teacher by ID
- Update Teacher
- Delete Teacher

### 4. Course Management

The course module is used to manage courses and assign teachers to courses.

Features:
- Create Course
- Get All Courses
- Get Course by ID
- Update Course
- Delete Course

### 5. Attendance Management

The attendance module is used to record and manage student attendance.

Features:
- Create Attendance
- Get All Attendance Records
- Get Attendance by ID
- Update Attendance
- Delete Attendance

## Team Members and Work

| Member | Module / Work |
|--------|---------------|
| **Anoop** | Authentication - Login, Register, JWT Authentication, Password Hashing |
| **Nikhil** | Student Management - Student CRUD APIs |
| **Gayathiri** | Teacher Management - Teacher CRUD APIs |
| **Poojitha** | Course & Attendance - Course CRUD APIs and Attendance APIs |
| **Sheetal** | Testing & Integration - Swagger Testing, Bug Fixes, GitHub Pull Requests, README and Final Integration |

## Project Setup

##1.The application will run at:

http://127.0.0.1:8000

##2.Run the project using Uvicorn

uvicorn app.main:app --reload


##4.Clone the project from GitHub:

git clone https://github.com/Poojitha2321/school_management-thestackly.git

