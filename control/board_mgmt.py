from model.mongodb import conn_mongodb

class Board():
    def __init__(self,title,no,publish_date,content,board_course):
        self.title = title
        self.no = no
        self.publish_date = publish_date
        self.content = content
        self.board_course = board_course
    

