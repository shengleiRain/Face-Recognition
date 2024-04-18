from libs.base.analysis_args import AnalysisArgs
import os
from conf.service_args import project_root

def init_args():
    args = AnalysisArgs()
    args.face_detect_model = os.path.join(project_root, "core/models/face_detection_yunet/face_detection_yunet_2023mar.onnx")
    args.face_recognize_model = os.path.join(project_root, "core/models/face_recognition_sface/face_recognition_sface_2021dec.onnx")
    return args


# 初始化参数,使用需要用import导入，防止不必要的二次复制 例如 import **.config.**_args as **_args
face_recognize_args = init_args()


if __name__ == "__main__":
    print(face_recognize_args)
