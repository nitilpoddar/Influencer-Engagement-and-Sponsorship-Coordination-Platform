import os
from flask import Flask, render_template

dbdir = os.path.abspath(os.path.dirname(__file__))

dbfile = os.path.join(dbdir,'testdb.sqlite3')

app = Flask(__name__)

app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{dbfile}'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)