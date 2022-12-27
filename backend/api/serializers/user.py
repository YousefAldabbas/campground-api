from http.client import NOT_FOUND
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from security import verify_password

def loginSerializer(req, db: Session = Depends()):
    user = db.query(User).filter(User.username == req.username).first()
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    
    if not verify_password(req.password,user.hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect password")
    
    return user