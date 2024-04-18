from db.engine import Session
from entity.user_entity import UserEntity


class UserMapper:
    def __init__(self):
        pass
    
    def insert(self, user: UserEntity):
        session = Session()
        session.add(user)
        session.commit()
        session.close()
        
    def search_by_username(self, username: str):
        session = Session()
        user = session.query(UserEntity).filter(UserEntity.username == username).first()
        session.close()
        return user
    
    def insert_all(self, users: list):
        session = Session()
        session.add_all(users)
        session.commit()
        session.close()
    
    def search_all(self)->list:
        session = Session()
        users = session.query(UserEntity).filter(UserEntity.face_img != None).all()
        session.close()
        return users
    
userMapper = UserMapper()