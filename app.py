from flask import Flask, jsonify, request, make_response, session
from flask_login import LoginManager,current_user, login_required,login_user, logout_user
from flask_cors import CORS
from view import login,student,access_check,teacher,pwchange,subject

from model.mongodb import make_board_collection, make_course_collection, make_student_collection, make_subject_collection, make_teacher_collection
#from blog_control.user_mgmt import User
import os

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
CORS(app)

make_board_collection()
make_course_collection()
make_teacher_collection()
make_student_collection()
make_subject_collection()

#보안을 위해서는 서버를 끄고 켤때마다 다른값으로 해야하는데 그렇게하면 그동안 설정된 세션이 모두 사라진다.
app.secret_key = 'dave_server3'#session 생성시 이 앱만의 secret key

app.register_blueprint(login.user_login, url_prefix = '/api/login')
app.register_blueprint(student.student, url_prefix = '/api/students')
app.register_blueprint(access_check.access_check, url_prefix = '/api/auth')
app.register_blueprint(subject.subject, url_prefix = '/api/subjects')
app.register_blueprint(teacher.teacher, url_prefix = '/api/teachers')
app.register_blueprint(pwchange.password_change, url_prefix = '/api/password')

@app.route('/')
def home():
    return "hello flask"

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)
