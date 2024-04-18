from libs.base.analysis_args import AnalysisArgs
import os
from conf.service_args import project_root



def init_args():
    args = AnalysisArgs()
    args.model = os.path.join(project_root, "core/models/face_detection_yunet/face_detection_yunet_2023mar.onnx")
    return args


# 初始化参数,使用需要用import导入，防止不必要的二次复制 例如 import **.config.**_args as **_args
face_detect_args = init_args()


if __name__ == "__main__":
    print(face_detect_args)
