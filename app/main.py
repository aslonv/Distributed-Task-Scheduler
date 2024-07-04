# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import authenticate_user, create_access_token, get_current_user
from app.tasks import create_task, get_task_status
from datetime import timedelta
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES

app = FastAPI()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/tasks")
async def schedule_task(task_data: dict, current_user: dict = Depends(get_current_user)):
    task_id = await create_task(task_data, current_user)
    return {"task_id": task_id}

@app.get("/tasks/{task_id}")
async def task_status(task_id: str, current_user: dict = Depends(get_current_user)):
    status = await get_task_status(task_id)
    return {"status": status}
