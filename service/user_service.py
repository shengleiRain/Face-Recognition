from entity.user_entity import UserEntity
from db.user_mapper import userMapper
from core.face_recognize.analysis_system import FaceRecognize
from core.face_detect.analysis_system import FaceDetect

from utils.image_utils import base64_cv2
from utils.web_utils import add_time_info

class UserService:
    def __init__(self):
        self.face_recognizer = FaceRecognize()
        self.face_detector = FaceDetect()
    
    @add_time_info
    def detect_face(self, img_base64):
        image = base64_cv2(img_base64)
        result = self.face_detector.analysis(image)
        return {'result': result}
    
    @add_time_info
    def recognize_face(self, img_base64):
        image = base64_cv2(img_base64)
        
        users = userMapper.search_all()
        for user in users:
            face_image_data = base64_cv2(user.face_img)
            result = self.face_recognizer.recognize(image,face_image_data)
            if result:
                return {'result': {
                    'username': user.username,
                    'id': user.id
                }}
        return {'result': None}  
    
    @add_time_info
    def insert_user_by_face_img(self, username: str, face_img: str):  
        image = base64_cv2(face_img)
        result = self.face_detector.analysis(image)
        if(result == False):
            return {'result': False}
        
        user = userMapper.search_by_username(username)
        if(user == None):
            userEntity = UserEntity()
            userEntity.face_img = face_img
            userEntity.username = username
            userMapper.insert(userEntity)    
            return {'result': True}   
        else:
            user.face_img = face_img
            userMapper.insert(user)
            return {'result': True}
         

    
userService = UserService()