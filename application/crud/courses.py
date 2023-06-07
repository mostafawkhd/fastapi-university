from application.core.db import database
from application.schemas import Course

async def get_all_courses():
    query='SELECT Course.crs_id,Course.crs_title,Course.dep_id,Instructor.ins_fname,Instructor.ins_lname FROM Course INNER JOIN Instructor ON Course.ins_id=Instructor.ins_id'
    data = await database.fetch_all(query)

    return data


async def insert_course(course: Course):
    values = {"crs_id": course.crs_id,"crs_title":course.crs_title,"ins_id":course.ins_id,"dep_id":course.dep_id}

    query = "INSERT INTO Course VALUES (:crs_id, :crs_title, :ins_id, :dep_id)"
    await database.execute(query=query, values=values)


async def delete_course(course_id):
    query = f'DELETE FROM Course WHERE crs_id="{course_id}"'
    await database.execute(query=query)