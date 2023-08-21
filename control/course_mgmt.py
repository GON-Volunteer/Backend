from model.mongodb import conn_mongodb
from bson import ObjectId


class Course:
    def __init__(self, grade, section, batch, subject_id, teacher_id, student_id):
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
            {"subject_id": obj_id}, {"$unset": {"subject_id": ""}}
        )

        # print(f"{result.modified_count} documents updated and subject_id removed.")

    def check_is_unique(grade, section, batch, subject_id):
        query = {
            "grade": grade,
            "section": section,
            "batch": batch,
            "subject_id": subject_id,
        }
        mongo_db = conn_mongodb()
        matching_course = mongo_db.course.count_documents(query)

        if matching_course > 0:
            print("같은 course가 이미 존재합니다")
            return False
        else:
            print("같은 course는 아직 존재하지 않습니다")
            return True

    def add_course(grade, section, batch, subject_id):
        print("enter add_course in Course class")
        mongo_db = conn_mongodb()
        mongo_db.course.insert_one(
            {
                "grade": grade,
                "section": section,
                "batch": batch,
                "subject_id": subject_id,
            }
        )

    def get_courses():
        print("enter get_courses in Course class")
        mongo_db = conn_mongodb()
        courses = mongo_db.course.find()
        course_list = []
        for course in courses:
            # print(course)
            course["_id"] = str(course["_id"])
            if "subject_id" in course:  # 'subject_id' 키가 있는지 확인
                subject_id = course["subject_id"]
                # print(f"subject_id:{subject_id}")
                subject_cursor = mongo_db.subject.find({"_id": ObjectId(subject_id)})

                for subject_document in subject_cursor:
                    # print("subject_document",subject_document)

                    subject_name = subject_document["name"]
                    is_elective_subject = subject_document["is_elective_subject"]
                    course["subject_name"] = subject_name
                    course["is_elective_subject"] = is_elective_subject

                course["subject_id"] = str(course["subject_id"])
                # print(f"modified course{course}")
                course_list.append(course)

            else:
                # print("'subject_id' key not found in course:", course)
                course_list.append(course)

        return course_list

    def delete_course(course_id):
        mongo_db = conn_mongodb()
        course_id = ObjectId(course_id)
        result = mongo_db.course.delete_one({"_id": course_id})
        if result.deleted_count == 1:
            return f"subject doucument with _id {course_id} deleted successfully"

    def delete_courses():
        mongo_db = conn_mongodb()
        result = mongo_db.course.delete_many({})

        return f"삭제된 문서 수: {result.deleted_count}"
