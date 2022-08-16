# import imp
from select import select
from sqlmodel import Session
from db.category import Category
from fastapi import Query

# from schemas.category import CategoryCreate
# from db.category import Category
from db.database import engine


def get_session():
    with Session(engine) as session:
        yield session


models_db = {'Category': Category}


class BasicCRUD():
    def __init__(self, db: Session, model_name: str, item):
        self.db_session = db # sessions
        self.models_db = models_db[model_name] # take model from dict
        self.item_add = self.models_db.from_orm(item) # vs repeat code
        

    async def create(self):
        self.db_session.add(self.item_add)
        self.db_session.commit()
        self.db_session.refresh(self.item_add)
        return self.item_add

    async def delete(self, category_name):
        self.db_session.delete(self.item_add)