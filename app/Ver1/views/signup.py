#!/usr/bin/python3
from schema.address import Address
import os
import re
from flask import redirect, render_template, request
from app.Ver1.views import scheme
from werkzeug.utils import secure_filename
from schema.database.data_storage import storage
from schema.users import User



UPLOAD_FOLDER = 'app/Ver1/static/artists/repository'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_files(filename):
    """
    validates if the file sent is a valid image source file
    """
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_upload_folder_if_not_exists(username):
    """
    create folder if it does not exist
    """
    upload_folder = f'{UPLOAD_FOLDER}/{username}'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)


@scheme.route('/handle_form', methods=['GET', 'POST'])
def handle_form():
    """
    Accept method post
    sets user address, and creates a new user account
    Handles the profile picture the user sets
    """
    if request.method == 'POST':        
        new_user = User()
        new_address = Address()

        for key, value in request.form.items():
            if key == 'state' or key == 'country' or key == 'city':
                new_address.__setattr__(key, value.capitalize())
            else:
                if key == 'password':
                    new_user.set_passwd(value)
                elif key == 'profile_picture':
                    pass
                elif key == 'bios':
                    new_bios = re.sub(r'\s+', ' ', key)
                    setattr(new_user, key, new_bios)
                else:
                    new_user.__setattr__(key, value.lower())

        if 'profile_picture' in request.files:
            file = request.files.get('profile_picture')
            if file and allowed_files(file.filename):
                filename = 'profile.' + secure_filename(file.filename).rsplit('.', 1)[1]

                create_upload_folder_if_not_exists(new_user.username)
                file.save(os.path.join(UPLOAD_FOLDER, new_user.username, filename))

                new_user.profile_picture = f'{UPLOAD_FOLDER}/{new_user.username}/{filename}'
        
        new_user.addresses.append(new_address)

        storage.new(new_user)
        
        storage.save()

        return request.form

    elif request.method == "GET":
        return redirect('/', 302)
