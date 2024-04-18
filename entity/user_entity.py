from sqlalchemy import Column, String, Integer,Text
from entity.base import Base
from db.engine import engine


class UserEntity(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    face_img = Column(Text(65536))
    card_id = Column(String(20))
    
    
Base.metadata.create_all(engine.engine)