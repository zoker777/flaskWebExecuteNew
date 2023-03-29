import subprocess
from myapp import app_client

@app_client.route('/send_tc')
def send_tc():
    # 从request中拿到调度参数字典，并用json.dump存到task_record目录下的文件中
    record_filename = 'record_taskid_date.txt'
    task_path = f'./task_record/{record_filename}'
    # 父进程和子进程中需要注意几点：PYTHONPATH和工作目录
    # 想改变子进程的PYTHONPATH和工作目录。
    # PYTHONPATH：只能在子进程中改变，添加sys.path、工作目录：可以在父进程中改变，在下面字符串前面加上cd **即可，如cd ** && python3 **
    child = subprocess.Popen(f'python3 ./myapp/client/execute_daily.py {task_path}',shell=True,
                             stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    # out,err = child.communicate()
    # out = out.decode()
    # err = err.decode()
    # print(str(out), str(err), sep='\n')
    # # 如果子进程执行的python脚本，那么可以用communicate给父进程console展示 or 用logger打印输出到文件
    # # 如果子进程执行的shell脚本，那么可以用communicate给父进程console展示 or echo '**' > file打印输出到文件
    return 'hello send_tc'


if __name__ == '__main__':
    pass
