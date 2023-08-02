from model.mongodb import conn_mongodb
from flask_login import UserMixin
from pymongo import MongoClient

mongo_db = conn_mongodb()

class Teacher():
    def __init__(self,id,hashed_pw,account,full_name,phone_num,teacher_course):
        self.id = id
        self.pw = hashed_pw
        self.account = account
        self.full_name = full_name
        self.phone_num = phone_num
        self.teacher_course = teacher_course
        
    def add_teacher(id,hashed_pw,account,full_name,phone_num,teacher_course):
        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            "id" : id,
            "hashed_pw" : hashed_pw,
            "full_name" : full_name,
            "phone_num" : phone_num,
            "teacher_course" : teacher_course
        })
        