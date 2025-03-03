from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from typing import List
from sqlalchemy.orm import session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.showBlog])
def all(db: session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED, )
def create(request: schemas.Blog, db : session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.create(request, db)
    
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.delete(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db) 


@router.get('/{id}', status_code=200, response_model=schemas.showBlog)
def show(id:int, db: session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blog.show(id, db)


