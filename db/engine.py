# 初始化数据库连接
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf.service_args import service_config

class Engine:
    def __init__(self):
        driver = service_config["MySQL"]["driver"]
        host = service_config["MySQL"]["host"]
        port = service_config["MySQL"]["port"]
        user = service_config["MySQL"]["user"]
        password = service_config["MySQL"]["password"]
        database = service_config["MySQL"]["database"]

        # 初始化数据库连接，修改为你的数据库用户名和密码
        self.engine = create_engine('{}://{}:{}@{}:{}/{}'.format(driver, user, password, host, port, database))
    
        
    def getEngine(self):
        return self.engine


engine = Engine()

Session = sessionmaker(bind=engine.engine)