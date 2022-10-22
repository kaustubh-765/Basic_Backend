from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = '314WER'

    return app