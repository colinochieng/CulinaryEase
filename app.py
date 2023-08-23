from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('profile_form.html')

@app.route('/submit_profile', methods=['POST'])
def submit_profile():
    profile_picture = request.files['profile_picture']
    bio = request.form['bio']
    
    # Process the profile picture and bio (store them, etc.)
    # For simplicity, let's just print them here.
    print("Profile Picture:", profile_picture.filename)
    print("Bio:", bio)
    
    return "Profile submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request
import boto3
import os
import uuid

app = Flask(__name__)

s3 = boto3.client(
    's3',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

BUCKET_NAME = 'your-bucket-name'

@app.route('/')
def index():
    return render_template('profile_form.html')

@app.route('/submit_profile', methods=['POST'])
def submit_profile():
    profile_picture = request.files['profile_picture']
    bio = request.form['bio']

    # Generate a unique filename
    unique_filename = str(uuid.uuid4()) + '.' + profile_picture.filename.split('.')[-1]
    
    # Upload the image to S3
    s3.upload_fileobj(profile_picture, BUCKET_NAME, unique_filename)
    
    # Store metadata in the database (you'd need to set up your database)
    # Here, we're just printing for demonstration
    print("Profile Picture:", unique_filename)
    print("Bio:", bio)

    return "Profile submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
