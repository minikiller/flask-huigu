#!/usr/bin/python
# -*- coding: utf-8 -*-
# from flask import Flask, request, jsonify, make_response, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import desc
# import uuid
# from werkzeug.security import generate_password_hash, check_password_hash
# import jwt
# import datetime
# from functools import wraps
from model import app
from child import child_api
from user import user_api


app.register_blueprint(user_api, url_prefix='/users')
app.register_blueprint(child_api, url_prefix='/childs')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
#     app.run(host='0.0.0.0', debug=False,
#             ssl_context=('cert.pem', 'privkey.pem'))
    # db.create_all()
