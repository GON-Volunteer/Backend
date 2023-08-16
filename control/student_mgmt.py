from model.mongodb import conn_mongodb
from flask_login import UserMixin
from bson import ObjectId
from flask import jsonify


class Student():
    def __init__(self,id,hashed_pw,account,s_n,full_name,phone_num,father_phone_num,mother_phone_num,guardians_phone_num, course_id):
        self.id=id
        self.hashed_pw = hashed_pw
        self.account = account
        self.s_n = s_n
        self.full_name = full_name
        self.phone_num = phone_num
        self.fatehr_phone_num = father_phone_num
        self.mother_phone_num = mother_phone_num
        self.guardians_phone_num = guardians_phone_num
        self.course_id = course_id
    
    def add_student(id,hashed_pw,account,s_n,full_name,phone_num,father_phone_num,mother_phone_num,guardians_phone_num):
        mongo_db = conn_mongodb()
        mongo_db.student.insert_one({
            "id" : id,
            "hashed_pw" : hashed_pw,
            "account":account,
            "s_n" : s_n,
            "full_name" : full_name,
            "phone_num" : phone_num,
            "father_phone_num" : father_phone_num,
            "mother_phone_num" : mother_phone_num,
            "guardians_phone_num" : guardians_phone_num
        })
        
    def delete_student(student_id):
        mongo_db = conn_mongodb()
        delete_condition={"_id":ObjectId(student_id)}
        row = mongo_db.course.find_one({"student_id":ObjectId(student_id)})
        print("delete_student_func")
        print(row)
        if row:
            print("find student_id in course")
            target = {"student_id":ObjectId(student_id)}
            update_data = {'$set':{"student_id":None}}
            mongo_db.course.update_one(target,update_data)
        
        mongo_db.student.delete_one(delete_condition)
    
    
    def edit_student(target,new_data):
        mongo_db = conn_mongodb()
        print("enter edit_student")
        result = mongo_db.student.update_one(target,new_data)
        print(result.modified_count) 
        return result
    
    def check_is_unique(input_id,input_sn):
        mongo_db = conn_mongodb()
        exist_id = mongo_db.student.find_one({'id':input_id})
        exist_s_n = mongo_db.student.find_one({'s_n':input_sn})
        print(exist_id)
        print(exist_s_n)
        
        if exist_id or exist_s_n:
            return False
        else:
            return True
        
    def find_by_student_id(student_id):
        mongo_db = conn_mongodb()
        row = mongo_db.student.find_one({'_id':student_id})
        return row
        