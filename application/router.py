from fastapi import APIRouter
from application.crud.students import get_all_students,insert_student
from application.schemas import Student

router=APIRouter()

@router.get('/students')
async def show_students():
    students=await get_all_students()
    
    return students

@router.post('/students')
async def create_student(student : Student):
    await insert_student(student)
