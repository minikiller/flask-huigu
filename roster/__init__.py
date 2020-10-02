from flask import Blueprint

# 创建 puke 接口的蓝图
roster_api = Blueprint("roster", __name__)

from roster import views
