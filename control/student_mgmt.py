from model.mongodb import conn_mongodb
from flask_login import UserMixin

class Student():
    def __init__(self,id,hashed_pw,account,full_name,phone_num,father_phone_num,mother_phone_num,student_course):
        self.id=id
        self.pw = hashed_pw
        self.account = account
        self.full_name = full_name
        self.phone_num = phone_num
        self.fatehr_phone_num = father_phone_num
        self.mother_phone_num = mother_phone_num
        self.student_course = student_course
        