#!/usr/bin/python3
from flask import render_template, request, jsonify
from app.Ver1.views import scheme
from schema.users import User
from schema.database.data_storage import storage


@scheme.route('/about_page')
def about():
    return render_template('about.html')