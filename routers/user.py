from fastapi import APIRouter, Depends
from db.database import get_db
from routers.schemas import UserBase, UserDisplay
from db import db_user
from sqlalchemy.orm.session import Session

router = APIRouter(
    prefix='/user',
    tags= ['user']
)

@router.post('', response_model= UserDisplay)
def create_user(request: UserBase, db: Session =  Depends(get_db)):
    return db_user.create_user(db, request)