import conf.global_variable as global_variable
from pydantic import BaseModel
from fastapi import APIRouter, Query, Form
from typing import List
from utils.log_init import logger
from core.analysis_pipeline.analysis_pipeline_args import task_candidate_list
from utils.web_exception import openapi_response
from utils.web_utils import BaseResponseItem
from typing import Union
from utils.image_utils import base64_cv2
import cv2
from service.user_service import userService


# 返回体信息
class ResponseItem(BaseResponseItem):
    data: dict


description = """
data: dict
"""

# 构建路由
router = APIRouter(prefix='/api/face', tags=['addition'])

@router.post("/recognize",
             responses=openapi_response,
             response_model=ResponseItem,
             response_description=description)
def recognize_face(image: str=Form(...)):
    return userService.recognize_face(img_base64=image)

@router.post("/detect",
             responses=openapi_response,
             response_model=ResponseItem,
             response_description=description)
def detect_face(image: str=Form(...)):
    return userService.detect_face(img_base64=image)

@router.post("/add_user",
             responses=openapi_response,
             response_model=ResponseItem,
             response_description=description)
def add_user(image: str=Form(...), username: str=Form(...)):
    return userService.insert_user_by_face_img(username=username, face_img=image)