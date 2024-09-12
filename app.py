from flask import Flask, request, url_for, render_template
import os
from models import common_import_modules


currentDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(currentDir,'testDB.sqlite3')

@app.route('/')
def test():
    return "<h1>This is a Sample Heading </h1>"

if __name__ == '__main__':
    app.run(debug = True)

