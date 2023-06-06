from application.core.db import database
from application.schemas import Student

async def get_all_students():
    query='SELECT * FROM Student'
    data = await database.fetch_all(query)

    return data


async def insert_student(student: Student):
    values = {"student_id": student.student_id,"student_fname":student.student_fname,"student_lname":student.student_lname,
              'student_gpa':student.student_gpa}

    query = "INSERT INTO Student VALUES (:student_id, :student_fname, :student_lname, :student_gpa)"
    await database.execute(query=query, values=values)


async def delete_student(student_id):
    query = f'DELETE FROM Student WHERE student_id="{student_id}"'
    await database.execute(query=query)