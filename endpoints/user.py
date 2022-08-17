from fastapi import APIRouter, Depends
from sqlmodel import Session

from security.user import oauth2_scheme
from schemas import user
from .depends import get_session
from repository.user import UserRepository

router = APIRouter()

@router.get("/get_user")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {'token': token}



@router.post('/create_user', response_model=str)
async def create_user(new_user: user.NewUser,
                      session: Session = Depends(get_session)):
    crud_user = UserRepository(session)
    return await crud_user.create_user(new_user=new_user)