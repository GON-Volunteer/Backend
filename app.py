from flask import Flask, jsonify, request, make_response, session
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_cors import CORS
from view import login, student, access_check, teacher, pwchange, subject, course
from control import board_mgmt, comment_mgmt, course_board_mgmt, course_comment_mgmt
from model.mongodb import (
    make_board_collection,
    make_comment_collection,
    make_course_board_collection,
    make_course_comment_collection,
    make_course_collection,
    make_student_collection,
    make_subject_collection,
    make_teacher_collection,
)

# Test 나중에 지우삼
from model.mongodb import conn_mongodb
import bcrypt

# from blog_control.user_mgmt import User
import os

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)
CORS(app)


# TEST 나중에 지우삼
mongo_db = conn_mongodb()
pw = "1234"
hashed_pw = bcrypt.hashpw(pw.encode("UTF-8"), bcrypt.gensalt())
mongo_db.teacher.insert_one(
    {
        "id": "tgool",
        "hashed_pw": hashed_pw,
        "account": 0,
        "s_n": "test",
        "full_name": "taejin king",
        "phone_num": "01020032003",
        "father_phone_num": "00700",
        "mother_phone_num": "119",
        "guardians_phone_num": "5252",
    }
)

pw2 = "1234"
hashed_pw2 = bcrypt.hashpw(pw2.encode("UTF-8"), bcrypt.gensalt())
mongo_db.student.insert_one(
    {
        "id": "tgool2",
        "hashed_pw": hashed_pw2,
        "account": 2,
        "s_n": "test",
        "full_name": "taejin student",
        "phone_num": "01020032003",
        "father_phone_num": "00700",
        "mother_phone_num": "119",
        "guardians_phone_num": "5252",
    }
)

make_board_collection()
make_comment_collection()
make_course_board_collection()
make_course_comment_collection()
make_course_collection()
make_teacher_collection()
make_student_collection()
make_subject_collection()

# 보안을 위해서는 서버를 끄고 켤때마다 다른값으로 해야하는데 그렇게하면 그동안 설정된 세션이 모두 사라진다.
app.secret_key = "dave_server3"  # session 생성시 이 앱만의 secret key

# app.register_blueprint(sign_up.user_sign_up, url_prefix="/signup")

app.register_blueprint(board_mgmt.board, url_prefix="/api/articles")
app.register_blueprint(comment_mgmt.comment, url_prefix="/api/comment")
app.register_blueprint(
    course_board_mgmt.course_board, url_prefix="/api/courses/<string:coidx>/articles"
)
app.register_blueprint(
    course_comment_mgmt.course_comment, url_prefix="/api/courses/<string:coidx>/comment"
)
app.register_blueprint(login.user_login, url_prefix="/api/login")
app.register_blueprint(student.student, url_prefix="/api/students")
app.register_blueprint(access_check.access_check, url_prefix="/api/auth")
app.register_blueprint(subject.subject, url_prefix="/api/subjects")
app.register_blueprint(teacher.teacher, url_prefix="/api/teachers")
app.register_blueprint(course.course, url_prefix="/api/courses")
app.register_blueprint(pwchange.password_change, url_prefix="/api/password")


@app.route("/")
def home():
    return "hello flask"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
