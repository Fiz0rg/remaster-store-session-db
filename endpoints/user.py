from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, Security
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from db.user import UserDb, GoodsDb
from schemas.goods import FullGoodsResponse
from security.user import ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user, create_access_token, oauth2_scheme, auth_user
from schemas.user import IdUser, NewUser, UserBasket, UserName
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


@router.post('/create_user', response_model=IdUser)
async def create_user(new_user: NewUser,
                session: Session = Depends(get_session)):
    crud_user = UserRepository(session)
    return await crud_user.create_user(new_user=new_user)


@router.get('/get_all_users', response_model=List[UserName])
def get_all_users(session: Session = Depends(get_session)):
    return session.query(UserDb).all()


@router.get('/current_user', response_model=UserBasket)
def user(current_user: UserBasket = Security(get_current_user, scopes=["current"])):
    """
    Получение текущего пользователя по Security.
    Может сделать это только он сам.
    """

    return current_user


@router.get('/test', response_model=UserBasket)
def test(user_id: int,
         session: Session = Depends(get_session)):
    """
    Тестовая ф-ция для получения юзера просто по его id.
    Тут пример того, что обращение к UserDb.goods выдаёт ошибку, что такого атрибута не найдено в модели.
    """

    get_user = session.get(UserDb, user_id)
    print("Goods: " , get_user.goods)
    return get_user



# @router.patch('/add_goods_in_basket', response_model=UserBasket)
# def update_basket(*, goods_id: int,
#                      session: Session = Depends(get_session),
#                      current_user: UserName = Security(get_current_user, scopes=["current"])):
#     user = current_user
#     goods = session.query(GoodsDb).get(goods_id)
#     goods_data = FullGoodsResponse(**goods.dict())
#     test = goods.dict()
#     goods_dataA = goods_data.dict(exclude_unset=True)
#     for key, value in goods_dataA.items():
#         setattr(user, key, value)
#     session.add(user)
#     session.commit()
#     session.refresh(user)
#     return user
    