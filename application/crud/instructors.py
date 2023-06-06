from application.core.db import database
from application.schemas import Instructor

async def get_all_instructors():
    query='SELECT * FROM Instructor'
    data = await database.fetch_all(query)

    return data


async def insert_instructor(instructor: Instructor):
    values = {"ins_id": instructor.ins_id,"ins_fname":instructor.ins_fname,"ins_lname":instructor.ins_lname,}

    query = "INSERT INTO Instructor VALUES (:ins_id, :ins_fname, :ins_lname)"
    await database.execute(query=query, values=values)


async def delete_instructor(instructor_id):
    query = f'DELETE FROM Instructor WHERE ins_id="{instructor_id}"'
    await database.execute(query=query)