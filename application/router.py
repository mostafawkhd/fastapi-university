from fastapi import APIRouter
from application.crud.students import get_all_students

router=APIRouter()

@router.get('/students')
async def show_students():
    students=await get_all_students()
    
    return students