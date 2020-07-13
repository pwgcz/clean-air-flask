import os
from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # postgresql: // username: password @ hostname / database
    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
    SERVER_NAME = 'https://clean-air-poland.herokuapp.com'


class DevelopmentConfig(Config):
    SECRET_KEY = 'djbavbarhvbadvb'
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
