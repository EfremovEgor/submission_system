from typing import Union
from auth.router import router as auth_router
from users.router import router as users_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)
