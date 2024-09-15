from flask import Blueprint, redirect, url_for, render_template, request
from models.user import User  # Import the User model
from models import db  # Import the db instance

# Define the blueprint
createUser = Blueprint('createUser', __name__)

@createUser.route('/createUser', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')
    
    # Handle POST request (form submission)
    else:
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Create new user instance
        new_user = User(name=name, email=email, password=password, username=username)

        # Add user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('test'))
