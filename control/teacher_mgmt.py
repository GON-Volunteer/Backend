from model.mongodb import conn_mongodb
from flask_login import UserMixin
from pymongo import MongoClient
from bson import ObjectId

mongo_db = conn_mongodb()

class Teacher():
    def __init__(self,id,hashed_pw,account,full_name,phone_num,course_id):
        self.id = id
        self.pw = hashed_pw
        self.account = account
        self.full_name = full_name
        self.phone_num = phone_num
        self.course_id = course_id
        
    def add_teacher(id,hashed_pw,account,full_name,phone_num):
        mongo_db = conn_mongodb()
        mongo_db.teacher.insert_one({
            "id" : id,
            "hashed_pw" : hashed_pw,
            "account":account,
            "full_name" : full_name,
            "phone_num" : phone_num,
            "course_id" : None
        })

    def check_is_unique(input_id):
        mongo_db = conn_mongodb()
        exist_id = mongo_db.teacher.find_one({'id':input_id})
        print(exist_id)
        
        if exist_id:
            return False
        else:
            return True
        
    def delete_teacher(teacher_id):
        mongo_db = conn_mongodb()
        delete_condition={"_id":ObjectId(teacher_id)}
        row = mongo_db.course.find_one({"teacher_id":ObjectId(teacher_id)})
        print("delete_teacher_func")
        print(row)
        if row:
            print("find teacher_id in course")
            target = {"teacher_id":ObjectId(teacher_id)}
            update_data = {'$set':{"teacher_id":None}}
            mongo_db.course.update_one(target,update_data)
        
        mongo_db.teacher.delete_one(delete_condition)
    
    def edit_teacher(target,new_data):
        mongo_dbdb = conn_mongodb()
        print("enter edit_student")
        result = mongo_db.teacher.update_one(target,new_data)
        print(result.modified_count) 
        return result