from model.mongodb import conn_mongodb

class Course():
    def __init__(self,grade,section,batch,subject_id,teacher_id, student_id):
        self.grade = grade
        self.section = section
        self.batch = batch
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.student_id = student_id