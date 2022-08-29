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
        new = NewUser(
            name=new_user.name,
            password=hash_password(new_user.password))

        result = BasicCRUD(db=self.session, model_name="UserDb")
        return await result.create(new)

    async def patch(self, current_user, goods_id):
        statement = select(UserDb).where(UserDb.id == current_user)
        result = self.session.exec(statement)
        user = result.one()

        user.goods_id = goods_id
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user


