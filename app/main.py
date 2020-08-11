from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/me")
def me_api():
    return {
        "username": 'test',
        "theme": 'theme',
        "image": 'image',
    }