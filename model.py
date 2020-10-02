from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS


app = Flask(__name__, static_folder='static',)
#  Cross Origin Resource Sharing
CORS(app, expose_headers=["x-suggested-filename"])

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
basedir = os.path.abspath(os.path.dirname(__file__))
# print('base path is {}'.format(basedir))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'huigu.sqlite')

db = SQLAlchemy(app)


# 系统用户
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))         # 登陆用的用户名
    password = db.Column(db.String(20))     # 密码
    mobile = db.Column(db.String(20))       # 手机号码
    email = db.Column(db.String(50))        # 电子邮件地址
    rank = db.Column(db.Integer)            # 级别：-25K ～ 9D
    lefttimes = db.Column(db.Integer)       # 用户使用对局室的剩余时间
    isadmin = db.Column(db.Boolean)         # 系统管理员
    avatar = db.Column(db.String(200))             # 用户头像照片
    create_date = db.Column(db.DateTime)
    win = db.Column(db.Integer)  # 胜利局数
    fail = db.Column(db.Integer)  # 失败局数
    background = db.Column(db.String(50))


class Roster(db.Model):  #花名册
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))  # 名称
    code = db.Column(db.String(8))  # 班号
    number = db.Column(db.String(50))  # 身份证
    sex = db.Column(db.String(2))  # 性别


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=False,
    #         ssl_context=('cert.pem', 'privkey.pem'))
    db.create_all()
