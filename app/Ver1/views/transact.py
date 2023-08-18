from app.Ver1.views import scheme
from flask import render_template, request
from flask import jsonify

@scheme.route('/status')
def status():
    return jsonify({'Status': 'ok'})

@scheme.route('/login')
def login():
    return render_template('login.html')
