from flask import Flask, Blueprint, request, make_response,jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
import datetime
import bcrypt
import jwt
from control.teacher_mgmt import Teacher
from model.mongodb import conn_mongodb

user_sign_up = Blueprint('signup',__name__)#blueprint 객체 생성

mongo_db = conn_mongodb()

@user_sign_up.route('/teacher', methods = ['POST'])
def sign_up_teacher():
    new_user = request.get_json()
    #print(new_user)
    new_user['pw'] = bcrypt.hashpw(new_user['pw'].encode('UTF-8'),bcrypt.gensalt())
    #print(new_user['pw'])
    Teacher.add_teacher(new_user['id'],new_user['pw'],new_user['account'],new_user['full_name'],new_user['phone_num'],new_user['teacher_course'])

    return jsonify({'succe':True,'message':'회원가입 성공!'})















    # new_user = request.json
    # new_user['pw'] = bcrypt.hashpw(new_user['pw'].encode('UTF-8'),bcrypt.gensalt())
    # print(new_user['pw'])
    
    # #id,pw,account,full_name,phone_num,teacher_course
    # Teacher.add_teacher(new_user['id'],new_user['pw'],new_user['account'],new_user['full_name'],new_user['phone_num'],new_user['teacher_course'])

# s1 = "hello"
# print(s1.encode('UTF-8'))
# s1_encode = bcrypt.hashpw(s1.encode('UTF-8'),bcrypt.gensalt())
# print(s1_encode)
# print(s1.encode('UTF-8'))



