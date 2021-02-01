from flask import Flask


def  create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'azertyuiop1234567890'

    return app