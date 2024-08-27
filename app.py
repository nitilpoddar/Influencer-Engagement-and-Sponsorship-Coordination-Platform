import os
from datetime import datetime
from flask import Flask, render_template
from controllers.user_blueprint_test import bp as user_bp

app = Flask(__name__)


#finding the path for the database file and configuring the app database URI
dbdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(dbdir,'testdb.sqlite3')
app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{dbfile}'

app.register_blueprint(user_bp)

#A sample home page route to test if the flask app is working fine

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', current_time=datetime.now())


if __name__ == '__main__':
    app.run(debug=True)