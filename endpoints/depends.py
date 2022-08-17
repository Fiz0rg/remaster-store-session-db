# import imp
from select import select
from sqlmodel import Session
from db.category import Category
from fastapi import Query

# from schemas.category import CategoryCreate
# from db.category import Category
from db.database import engine
from db.goods import GoodsDb


def get_session():
    with Session(engine) as session:
        yield session


models_db = {'Category': Category,
             'GoodsDb': GoodsDb}


class BasicCRUD():
    def __init__(self, db: Session, model_name: str):
        self.db_session = db # sessions
        self.models_db = models_db[model_name] # take model from dict! Think about this in future
        

    async def create(self, item):
        self.item_add = self.models_db.from_orm(item)
        self.db_session.add(self.item_add)
        self.db_session.commit()
        self.db_session.refresh(self.item_add)
        return self.item_add

    async def delete(self, category_name: str):
        one_item = self.db_session.query(self.models_db).filter(self.models_db.name == category_name).first()
        self.db_session.delete(one_item)
        self.db_session.commit()
        return  {'response': "ok"}