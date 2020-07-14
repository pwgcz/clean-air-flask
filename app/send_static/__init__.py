import os

from flask import Blueprint

static_folder = os.path.join(os.pardir, 'build')
send_static = Blueprint("send_static", __name__, static_folder=static_folder, static_url_path='/')
print(static_folder)
from . import url
