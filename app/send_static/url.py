from flask import current_app
from . import send_static


@send_static.route('/')
def index():
    return current_app.send_static_file('index.html')
