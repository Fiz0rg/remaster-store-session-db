from sqlmodel import Session

from schemas import user
from security.user import hash_password
from db.user import UserDb


class UserRepository:
    def __init__(self, db: Session):
        self.session = db


    async def create_user(self, new_user):
        new = user.NewUser(
            name=new_user.name,
            password=hash_password(new_user.password))
        print('123')
        prikol = UserDb.from_orm(new)
        add = self.session.add(prikol)
        self.session.commit()
        self.session.refresh(prikol)
        return prikol.name

