from model.mongodb import conn_mongodb
from bson import ObjectId

class Course():
    def __init__(self,grade,section,batch,subject_id,teacher_id, student_id):
        self.grade = grade
        self.section = section
        self.batch = batch
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.student_id = student_id

    def delete_subject(subject_id):
        # Convert subject_id to ObjectId
        mongo_db = conn_mongodb()
        print("enter into delete_subject in course_mgmt.py")
        obj_id = ObjectId(subject_id)
        print(f"obj_id is {obj_id}")

        # Update documents with matching subject_id and remove subject_id field
        result = mongo_db.course.update_many(
            {"subject_id": obj_id},
            {"$unset": {"subject_id": ""}}
        )

        # print(f"{result.modified_count} documents updated and subject_id removed.")

    def check_is_unique(grade, section,batch,subject_id):
        query={
            "grade":grade,
            "section":section,
            "batch":batch,
            "subject_id":subject_id
        }
        mongo_db = conn_mongodb()
        matching_course = mongo_db.course.count_documents(query)


        if matching_course>0 :
            print("같은 course가 이미 존재합니다")
            return False
        else:
            print("같은 course는 아직 존재하지 않습니다")
            return True

    def add_course(grade,section,batch,subject_id):
        print("enter course in Course class")
        mongo_db = conn_mongodb()
        mongo_db.course.insert_one({
            "grade": grade,
            "section": section,
            "batch":batch,
            "subject_id":subject_id
        })