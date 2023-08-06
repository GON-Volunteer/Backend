from flask import Flask, jsonify, request, make_response, session
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_cors import CORS
from view import sign_up, login
from model.mongodb import make_collection

# from blog_control.user_mgmt import User
import os

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)
CORS(app)

make_collection()

# 보안을 위해서는 서버를 끄고 켤때마다 다른값으로 해야하는데 그렇게하면 그동안 설정된 세션이 모두 사라진다.
app.secret_key = "dave_server3"  # session 생성시 이 앱만의 secret key

app.register_blueprint(sign_up.user_sign_up, url_prefix="/signup")
app.register_blueprint(login.user_login, url_prefix="/api/login")


@app.route("/")
def home():
    return "hello flask"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
