from typing import List

import imp
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select
from . import depends

from schemas.category import CategoryCreate
from db.category import Category


router = APIRouter()


@router.get('/get_all_categories', response_model=List[CategoryCreate])
async def get_all_categories(offset: int = 0,
                             limit: int = Query(default=100, lte=100),
                             session: Session = Depends(depends.get_session)):
    fetch = session.exec(select(Category).offset(offset).limit(limit)).all()
    return fetch


@router.post('/create_category', response_model=CategoryCreate)
async def create_category(cat: CategoryCreate, session: Session = Depends(depends.get_session)):
    model_name = "Category"
    crud_class = depends.BasicCRUD(session, model_name, cat)
    return await crud_class.create()


@router.delete('/delete', response_model=CategoryCreate)
async def delete_category(category_name: str,
                          session: Session = Depends(depends.get_session)):
    model_name = "Category"
    crud_class = depends.BasicCRUD(session, model_name, category_name)
    return await crud_class.delete(category_name)