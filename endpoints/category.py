from typing import List

import imp
from fastapi import APIRouter, Depends, Query, Security
from sqlmodel import Session, select

from security.user import get_current_user
from .depends import BasicCRUD, get_session

from schemas.user import UserName
from schemas.category import CategoryCreate, CategoryName
from db.category import Category

model_name = "Category"

router = APIRouter()


@router.get('/get_all_categories', response_model=List[CategoryCreate])
async def get_all_categories(offset: int = 0,
                             limit: int = Query(default=100, lte=100),
                             session: Session = Depends(get_session)):
    fetch = session.exec(select(Category).offset(offset).limit(limit)).all()
    return fetch


@router.post('/create_category', response_model=CategoryCreate)
async def create_category(name: CategoryName, 
                          session: Session = Depends(get_session),
                        #   permissions: UserName = Security(get_current_user, scopes=["admin"])
                        ):
    base_class = BasicCRUD(db=session, model_name=model_name)
    return await base_class.create(item_name=name)

@router.delete('/delete')
async def delete_category(category_name: str,
                          session: Session = Depends(get_session),
                        #   permissions: UserName = Security(get_current_user, scopes=["admin"])
                        ):
    model_name = "Category"
    crud_class = BasicCRUD(session, model_name)
    return await crud_class.delete(category_name)