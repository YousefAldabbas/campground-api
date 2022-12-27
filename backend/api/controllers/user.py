from security import get_password_hash
from sqlalchemy.orm import Session
from models.user import User




def create(req, db: Session):
    new_user = User(email = req.email, username = req.username,hashed_password = get_password_hash(req.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




