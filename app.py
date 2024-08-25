from flask import Flask, request, redirect, render_template,url_for
import os
from flask_sqlalchemy import SQLAlchemy, session

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

databasedir = os.path.join(basedir,'testdb.sqlite3')


# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{databasedir}'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Define a route
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/create_user', methods=['POST'])
def createUser():
    username = request.form.get('username')
    email = request.form.get('email')
    

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/showusers', methods=['GET'])
def showuser():
    users = User.query.all()
    return render_template('viewUser.html', users=users)

if __name__ == '__main__':
    # Create all the tables
    with app.app_context():
        db.create_all()

    # Run the app
    app.run(debug=True)
