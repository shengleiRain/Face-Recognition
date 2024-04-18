# 1 Face-Recognition
该项目主要是提供了检测一张图片中是否存在人脸，以及简单的1:N人脸识别比对的功能。
其中，
- 人脸检测（Face Detection）采用[YuNet](https://github.com/opencv/opencv_zoo/blob/main/models/face_detection_yunet)
- 人脸识别 (Face Recognition)采用[SFace](https://github.com/opencv/opencv_zoo/blob/main/models/face_recognition_sface)
- 数据库使用mysql
- api实现使用FastAPI

## 1.1 实现功能
- [x] 人脸检测API
- [x] 人脸识别API 
- [x] 与[face-vue](https://github.com/shengleiRain/face-vue)可以配合使用



## 1.2 环境安装
```
pip install -r requirements.txt
```
## 1.3 运行web分析服务
```
python service_run.py
```

## 1.4 运行gradio服务
暂时不可用！！！
```
python service_gradio.py
```

# 2 开发指南
## 2.1 文件树
```
--| conf 配置文件目录，用于存放可修改的配置文件与项目级别的配置文件
--|--| config.yml 部署时可修改的参数文件
--|--| global_variable.yml 全局变量
--|--| ... 
--| core 核心模块组，用于存放各个分析模块
--|--| __init__.py 显式导入pipeline需要的模块类
--|--|** **分析模块
--|--|--| **config 分析模块自有参数
--|--|--| **api 分析模块自有路由
--|--|--| ... 分析模块自有其他文件
--| libs 通用依赖组件
--| tests 测试模块
--| utils 工具模块
--| web web服务启动模块
```
## 2.2 开发约束
```
1) pipeline 所用到的子类需要集成自相同的基类，以便pipeline模块自动构建与调用
2) core 模块中，分析类定义时，需要设定默认参数，以便调用方可以更简洁的调用
3) core 模块中，自有参数和路由放在该模块文件夹中，以便实现插件式增模块
4) core 模块中，如果逻辑允许，继承base模块中的分析类和参数类，以便实现插件式增模块
5) core 模块中，如果模块需要构建接口，请在模块中构建**api路由文件，以自动注册路由
6) core 模块中，如果存在**api路由文件，需要自动注册相关路由的，设定router = APIRouter(...)，路由注册函数会搜寻该变量名
```


