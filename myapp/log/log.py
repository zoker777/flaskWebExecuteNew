import logging
import os
import time

# 此文件在flask app加载settings配置文件时执行并初始化flask的logger，后面需要打印日志的地方直接import logging即可
# 第一步，获取flask的logger(flask默认使用logging的logger)
logger = logging.getLogger()
# logger = app.logger #和上面等价
logger.setLevel(logging.INFO)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件(%Y%m%d%H%M)
day = time.strftime('%Y%m%d', time.localtime(time.time()))
log_path = os.path.dirname(__file__) + f'/flask_{day}.log'
fh = logging.FileHandler(log_path, mode='a',encoding='UTF-8')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
#启动flask默认会有一个console。有个自带的app.logger,一般自建logger，新建fh和ch。子进程的console是单独的，子进程的console只能通过community给父进程console输出。
#父子进程用一个logger，filehandler能看到父子进程的输出，但是consolehandler只能看到父进程的输出，无法看到子进程的console输出(只能通过community给父进程console输出)
#父进程中的logger输出，console和file都能看到。子进程中的logger输出，只有file能看到，console看不到，因为子进程和父进程的console是独立的(只能通过community给父进程console输出)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG) # 不指定级别则默认使用logger.setLevel设置的级别

# 第三步，定义handler的输出格式
formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第四步，将handler添加到logger里面
logger.addHandler(fh)
logger.addHandler(ch)
# flask自带有logger，但是一般新建logger使用，这样导入使用更方便。flask自带logger如：app.logger.addHandler(handler)


if __name__ == '__main__':
    logger.warning('this is warning information!')

    # 下面为RotatingFileHandler定时切割日志
    # import logging
    # import os
    # from logging.handlers import RotatingFileHandler
    #
    # # 设置日志的记录等级
    # logging.basicConfig(level=logging.DEBUG) # 调试debug级
    # project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小<如下为100M>、保存的日志文件个数上限
    # file_log_handler = RotatingFileHandler(f"{project_dir}/myapp/logs/run.log",maxBytes=1024*1024*100,backupCount=7, encoding='utf-8')
    # # 创建日志记录的格式
    # formatter = logging.Formatter(
    #             '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    # # 为刚创建的日志记录器设置日志记录格式
    # file_log_handler.setFormatter(formatter)
    # # 为全局的日志工具对象（flask app使用的）添加日志记录器
    # logging.getLogger().addHandler(file_log_handler)
