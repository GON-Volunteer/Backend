from model.mongodb import conn_mongodb

class Course():
    def __init__(self,grade,section,batch,subject,is_elective_subject):
        self.grade = grade
        self.section = section
        self.batch = batch
        self.subject = subject
        self.is_elective_subject = is_elective_subject