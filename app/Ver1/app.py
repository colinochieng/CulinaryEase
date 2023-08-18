#!/usr/bin/python3

from flask import Flask, render_template, request, url_for
from app.Ver1.views import scheme

app = Flask(__name__, template_folder='templates', static_folder='static')
app.url_map.strict_slashes = True
app.register_blueprint(scheme)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission here
        username = request.form['username']
        email = request.form['email']
        message = request.form['message']
        # Do something with the form data, e.g., store it in a database, send an email, etc.
        return f"Thank you, {username}, for your {message}!"
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)