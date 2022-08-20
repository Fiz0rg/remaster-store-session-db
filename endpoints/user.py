from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from db.user import UserDb
from security.user import oauth2_scheme
from schemas.user import FullUser, NewUser, UserNameId, NameUser
from .depends import get_session
from repository.user import UserRepository

router = APIRouter()

@router.get("/get_user")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {'token': token}



@router.post('/create_user', response_model=NameUser)
async def create_user(new_user: NewUser,
                      session: Session = Depends(get_session)):
    crud_user = UserRepository(session)
    return await crud_user.create_user(new_user=new_user)


@router.get('/get_all_users', response_model=List[UserNameId])
async def get_all_users(session: Session = Depends(get_session)):
    return session.query(UserDb).all()