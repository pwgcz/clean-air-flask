from flask import Blueprint


send_static = Blueprint("send_static", __name__)

from . import url
