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