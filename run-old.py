'''
    logging
    os sys time datetime shutil
    string random hashlib math getpass
    re
    subprocess threading
    django flask restfulapi requests
    pyyaml/yaml json

    ##暂时不需要multiprocessing
    ##暂时不需要pymysql smtplib paramiko openpyxl
    ##暂时不需要queue socket
    ##暂时不需要pytest<接口自动化> selenium<web自动化>
'''
"""
    参考网站：https://www.jianshu.com/p/6452596c4edb
    pycharm中为当前虚拟环境安装第三方模块：使用.\venv\Scripts\pip.exe install *
    html模板：如果是run.py渲染html模板，项目根目录下创建templates目录，如果是包myapp中的代码渲染html模板，那么myapp目录下创建templates目录
        即render_template代码所在的当前目录下必须存在templates目录
    flask的url重定向，如url为/aa /aa/区别：url为/aa，那么只能以/aa访问，/aa/访问报错404；
        url为/aa/，那么/aa或/aa/都能访问。一般建议用/aa的形式，保证url唯一性。
    代码中对列表or字典进行操作时，为了减少代码报错的概率。如删del改为pop、查dict['k']改为dict.get('c','None')
    flask request中请求参数，请求头，请求体中相应的处理。请求参数
    
    python在导入模块文件内容时<如b文件导入a文件中的一个函数时>，会先执行下a文件中的所有代码行，然后再导入函数
        ##<如b文件去一个包test中a文件导入函数时，会先执行下包test下init文件所有代码行，然后执行下a文件的所有代码行，最后再导入函数>
        ##只要是去一个包中导入内容时，都会先执行init文件的所有代码行，然后再导入内容<小技巧：可以在init文件写创建对象的代码，直接from 包 import 对象即可>
"""

import os
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    print(os.getcwd())
    # test()
    print('args:',request.args,'form',request.form,'data',request.data,'json',request.json,sep='\n')

    return {
        'msg': 'success',
        'data': 'welcome to use flask.'
    }
@app.route('/user/<uid>')
def user_info(uid):
    return {
        "msg": "success",
        "data": {
            "id": uid,
            "username": 'zhangsan',
            "age": 18
        }
    }
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

#直接访问/login是用get方式访问，body中的title变量为Default，访问页面为login.html
#带数据的post请求/login，才会走下面的if判断，判断表单中的key user是否为admin，用postman来模拟post表单请求
@app.route('/login1', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form.get('user') == 'admin':
            session['user'] = request.form['user']
                # print(session) print(type(session))
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    #下面走的get请求
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        # params=[]
        params = {}
        title = request.args.get('title', 'Default') # print(title)
        sex = request.args.get('sex', 'man')
        # params.extend([title,sex])
        params.update({'title':title,'sex':sex})
        # 下面分别展示了向html模板文件传递变量，列表，字典来渲染
        # return render_template('login.html', title=title, sex=sex)
        # return render_template('login.html', params=params)
        return render_template('login.html', params=params)


@app.route('/logout')
def logout():
    session.pop('user', None)
    #url_for:查找函数login所对应的url
    return redirect(url_for('login'))

if __name__ == '__main__':
    # app.debug = True
    # temp_path=os.getcwd()+r'\myapp\templates'
    app.secret_key = '123456'
    app.run(host='0.0.0.0',port=5001,debug=True)


