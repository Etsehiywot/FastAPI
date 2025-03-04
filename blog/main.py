from fastapi import FastAPI
from . import schemas
from . import models
from .hashing import Hash

from .database import engine, get_db
from sqlalchemy.orm import session
from fastapi import Depends
from .routers import blog, user, authentication

app = FastAPI()


models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


    
