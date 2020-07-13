from flask import Blueprint
from flask_restful import Api

pollination_api = Blueprint("pollination_api", __name__)
api = Api(pollination_api)

from . import endpoints
