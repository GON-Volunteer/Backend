from model.mongodb import conn_mongodb
class Subject():
    def __init__(self,name,is_elective_subject):
        self.name = name
        self.is_elective_subject = is_elective_subject

        
    