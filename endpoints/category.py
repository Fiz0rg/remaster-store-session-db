from typing import List

import imp
from fastapi import APIRouter, Depends, Query, Security
from sqlmodel import Session, select

from security.user import get_current_user
from . import depends

from schemas.user import NameUser
from schemas.category import CategoryCreate, CategoryName
from db.category import Category

model_name = "Category"

router = APIRouter()


@router.get('/get_all_categories', response_model=List[CategoryCreate])
async def get_all_categories(offset: int = 0,
                             limit: int = Query(default=100, lte=100),
                             session: Session = Depends(depends.get_session)):
    fetch = session.exec(select(Category).offset(offset).limit(limit)).all()
    return fetch


@router.post('/create_category', response_model=CategoryCreate)
async def create_category(name: CategoryName, 
                          session: Session = Depends(depends.get_session),
                          permissions: NameUser = Security(get_current_user, scopes=["admin"])):
    crud_class = depends.BasicCRUD(db=session, model_name=model_name)
    return await crud_class.create(name)


@router.delete('/delete')
async def delete_category(category_name: str,
                          session: Session = Depends(depends.get_session),
                          permissions: NameUser = Security(get_current_user, scopes=["admin"])):
    model_name = "Category"
    crud_class = depends.BasicCRUD(session, model_name)
    return await crud_class.delete(category_name)