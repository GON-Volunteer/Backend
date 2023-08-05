from flask import Flask, Blueprint, request, make_response,jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
import datetime
import bcrypt
import jwt
from control.teacher_mgmt import Teacher
from model.mongodb import conn_mongodb
from control.student_mgmt import Student
from view.login import check_access_token
from bson import ObjectId

student = Blueprint('students',__name__)#blueprint 객체 생성

mongo_db = conn_mongodb()

@student.route('/', methods = ['POST'])
def student_add():
    new_user = request.get_json()

    access_token = request.headers.get('Authorization')
    print(access_token)
    check_access = check_access_token(access_token)

    if not check_access:
        return jsonify({"code":"400", "message" : "토큰이 유효하지 않거나 만료되었습니다."})
        
    exist_id = mongo_db.student.find_one({'id':new_user['id']})
    exist_s_n = mongo_db.student.find_one({'s_n':new_user['s_n']})
    
    if exist_id or exist_s_n:
        return jsonify({"code":"400", "message" : "아이디 혹은 s_n가 중복입니다."})
    else:
        #입력받은 비밀번호 암호화하여 db저장
        new_user['pw'] = bcrypt.hashpw(new_user['pw'].encode('UTF-8'),bcrypt.gensalt())
        
        #id,hashed_pw,account,s_n,full_name,phone_num,father_phone_num,mother_phone_num,guardians_phone_num
        Student.add_student(new_user['id'],new_user['pw'],new_user['account'],new_user['s_n'],new_user['full_name'],
                            new_user['phone_num'],new_user['father_phone_num'],new_user['mother_phone_num'],new_user['guardians_phone_num'])

        return jsonify({'code':"200",'message':'회원가입 성공!'})

@student.route('/<student_id>', methods = ['DELETE','PATCH'])
def student_crud(student_id):
    
    access_token = request.headers.get('Authorization')
    print(access_token)
    check_access = check_access_token(access_token)

    if not check_access:
        return jsonify({"code":"400", "message" : "토큰이 유효하지 않거나 만료되었습니다."})
    
    if request.method == "DELETE":
        print("delete enter")
        Student.delete_student(student_id)
        return jsonify({"code":"200"})
    
    if request.method == "PATCH":
        input_data = request.json
        
        exist_id = mongo_db.student.find_one({'id':input_data['id']})
        exist_s_n = mongo_db.student.find_one({'s_n':input_data['s_n']})
    
        if exist_id or exist_s_n:
            return jsonify({"code":"400", "message" : "아이디 혹은 s_n가 중복입니다."})
        else:
            input_data['pw'] = bcrypt.hashpw(input_data['pw'].encode('UTF-8'),bcrypt.gensalt())
            target = {"_id":ObjectId(student_id)}
            
            new_data = {"$set":{
                'id': input_data['id'],
                'hashed_pw' : input_data['pw'],
                's_n' : input_data['s_n'],
                'full_name' : input_data['full_name'],
                'phone_num' : input_data['phone_num'],
                'father_phone_num' : input_data['father_phone_num'],
                'mother_phone_num' : input_data['mother_phone_num'],
                'guardians_phone_num' : input_data['guardians_phone_num']
                }}
            print(target)
            mongo_db.student.update_one(target,new_data)
        
            return jsonify({'code':"200",'message':'학생정보 수정성공!'})
        
    
    
    
