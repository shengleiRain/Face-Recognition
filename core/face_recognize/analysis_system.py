from libs.base.image_analysis import BaseImageAnalysis
from core.face_recognize.config import face_recognize_args
from core.models.face_detection_yunet.yunet import YuNet
from core.models.face_recognition_sface.sface import SFace


class FaceRecognize(BaseImageAnalysis):
    def __init__(self, module_args=face_recognize_args):
        super().__init__(module_args)
        self.face_det_module, self.face_rec_module = self.init_analysis_module()

    @staticmethod
    def init_analysis_module():
        face_det_module = YuNet(modelPath=face_recognize_args.face_detect_model, confThreshold=0.9, nmsThreshold=0.3, topK=5000)
        face_rec_module = SFace(modelPath=face_recognize_args.face_recognize_model)
        return face_det_module, face_rec_module

    def analysis(self, image):
        img1 = image[0]
        img2 = image[1]
        return self.recognize(img1, img2)
    
    def recognize(self, img1, img2):
        detector = self.face_det_module
        recognizer = self.face_rec_module
        
        # Detect faces
        detector.setInputSize([img1.shape[1], img1.shape[0]])
        faces1 = detector.infer(img1)
        if(faces1.shape[0] == 0):
            return False
        detector.setInputSize([img2.shape[1], img2.shape[0]])
        faces2 = detector.infer(img2)
        if(faces2.shape[0] == 0):
            return False
        
        # Match
        result = recognizer.match(img1, faces1[0][:-1], img2, faces2[0][:-1])
        # return {'score': result[0], 'match': result[1] == 1}
        return result[1] == 1    
    

        

