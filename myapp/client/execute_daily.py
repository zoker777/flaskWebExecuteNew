import json
import os, sys
import logging
import subprocess
from multiprocessing import Pool

# 添加根目录到模块路径sys.path
module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = os.path.dirname(module_path)
sys.path.extend([root_path,module_path])

# import和直接运行py文件区别：
# import方式：PYTHONPATH路径和工作目录为 run.py所在目录，即flaskWebDemo/
# 直接运行方式：PYTHONPATH路径为 当前文件所在目录，即flaskWebDemo/myapp/client/；工作目录为 run.py所在目录，即flaskWebDemo/
# print(sys.path);print(os.getcwd())

# 此函数用于调度一个业务shell脚本，通过不同的参数执行不同的内容
def execute_sh(execute_script,execute_param):
    child = subprocess.Popen(f'sh ./myapp/business/{execute_script} {execute_param}', shell=True,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = child.communicate()
    out = out.decode()
    err = err.decode()
    try:
        logging.info(out+err)
    except Exception as e:  # 如果实在不知道是什么错误类型，或者想偷懒也可以捕获所有的错误类型，“Exception”已经包含了大部分的错误类型
        logging.error("except:"+str(e))

# 此函数用于调度执行业务命令，可以是任何命令，如python等任何可在linux上执行的命令
def execute_command(execute_script):
    child = subprocess.Popen(f'{execute_script}', shell=True,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = child.communicate()
    out = out.decode()
    err = err.decode()
    logging.info(out + err)

def assign_task(params_dict):
    pool = Pool(4) # 创建4个进程
    for param in params_dict:
        execute_script = param['execute_script']
        execute_param = param['execute_param']
        if execute_param == 'command':
            logging.info('执行参数:'+execute_param)
            pool.apply_async(execute_command, (execute_script,))
        else:
            logging.info('执行参数:'+execute_param)
            pool.apply_async(execute_sh,(execute_script,execute_param))
    pool.close() # 关闭进程池，表示不能在往进程池中添加进程
    pool.join() # 等待进程池中的所有进程执行完毕，必须在close()之后调用


if __name__ == '__main__':
    task_path = sys.argv[1]
    with open(task_path, 'r') as f:
        params_str = f.read()
    params_dict = json.loads(params_str)['execute_dict']
    assign_task(params_dict)
