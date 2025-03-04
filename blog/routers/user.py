from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import session
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: session = Depends(get_db)):
   return user.create(request,db)
    
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id, db: session = Depends(get_db)):
   return user.show(id,db)
