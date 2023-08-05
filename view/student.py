from flask import Flask, Blueprint, request, make_response,jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
import datetime
import bcrypt
import jwt
from control.teacher_mgmt import Teacher
from model.mongodb import conn_mongodb
from control.student_mgmt import Student
from view.login import check_access_token

student = Blueprint('students',__name__)#blueprint 객체 생성

mongo_db = conn_mongodb()

@student.route('/', methods = ['POST'])
def student_crud():
    new_user = request.get_json()
    
    access_token = request.headers.get('Authorization')
    print(access_token)
    check_access = check_access_token(access_token)

    if not check_access:
        return jsonify({"code":"400"})
        
    exist_id = mongo_db.student.find_one({'id':new_user['id']})
    exist_s_n = mongo_db.student.find_one({'s_n':new_user['s_n']})
    
    # print(mongo_db.student.find_one({'_id':exist_id}))
    # print(exist_s_n)
    
    if exist_id or exist_s_n:
        return jsonify({"code":"400"})
    else:
        #입력받은 비밀번호 암호화하여 db저장
        new_user['pw'] = bcrypt.hashpw(new_user['pw'].encode('UTF-8'),bcrypt.gensalt())
        
        #id,hashed_pw,account,s_n,full_name,phone_num,father_phone_num,mother_phone_num,guardians_phone_num
        Student.add_student(new_user['id'],new_user['pw'],new_user['account'],new_user['s_n'],new_user['full_name'],
                            new_user['phone_num'],new_user['father_phone_num'],new_user['mother_phone_num'],new_user['guardians_phone_num'])

        return jsonify({'succe':True,'message':'회원가입 성공!'})
    
    
