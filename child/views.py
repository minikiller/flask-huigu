#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request, jsonify, make_response
 
from child import child_api
from user.views import token_required


@ child_api.route('/', methods=['GET'])
@ token_required
def get_all_users(current_user):

    pass






