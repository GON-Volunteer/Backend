from model.mongodb import conn_mongodb
from flask_login import UserMixin

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
        