from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic Model
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

students = []

# Create Student
@app.post("/students/")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student added", "student": student}

# Get All Students
@app.get("/students/")
def get_students():
    return students

# Get Student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    return {"message": "Student not found"}

# Update Student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = updated_student
            return {"message": "Student updated", "student": updated_student}
    return {"message": "Student not found"}

# Delete Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted"}
    return {"message": "Student not found"}

Output:
Endpoint:

POST /students/

Request Body:

{
  "id": 1,
  "name": "Riya",
  "age": 21,
  "course": "Data Science"
}

Response:

{
  "message": "Student added",
  "student": {
    "id": 1,
    "name": "Riya",
    "age": 21,
    "course": "Data Science"
  }
}
