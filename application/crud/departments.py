from application.core.db import database
from application.schemas import Department

async def get_all_departments():
    query='SELECT * FROM Department'
    data = await database.fetch_all(query)

    return data


async def insert_department(department: Department):
    values = {"dep_id": department.dep_id,"dep_name":department.dep_name,}

    query = "INSERT INTO Department VALUES (:dep_id, :dep_name)"
    await database.execute(query=query, values=values)


async def delete_department(department_id):
    query = f'DELETE FROM Department WHERE dep_id="{department_id}"'
    await database.execute(query=query)