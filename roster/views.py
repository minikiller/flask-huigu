#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request, jsonify, make_response

from roster import roster_api
from user.views import token_required
from model import Roster
import datetime


@ roster_api.route('/', methods=['GET'])
# @ token_required
def get_all_users():
    rosters = Roster.query.all()

    output = []

    for roster in rosters:
        roster_data = {}
        setRosterData(roster_data, roster)
        output.append(roster_data)

    return jsonify(output)


def setRosterData(roster_data, roster):
    roster_data['id'] = roster.id
    roster_data['name'] = roster.name
    roster_data['code'] = roster.code
    roster_data['number'] = roster.number
    roster_data['sex'] = roster.sex

# 用于vue-select选择框进行学生的选择查询


@roster_api.route('/data', methods=['GET'])
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    output = []
    roster = request.args.get('roster')
    roster = roster.replace('%', '\\').encode().decode('unicode-escape')

    if roster == "":
        return jsonify(output)
    else:
        rosters = Roster.query.filter(
            Roster.name.like("%{}%".format(roster))).all()

    for roster in rosters:
        roster_data = {}
        setRosterData(roster_data, roster)
        output.append(roster_data)

    return jsonify(output)


@ roster_api.route('/', methods=['POST'])
def create_roster():
    # now_time = datetime.datetime.now()
    data = request.get_json()
    roster = Roster(
        name=data['name'],
        fullname=data['code'],
        parent=data['number'],
        roster_id=data['sex'],
    )

    db.session.add(roster)
    db.session.commit()

    return jsonify({'message': '新增成功!'})


@ roster_api.route('/<roster_id>', methods=['PUT'])
@ token_required
def promote_user(current_user, roster_id):

    roster = Roster.query.filter_by(id=roster_id).first()

    if not roster:
        return jsonify({'message': '学生信息没有找到!'})
    data = request.get_json()
    roster.name = data["name"]
    roster.sex = data["sex"]
    roster.code = data["code"]
    roster.number = data["number"]

    db.session.commit()

    return jsonify({'message': '学生信息，更新成功!'})

@ roster_api.route('/<roster_id>', methods=['GET'])
@ token_required
def get_one_user(current_user, roster_id):

    roster = Roster.query.filter_by(id=roster_id).first()

    if not roster:
        return jsonify({'message': 'No roster found!'})

    roster_data = {}
    setRosterData(roster_data, roster)

    return jsonify({'roster': roster_data})