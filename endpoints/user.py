from datetime import timedelta
import imp
from typing import List

from fastapi import APIRouter, Depends, Security
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from db.user import UserDb
from security.user import ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user, create_access_token, oauth2_scheme, auth_user
from schemas.user import NewUser, UserNameId, NameUser
from .depends import get_session
from repository.user import UserRepository

router = APIRouter()

@router.get("/get_user")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {'token': token}


@router.post('/token')
async def access_token(user_form: OAuth2PasswordRequestForm = Depends(),
                       session: Session = Depends(get_session)):
    user = auth_user(user_form.username, user_form.password, session)
    access_expire_token = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name, "scopes": user_form.scopes}, 
        expires_delta=access_expire_token
    )
    return {"access_token": access_token, "type_token": "bearer"} 


@router.post('/create_user', response_model=NameUser)
async def create_user(new_user: NewUser,
                      session: Session = Depends(get_session)):
    crud_user = UserRepository(session)
    return await crud_user.create_user(new_user=new_user)


@router.get('/get_all_users', response_model=List[UserNameId])
async def get_all_users(session: Session = Depends(get_session)):
    return session.query(UserDb).all()


@router.get('/current_user', response_model=NameUser)
async def user(current_user: NameUser = Security(get_current_user, scopes=["current"])):
    return current_user
