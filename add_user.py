from pypinyin import lazy_pinyin
from model import User, db, app, Roster
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime

# 通过孩子的名字自动生成家长的用户名
password = "123"
parent = "mother"


def printAll():
    users = User.query.all()
    for user in users:
        print(user.name)


def addUser(roster):
    hashed_password = generate_password_hash(password, method='sha256')
    now_time = datetime.datetime.now()
    # 生成拼音用户名
    sentence = lazy_pinyin(roster.name)
    username = ''.join(sentence)
    new_user = User(
        public_id=str(uuid.uuid4()),
        name=username,
        password=hashed_password,
        fullname="",
        parent=parent,
        roster_id=roster.id,
        isadmin=False,
        create_date=now_time,
    )

    db.session.add(new_user)


def createUser():
    rosters = Roster.query.all()
    for roster in rosters:
        addUser(roster)
    db.session.commit()


if __name__ == '__main__':
    # createUser()
    printAll()