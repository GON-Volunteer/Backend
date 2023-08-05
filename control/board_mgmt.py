from model.mongodb import conn_mongodb

class Board():
    def __init__(self,title,publish_date,course_id):
        self.title = title
        self.publish_date = publish_date
        self.course_id = course_id

