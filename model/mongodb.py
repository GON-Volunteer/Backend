import pymongo
from pymongo import MongoClient

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient('mongodb://%s'%(MONGO_HOST)) #localhost로 연결설정

#cladatabase collection 생성

def make_collection():
    MONGO_HOST = 'localhost'
    MONGO_CONN = pymongo.MongoClient('mongodb://%s'%(MONGO_HOST))
    cla_db = MONGO_CONN.cla_db
    cla_collection = cla_db.cla_collection
    
#Mongodb 연결확인 함수
def conn_mongodb():
    try:
        MONGO_CONN.admin.command('ismaster')
        cla_collection = MONGO_CONN.cla_db.cla_collection
    except:
        MONGO_CONN = pymongo.MongoClient('mongodb://%s'%(MONGO_HOST))
        cla_collection = MONGO_CONN.cla_db.cla_collection
    return cla_collection