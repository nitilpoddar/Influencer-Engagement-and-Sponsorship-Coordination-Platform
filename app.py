from flask import Flask, request, url_for, render_template
import os
from models import *


currentDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(currentDir,'testDB.sqlite3')
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def test():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)

