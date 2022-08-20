from sqlmodel import Session

from schemas import user
from security.user import hash_password
from db.user import UserDb
from endpoints.depends import BasicCRUD


class UserRepository:
    def __init__(self, db: Session):
        self.session = db


    async def create_user(self, new_user):
        new = user.NewUser(
            name=new_user.name,
            password=hash_password(new_user.password))

        result = BasicCRUD(db=self.session, model_name="UserDb")
        print(type(new))
        return await result.create(new)
        # prikol = UserDb.from_orm(new)
        # self.session.add(prikol)
        # self.session.commit()
        # self.session.refresh(prikol)
        # return prikol.name

