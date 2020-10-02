from flask import Blueprint

# 创建 puke 接口的蓝图
child_api = Blueprint("child", __name__)

from child import views
