import imp

from typing import List
from fastapi import APIRouter, Depends, Security
from sqlmodel import Session

from db.goods import GoodsDb
from schemas.user import NameUser
from security.user import get_current_user

from .depends import get_session, BasicCRUD
from schemas import goods

router = APIRouter()

model_name = 'GoodsDb'


@router.post('/create', response_model=goods.FullGoodsResponse)
async def create_goods(item: goods.GoodsCreate,
                       session: Session = Depends(get_session),
                       permissions: NameUser = Security(get_current_user, scopes=["admin"])):
    base_class = BasicCRUD(db=session, model_name=model_name)
    return await base_class.create(item)


@router.get('/get_one', response_model=goods.FullGoodsResponse)
async def get_one_goods(name: str,
                        session: Session = Depends(get_session)):
    return session.query(GoodsDb).filter(GoodsDb.name == name).first()


@router.get('/get_all', response_model=List[goods.FullGoodsResponse])
async def get_all_goods(session: Session = Depends(get_session)):
    return session.query(GoodsDb).all()