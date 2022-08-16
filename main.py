import imp
from fastapi import FastAPI

from db.database import create_db_and_tables
from endpoints import category

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(category.router)