import conf.global_variable as global_variable
from fastapi import Form
from pydantic import BaseModel
from fastapi import APIRouter, Query
from typing import List
from utils.log_init import logger
from core.analysis_pipeline.analysis_pipeline_args import task_candidate_list
from utils.web_exception import openapi_response
from utils.web_utils import BaseResponseItem
from typing import Union
from utils.image_utils import base64_cv2
import cv2

# 构建本地文件请求体参数
class PipelineItem(BaseModel):
    image: str
    tasks: List[str] = Query(
        description="Candidate is a subset of:" + str(task_candidate_list))
    tasks_args: dict = {}


# 返回体信息
class ResponseItem(BaseResponseItem):
    data: dict


description = """
data: dict, 其元素为
- **task_name**: **task_res**
- **task_res** 未成功分析时，默认为None
"""

# 构建路由
router = APIRouter(prefix='/face', tags=['addition'])

@router.post("/detect",
             responses=openapi_response,
             response_model=ResponseItem,
             response_description=description)
def face_detect(image: str=Form(...)):
    logger.info("pipeline接收到multipart/form-data请求 tasks:{}".format("face_detect"))
    image_data = base64_cv2(image)
    # image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
    return global_variable.image_analysis_pipeline.analysis_image(image_data,
                                                                  ["face_detect"])


@router.post("/compare",
             responses=openapi_response,
             response_model=ResponseItem,
             response_description=description)
def face_compare(img1: str=Form(...), img2: str=Form(...)):
    logger.info("pipeline接收到multipart/form-data请求  tasks:{}".format("face_recognize"))
    image_data = base64_cv2(img1)
    # image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
    compatedImage_data = base64_cv2(img2)
    # compatedImage_data = cv2.cvtColor(compatedImage_data, cv2.COLOR_BGR2GRAY)
    return global_variable.image_analysis_pipeline.analysis_image([image_data, compatedImage_data],
                                                                  ["face_recognize"])

