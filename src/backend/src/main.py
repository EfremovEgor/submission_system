from typing import Union
from auth.router import router as auth_router
from users.router import router as users_router
from conferences.router import router as conferences_router
from submissions.router import router as submissions_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:3000",
    "http://frontend",
    "http://frontend:3000",
    "http://frontend:80",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(conferences_router)
app.include_router(submissions_router)
