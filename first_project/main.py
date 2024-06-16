from fastapi import FastAPI,Path
import uvicorn
from typing import Optional


app = FastAPI()

student = {
    1 : {
        "name" : "Tej",
        "age" : 69,
        "class" : "Year 420"
    }
}


@app.get("/")
def index():
    return {"name":"First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(description="input the Id of the student",gt=0,lt=3)):
    return student[student_id]


@app.get("/get-by-name/{student_id}")
def get_student(student_id : int,name:Optional[str] = None):
    for student_id in student:
        if student[student_id]["name"]==name:
            return student[student_id]
    return {"Data" : "Not Found"}
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)