from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import ProductionConfig, DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
cr = CORS()
ma = Marshmallow()


def create_app():
    app = Flask(__name__, static_folder='./build', static_url_path='/')

    app.config.from_object(ProductionConfig)

    cr.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)

    @app.route('/')
    def index():
        
        return'index.html'

    from .pollination_api import pollination_api as pollination_api_blueprint
    app.register_blueprint(pollination_api_blueprint)

    return app
