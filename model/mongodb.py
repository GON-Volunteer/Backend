import pymongo
from pymongo import MongoClient

MONGO_HOST = "localhost"
MONGO_CONN = pymongo.MongoClient("mongodb://%s" % (MONGO_HOST))  # localhost로 연결설정

# cladatabase collection 생성


def make_board_collection():
    MONGO_HOST = "localhost"
    MONGO_CONN = pymongo.MongoClient("mongodb://%s" % (MONGO_HOST))
    cla_db = MONGO_CONN.cla_db
    board_collection = cla_db.board_collection


def make_comment_collection():
    MONGO_HOST = "localhost"
    MONGO_CONN = pymongo.MongoClient("mongodb://%s" % (MONGO_HOST))
    cla_db = MONGO_CONN.cla_db
    comment_collection = cla_db.board_collection


def make_course_collection():
    MONGO_HOST = "localhost"
    MONGO_CONN = pymongo.MongoClient("mongodb://%s" % (MONGO_HOST))
    cla_db = MONGO_CONN.cla_db
    course_collection = cla_db.course_collection


def make_teacher_collection():
    MONGO_HOST = "localhost"
    MONGO_CONN = pymongo.MongoClient("mongodb://%s" % (MONGO_HOST))
    cla_db = MONGO_CONN.cla_db
    teacher_collection = cla_db.teacher_collection


def make_student_collection():
    MONGO_HOST = "localhost"
    MONGO_CONN = pymongo.MongoClient("mongodb://%s" % (MONGO_HOST))
    cla_db = MONGO_CONN.cla_db
    student_collection = cla_db.student_collection


def make_subject_collection():
    MONGO_HOST = "localhost"
    MONGO_CONN = pymongo.MongoClient("mongodb://%s" % (MONGO_HOST))
    cla_db = MONGO_CONN.cla_db
    subject_collection = cla_db.subject_collection


# Mongodb 연결확인 함수
def conn_mongodb():
    try:
        MONGO_CONN.admin.command("ismaster")
        cla_db = MONGO_CONN.cla_db
    except:
        MONGO_CONN = pymongo.MongoClient("mongodb://%s" % (MONGO_HOST))
        cla_db = MONGO_CONN.cla_db
    return cla_db
