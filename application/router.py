from fastapi import APIRouter
from application.crud.students import get_all_students,insert_student,delete_student
from application.crud.departments import get_all_departments,insert_department,delete_department
from application.crud.instructors import get_all_instructors,insert_instructor,delete_instructor
from application.crud.courses import get_all_courses,insert_course,delete_course
from application.schemas import Student,Department,Instructor,Course

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
    instructors=await get_all_instructors()
    
    return instructors

@router.post('/instructors')
async def create_instructor(instructor : Instructor):
    await insert_instructor(instructor)

@router.delete('/instructors/{instructor_id}')
async def remove_instructor(instructor_id):
    await delete_instructor(instructor_id)  




@router.get('/courses')
async def show_courses():
    courses=await get_all_courses()
    
    return courses

@router.post('/courses')
async def create_course(course : Course):
    await insert_course(course)

@router.delete('/courses/{course_id}')
async def remove_course(course_id):
    await delete_course(course_id)  
