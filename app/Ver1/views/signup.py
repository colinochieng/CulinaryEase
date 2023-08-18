#!/usr/bin/python3
from flask import render_template, request, jsonify
from app.Ver1.views import scheme
from schema.user import User
from schema.database.data_storage import storage



@scheme.route('/sign_up')
def sign_up():
    return render_template('forms.html')

@scheme.route('/handle_form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        if storage.get_user_by_email(User, request.form.get('email')):
            return jsonify({'error': 'the email already has account'})
        new = User()
        new.email = request.form.get('email')
        new.first_name = request.form.get('first_name')
        new.surname = request.form.get('surname')
        new.password = request.form.get('password')
        storage.new(new)
        storage.save()
        return new.to_dict()
    return None