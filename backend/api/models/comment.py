from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..config import Base



class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, unique=True, index=True)
    comment = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_id = Column(Integer,back_populates="comments.id")
    camp_id = Column(Integer,back_populates="comments.id")

    # user = relationship("User", back_populates="comments")
    camp = relationship("Camp", back_populates="comments")