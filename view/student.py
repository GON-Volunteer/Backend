from flask import Flask, Blueprint, request, make_response,jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
import datetime
import bcrypt
import jwt
from control.teacher_mgmt import Teacher
from model.mongodb import conn_mongodb
from control.student_mgmt import Student
from bson import ObjectId
from bson.json_util import dumps
import json

student = Blueprint('students',__name__)#blueprint 객체 생성

mongo_db = conn_mongodb()

@student.route('/', methods = ['POST','GET'])
def student_add():
    if request.method == 'POST':
        new_user = request.get_json()
        
        if not Student.check_is_unique(new_user['id'],new_user['s_n']):
            return jsonify({"code":"400", "message" : "아이디 혹은 s_n가 중복입니다."})
        else:
            #입력받은 비밀번호 암호화하여 db저장
            new_user['pw'] = bcrypt.hashpw(new_user['pw'].encode('UTF-8'),bcrypt.gensalt())
            
            #id,hashed_pw,account,s_n,full_name,phone_num,father_phone_num,mother_phone_num,guardians_phone_num
            Student.add_student(new_user['id'],new_user['pw'],new_user['account'],new_user['s_n'],new_user['full_name'],
                                new_user['phone_num'],new_user['father_phone_num'],new_user['mother_phone_num'],new_user['guardians_phone_num'])

            return jsonify({'code':"200",'message':'회원가입 성공!'})
    elif request.method == 'GET':
        page =int(request.args.get('page'))
        size = int(request.args.get('size'))
        
        result = mongo_db.student.find().sort("s_n",1).skip(size*(page-1)).limit(size)
        
        serialized_data = dumps(result, default=str)#dumps() : 딕셔너리 자료형을 JSON 문자열로 만든다.
        json_data = json.loads(serialized_data)#loads() : JSON 문자열을 딕셔너리로 변환
        
        return json_data
        

@student.route('/<student_id>', methods = ['DELETE','PATCH'])
def student_crud(student_id):
    
    if request.method == "DELETE":
        Student.delete_student(student_id)
        return jsonify({"code":"200","message":"삭제가 완료되었습니다."})
    
    if request.method == "PATCH":
        input_data = request.json
        
        if not Student.check_is_unique(input_data['id'],input_data['s_n']):
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
            print("hello")
            result = Student.edit_student(target,new_data)
        
            if result.modified_count == 0:
                return jsonify({"code":"400","message":"수정할 학생을 찾을 수 없습니다."})
            else:
                return jsonify({'code':"200",'message':'학생정보 수정성공!'})
                

    
    
    