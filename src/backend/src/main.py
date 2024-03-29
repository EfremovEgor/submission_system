from auth.router import router as auth_router
from users.router import router as users_router
from conferences.router import router as conferences_router
from submissions.router import router as submissions_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
origins = ["*"]
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
