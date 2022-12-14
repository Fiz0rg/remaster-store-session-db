# import imp
from select import select
from sqlmodel import Session
from fastapi import Query

from db.database import engine
from db.category import Category
from db.user import UserDb, GoodsDb


def get_session():
    with Session(engine) as session:
        yield session


models_db = {'Category': Category,
             'GoodsDb': GoodsDb,
             'UserDb': UserDb,
             }


class BasicCRUD:
    def __init__(self, db: Session, model_name: str):
        self.db_session = db # sessions
        self.models_db = models_db[model_name] # take model from dict! Think about this in future
        

    async def create(self, item_name):
        item_add = self.models_db.from_orm(item_name)
        self.db_session.add(item_add)
        self.db_session.commit()
        self.db_session.refresh(item_add)
        return item_add

    async def delete(self, category_name: str):
        one_item = self.db_session.query(self.models_db).filter(self.models_db.name == category_name).first()
        self.db_session.delete(one_item)
        self.db_session.commit()
        return  {'response': "ok"}