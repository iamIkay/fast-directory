from fastapi import FastAPI

from api import directories, users

app = FastAPI()


app.include_router(users.router)
app.include_router(directories.router)