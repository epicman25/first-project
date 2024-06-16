from fastapi import FastAPI,Path
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name : str
    age : int
    year : str
    
class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None

students = {
    1 : {
        "name" : "Tej",
        "age" : 69,
        "year" : "Year 420"
    },
    2 : {
        "name" : "Gan",
        "age" : 12,
        "year" : "Year 12"
    }
}


@app.get("/")
def index():
    return {"name":"First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(description="input the Id of the student",gt=0,lt=3)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(student_id : int,name:Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data" : "Not Found"}
        
@app.post("/create-student/{student_id}")
def create_student(student_id : int,student : Student): 
    if student_id in students:
        return {"Error" : "Student already exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student does not exists"}
    
    if student.name != None:
        students[student_id].name = student.name
        
    if student.age != None:
        students[student_id].age = student.age
        
    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error" : "Student does not exists"}
    
    del students[student_id]
    return {"Message" : "Student deleted successfully"}
    