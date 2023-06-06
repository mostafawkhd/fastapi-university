from pydantic.main import BaseModel


class Student(BaseModel):
    student_id: str
    student_fname: str
    student_lname: str
    student_gpa: float

class Course(BaseModel):
    crs_id: str
    crs_title: str
    ins_id: str
    dep_id: str 

class Instructor(BaseModel):
    ins_id: str
    ins_fname: str
    ins_lname: str 

class Department(BaseModel):
    dep_id: str
    dep_name: str          