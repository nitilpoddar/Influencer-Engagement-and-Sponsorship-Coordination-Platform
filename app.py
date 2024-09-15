from flask import Flask, render_template
import os
from models import db  # Import db from models
from blueprints.createUser import createUser  # Import blueprint

currentDir = os.path.abspath(os.path.dirname(__file__))

# Create Flask app
app = Flask(__name__)

# Register blueprint
app.register_blueprint(createUser)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(currentDir, 'testDB.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the db with the app
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# Test route
@app.route('/')
def test():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
