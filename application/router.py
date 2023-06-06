from fastapi import APIRouter
from application.crud.students import get_all_students,insert_student,delete_student
from application.crud.departments import get_all_departments,insert_department,delete_department
from application.crud.instructors import get_all_instructors,insert_instructor,delete_instructor
from application.schemas import Student,Department,Instructor

router=APIRouter()

@router.get('/students')
async def show_students():
    students=await get_all_students()
    
    return students

@router.post('/students')
async def create_student(student : Student):
    await insert_student(student)

@router.delete('/students/{student_id}')
async def remove_student(student_id):
        await delete_student(student_id)      




@router.get('/departments')
async def show_departments():
    students=await get_all_departments()
    
    return students

@router.post('/departments')
async def create_department(department : Department):
    await insert_department(department)

@router.delete('/departments/{department_id}')
async def remove_department(department_id):
    await delete_department(department_id)  



@router.get('/instructors')
async def show_instructors():
    students=await get_all_instructors()
    
    return students

@router.post('/instructors')
async def create_instructor(instructor : Instructor):
    await insert_instructor(instructor)

@router.delete('/instructors/{instructor_id}')
async def remove_instructor(instructor_id):
    await delete_instructor(instructor_id)  
