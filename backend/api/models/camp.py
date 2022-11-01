from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..config import Base


class Camp(Base):
    __tablename__ = "camps"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    image = Column(String,)
    description = Column(String(500))
    price = Column(Integer(6))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_id = Column(Integer,ForeignKey('users.id'))
    comments = relationship("Comment", back_populates="comments")

