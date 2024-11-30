from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from db.models import DbComment
from routers.schemas import CommentBase
import datetime

def create(db: Session, request: CommentBase):
    new_comment = DbComment(
        text = request.text, 
        username = request.username,
        post_id = request.post_id,
        timestamp = datetime.datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment) 
    return new_comment

def get_all(db: Session, post_id: int):
    post = db.query(DbComment).filter(DbComment.post_id == post_id).all()
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {post_id} not found')
    return post