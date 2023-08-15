from flask import Flask, Blueprint, request, make_response, jsonify, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
import datetime
import bcrypt
import jwt
import json
from control.teacher_mgmt import Teacher
from model.mongodb import conn_mongodb
from control.student_mgmt import Student
from control.subject_mgmt import Subject
from control.course_mgmt import Course
from bson import ObjectId

course = Blueprint('courses', __name__)  # blueprint 객체 생성

mongo_db = conn_mongodb()

# create update read delete

@course.route('/', methods=['POST'])
def create_course():
    new_course = request.get_json()
    # {
    #     "grade": "grade",
    #     "section": "section",
    #     "batch": "batch",
    #     "subject_id": "subject_id"
    # }
    grade = new_course['grade']
    section = new_course['section']
    batch = new_course['batch']
    subject_id = new_course['subject_id']


    if Course.check_is_unique(grade, section,batch,subject_id):
        Course.add_course(grade,section,batch,subject_id)
        return jsonify({
            "code": "200"
        })

    else:
        return jsonify({
            "code": "400",
            "message": "동일한 course가 존재합니다."
        })

#
# @course.route('/', methods=['GET'])
# def read_courses():
#     print("enter in read_courses")

# @subject.route('/', methods=['GET'])
# def read_subjects():
#     print("enter in read_subjects()")
#     json_subject_list = Subject.get_subjects()
#
#     return jsonify(json_subject_list)
#
#
# @subject.route('/<subject_id>', methods=['DELETE'])
# def delete_subject(subject_id):
#     print("enter in delete_subjects()")
#     result_message = Subject.delete_subject(subject_id)
#     Course.delete_subject(subject_id)
#
#     return jsonify({'code': "200"})



