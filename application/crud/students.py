from application.core.db import database

async def get_all_students():
    query='SELECT * FROM Student'
    data = await database.fetch_all(query)

    return data

