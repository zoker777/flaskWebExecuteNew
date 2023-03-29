from flask import Flask, render_template, current_app
from myapp import app_user,app_client
from settings import config
import logging
from flask_apscheduler import APScheduler


app = Flask(__name__)
app.config.from_object(config['default'])
scheduler = APScheduler()
scheduler.init_app(app=app)
scheduler.start()

app.register_blueprint(app_user,url_prefix='/user')
app.register_blueprint(app_client,url_prefix='/client')


@app.route('/')
def index():
    # request、session、g是请求上下文，根据不同的请求有不同的值、current_app是应用上下文，根据不同的应用有不同的值<一般就一个本应用>
    print(app.config['FLASKR_IP'])  #法一
    print(str(current_app.config['FLASKR_PORT']))   #法二：建议使用current_app，更加方便
    return render_template("index.html")

@app.route('/logger_warning')
def logger_warning():
    logging.warning('有人访问了测试logger的接口logger_warning')
    return '您访问了测试接口logger_warning'

#用于测试logger的接口，异常捕获+logger输出日志
@app.route('/logger_error')
def logger_error():
    try:
        no_thing = []
        i = no_thing[0]  # 这里会报错，因为列表根本是空的
        return 'Hello!'
    except Exception as e:
        # print(e)
        logging.error('%s', e)
        return str(e)


if __name__ == '__main__':
    # 启动flask程序
    print(app.url_map)
    with app.app_context(): #引用flask程序app的上下文
        flaskr_ip = current_app.config['FLASKR_IP']
        flaskr_port = current_app.config['FLASKR_PORT']
    app.run(port=flaskr_port, host=flaskr_ip, debug=True)
