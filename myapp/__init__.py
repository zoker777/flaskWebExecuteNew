from flask import Blueprint


app_client=Blueprint('client',__name__)
app_user=Blueprint('user',__name__)
    # 实例化一个蓝图对象app_user，它的名字叫user。如app.url_map中路由/user/login对应的函数字段为user.loginpage
    ##这里user.loginpage，user即为上面的蓝图名字，loginpage为路由所对应的具体的逻辑函数名。
    ##如果不是蓝图路由，是普通路由，那么路由直接对应函数名

from myapp.user.views import app_user
from myapp.client.execute import app_client
