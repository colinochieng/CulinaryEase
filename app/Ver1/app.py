#!/usr/bin/python3
from app.Ver1.api import blueprint
from flask_cors import CORS, cross_origin
from flask import jsonify, redirect
from flask import Flask, make_response, render_template, request
from app.Ver1.views import scheme
from schema.database.data_storage import storage
from datetime import timedelta


app = Flask(__name__, template_folder='templates', static_folder='static')
app.url_map.strict_slashes = False
# app.secret_key = 'pepperease'
app.config['SECRET_KEY'] = 'pepperease'
# app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.permanent_session_lifetime = timedelta(days=7)
print(app.static_folder)

app.register_blueprint(scheme)
app.register_blueprint(blueprint)
CORS(app)
storage.restart()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', recipe_url='/recipe/123')


@app.route('/usernames', methods=['POST'])
@cross_origin(origins="http://192.168.0.13:5000/")
def check_if_username_or_email_exists():
    user_by_email = None
    user_by_uname = None
    data = request.json
    username = data.get("username")
    email = data.get("email")

    if username:
        user_by_uname = storage.get_user_by_uname(username)

    if email:
        user_by_email = storage.get_user_by_email(email)

    archive = {}

    if user_by_uname:
        archive.update({"username": user_by_uname.username})
    else:
        archive.update({"username": None})
    if user_by_email:
        archive.update({"email": user_by_email.email})
    else:
        archive.update({"email": None})

    return jsonify(archive), 200

@app.route('/logcheck', methods=['POST'])
@cross_origin(origins="http://192.168.0.13:5000/")
def logcheck():
    """
    verify user email and password
    """
    email = request.json.get("email")
    password = request.json.get("password")

    if email:
        user = storage.get_user_by_email(email)

        if not user:
            return jsonify({'email': False}), 200
        else:
            valid = user.check_password(password)

            if valid:
                data = {"email": True}
                return make_response(jsonify(data), 200)
            else:
                response = make_response("Invalid password", 404)
                response.headers.update({'Content-Type': "text/plain"})
                return response
    else:
        response = make_response("Invalid email", 404)
        response.headers.update({'Content-Type': "text/plain"})
        return response


@app.teardown_request
def close_app(error=None):
    """
    close database connection
    """
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)