from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
students={
    1:{
        'name':'Ali',
        'age':22
    }
}

@app.get('/')
def index():
    return {'name':'Mostafa','age':22}  

@app.get('/students/{student_id}')
def get_student(student_id:int):
    return students[student_id]   