from libs.base.image_analysis import BaseImageAnalysis
from core.face_detect.config import face_detect_args
from core.models.face_detection_yunet.yunet import YuNet


class FaceDetect(BaseImageAnalysis):
    def __init__(self, module_args=face_detect_args):
        super().__init__(module_args)
        self.face_detect_model = self.init_analysis_module()

    @staticmethod
    def init_analysis_module():
        face_detect_model = YuNet(modelPath=face_detect_args.model)
        return face_detect_model

    def analysis(self, image):
        """
        input: image 
        output: true: detected 1 face, false: not detected or detected more than 1 face
        """
        h, w,_ = image.shape

        # Inference
        self.face_detect_model.setInputSize([w, h])
        results = self.face_detect_model.infer(image)
        
        # Print results
        print('{} faces detected.'.format(results.shape[0]))
        for idx, det in enumerate(results):
            print('{}: {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f} {:.0f}'.format(
                idx, *det[:-1])
            )
            
        return results.shape[0] == 1

