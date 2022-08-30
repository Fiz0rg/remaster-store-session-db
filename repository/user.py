from select import select
from sqlmodel import Session, select

from schemas.user import NewUser
from security.user import hash_password
from db.user import UserDb
from endpoints.depends import BasicCRUD


class UserRepository:
    def __init__(self, db: Session):
        self.session = db


    async def create_user(self, new_user):
        new_user.password = hash_password(new_user.password)
        result = BasicCRUD(db=self.session, model_name="UserDb")
        return await result.create(new_user)


