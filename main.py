import imp
from fastapi import FastAPI

from db.database import create_db_and_tables
from endpoints import category, goods, user

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


# @app.on_event("shutdown")
# def on_shutdown():
#     drop_db_and_tables()



app.include_router(category.router, tags=['category router'], prefix='/category')
app.include_router(goods.router, tags=['goods router'], prefix='/goods')
app.include_router(user.router, tags=['user router'], prefix='/users')
