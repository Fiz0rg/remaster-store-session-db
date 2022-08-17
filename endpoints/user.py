from fastapi import APIRouter, Depends

from security.user import oauth2_scheme

router = APIRouter()

@router.get("/users")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {'token': token}