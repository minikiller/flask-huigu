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





