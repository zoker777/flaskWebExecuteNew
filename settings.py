import os
from myapp.log.log import logger

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # @staticmethod
    # def init_app(app):
    #     pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.db')
    # flask加载的配置变量只能是大写，否则会报错'KeyError'
    FLASKR_IP = '0.0.0.0'
    FLASKR_PORT = 60805
    # flaskr_ip = '0.0.0.0';flaskr_port = 60805 #不能小写
    JOBS = [
            # {  # 第一个任务
            #     'id': 'job1',
            #     'func': '__main__:job_1',
            #     'args': (1, 2),
            #     'trigger': 'cron', # cron表示定时任务
            #     'hour': 19,
            #     'minute': 27
            # },
            {  # 第二个任务，每隔5S执行一次
                'id': 'job2',
                'func': 'myapp.server.schedule:method_test',  # 方法名
                'args': (1, 2),  # 入参
                'trigger': 'interval',  # interval表示循环任务
                'seconds': 60,
            }
    ]

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.db')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
