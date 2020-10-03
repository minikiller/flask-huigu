#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request, jsonify, make_response
 
from roster import roster_api
from user.views import token_required
from model import Roster


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

def setRosterData(roster_data,roster):
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
        setSelectUserData(roster_data, roster)
        output.append(roster_data)

    return jsonify(output)





