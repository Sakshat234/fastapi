from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List
from pydantic import BaseModel
from uuid import UUID,uuid4
from models import User,Gender, Role, UserUpdateRequest 
# UserUpdateRequest

app=FastAPI()

db:List[User]=[
    User(
        id=UUID("5df668dd-9b6d-4f17-8b8d-2861dc298ead"),
        first_name="John",
        last_name="Doe",
        roles=[Role.student],
        gender=Gender.male

    ),
    User(
        id=UUID("7436e908-37d9-4fa9-9743-4fbf4d2a2937"),
        first_name="Jane",
        last_name="Doe",
        roles=[Role.student,Role.user],
        gender=Gender.female

    )
]

@app.get("/")
def root():
    return{"hello":"world"}

@app.get("/api/v1/usr")
async def fetch_users():
    return db
@app.post("/api/v1/usr")
async def add_users(user:User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/v1/usr/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if(user_id==user.id):
            db.remove(user)
        return
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exist"
    )
@app.put("/api/v1/usr/{user_id}")
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if(user_id==user.id):
            if user_update.first_name is not None:
                user.first_name=user_update.first_name
            if user_update.last_name is not None:
                user.last_name=user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name=user_update.middle_name
            if user_update.roles is not None:
                user.roles=user_update.roles
                
            