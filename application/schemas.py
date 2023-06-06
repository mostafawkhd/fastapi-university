from pydantic.main import BaseModel


class Student(BaseModel):
    student_id: str
    student_fname: str
    student_lname: str
    student_gpa: float