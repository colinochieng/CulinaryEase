#!/usr/bin/python3
"""
For valid interactions between user and request
registring new user and creating new fields
"""
from schema.address import Address
from app.Ver1.api import blueprint
from datetime import datetime
from schema.database.data_storage import storage
from flask import request, abort, jsonify, make_response, render_template
import re
from schema.users import User


user_required = {'username': 'required',
                 'email': 'required',
                 "password": 'required', 
                 'bios': 'required'}

address_required = {'city': 'required',
                 'state': 'required',
                 'country': 'required'}


def valid_email(email):
    """
    email: user email
    checks if valid
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


@blueprint.route('/register', methods=['POST'])
def register():
    """
    registers new user
    """
    storage.restart()
    if request.is_json:
        data = request.json

        missing_for_user = [key for key in user_required if key not in data]
        missing_for_address = [key for key in address_required if key not in data]
        
        if len(missing_for_user) > 0 or len(missing_for_address) > 0:
            return make_response(jsonify({"All": 'Note all the fields listed are required execept this' ,**user_required, **address_required}), 400)
        
        for key, value in data.items():
            if value.isspace() or value.__len__() == 0:
                return abort(400, f'{key} cannot be empty')

        if not valid_email(data.get("email")):
            abort(400, "invalid email")

        # check if user exists
        get_user = storage.get_user_by_email(data.get('email').lower())

        if get_user:
            return make_response('Account with the email already exist', 406)
        else:
            get_user = storage.get_user_by_uname(data.get('username').lower())

            if get_user:
                return make_response('Account with the username already exist', 409)
    
        user = User()
        address = Address()

        for key, value in data.items():
            if key in user_required:
                if key == 'password':
                    user.set_passwd(value)
                elif key == 'email' or key == 'username':
                    setattr(user, key, value.lower())
                else:
                    setattr(user, key, re.sub(r'\s+', ' ', value))
            else:
                address.__setattr__(key, value)
        
        user.addresses.append(address)

        storage.new(user)
        storage.save()
        return make_response(jsonify({'Account': "creation complete"}), 200)
    else:
        return make_response({'status': 'fail', 'message': 'Only JSON'}, 400)


@blueprint.route('/user/<username>/profile')
def user_profile(username=None):
    """
    Returns user bios
    """
    storage.restart()
    if username:
        user = storage.get_user_by_uname(username.lower())
        
        if user:
            user_data = {
                "username": user.username.capitalize(),
                "id": user.id,
                "bios": user.bios,
                "email": user.email,
                "addresses": user.addresses[0].to_dict()
            }
            return make_response(user_data, 200)
        else:
            response = {"message": "No user with the username given", 'status': 'fail'}
            return make_response(response, 400)
    else:
        abort(400)

@blueprint.route('/user/update/<username>/<passcode>', methods=['PUT'])
def update_user(username, passcode):
    """
    updates user data
    """
    user = storage.get_user_by_uname(username.lower())
    check_if_account_exists = None

    if user:
        if user.check_password(passcode):
            if request.is_json:

                if len(request.json) == 0:
                    return make_response({'status': 'fail', 'message': 'no data provided'}, 400)

                for key, value, in request.json.items():
                    if key == 'email' or key == 'username' or key == 'bios':
                        if value.isspace() or value.__len__() == 0:
                            return abort(400, f'{key} cannot be empty')
                        if key == 'email':
                            if not valid_email(value):
                                return jsonify({'Account cannot be updated': 'Invalid: email'}), 203
                            
                            check_if_account_exists = storage.get_user_by_email(value.lower())

                            if  check_if_account_exists:
                                return jsonify({'Request Failed': 'Account with the email exists'}), 403
                        elif key == 'bios':
                            value = re.sub(r"\s+", ' ', value)
                        elif key == 'username':
                            check_if_account_exists = storage.get_user_by_uname(value.lower())

                            if  check_if_account_exists:
                                return jsonify({'Request Failed': 'Account with the username exists'}), 403

                        if key == 'email' or key == 'username':
                            user.__setattr__(key, value.lower())
                        else:
                            user.__setattr__(key, value)
                        user.updated_at = datetime.now()
                        storage.save()

                        return make_response(jsonify({'status': 'success', 'message': 'update successful'}), 200)
            else:
                return make_response({'status': 'fail', 'message': 'Only JSON'}, 400)
        else:
            return jsonify({'status': 'fail', 'message': 'Invalid passcode'})                
                            
    else:
        return {'status': 'fail', 'message': 'No user with such a username'}


@blueprint.route('/user/change-password', methods=['PUT'])
def change():
    '''
    Allow users to change their account password.
    '''
    response = make_response({'status': 'fail', 'message': 'Invalid Username'}, 400)
    required = ['new_password', 'old_password', 'username']

    if request.is_json:
        for key, value, in request.json.items():
            if key == 'old_password' or key == 'username' or key == 'new_password':
                if value.isspace() or value.__len__() == 0:
                    return abort(400, f'{key} cannot be empty')
                if key == 'new_password':
                    new_value = re.sub(r'\s+', '', value)
                    if len(value) < 8 or len(value) > len(new_value):
                        return make_response({'status': 'fail', 'message':
                                              "length less than 8 or password with white spaces"})
        
        lacking_data = [key for key in required if key not in  request.json]
        print(request.json)
        if lacking_data.__len__() > 0:
            return make_response({'status': 'fail', 'message':
                                              f"Lacking data {lacking_data}"})

        username = request.json.get('username', None)
        password = request.json.get('old_password', None)
        new_password = request.json.get('new_password', None)

        if username:
            user = storage.get_user_by_uname(username.lower())

            if user:
                if user.check_password(password):
                    user.set_passwd(new_password)
                    storage.save()
                    return make_response(jsonify({'status': 'success', 'message':
                                                  'Password updated successfully'}), 200)
                else:
                    return make_response({'status': 'fail', 'message':
                                          'Incorrect old password'}, 401)
            else:
                return response
        else:
            return response
    else:
        return make_response({'status': 'fail', 'message': 'Only JSON'}, 400)


@blueprint.route('/user/delete', methods=['DELETE'])
def remove_account():
    """
    deletes user account
    """
    if request.is_json:
        for key, value in request.json.items():
            if key == 'username' or key == 'password':
                if value.isspace() or value.__len__() == 0:
                    return abort(400, f'{key} cannot be empty')
                username = request.json.get('username')
                password = request.json.get('password')

                user = storage.get_user_by_uname(username.lower())

                if user:
                    if user.check_password(password):
                        storage.delete(user)
                        storage.save()
                        return jsonify({"status": 'success',
                                        'message': 'Account deleted successfully'})
                    else:
                        return jsonify({"status": 'fails',
                                        'message': 'Invalid password'})
    else:
        return make_response({'status': 'fail', 'message': 'Only JSON'}, 400)
