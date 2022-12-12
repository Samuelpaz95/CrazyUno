import os
from flask import Flask
from flask_migrate import Migrate
from config import Config
from .models import db
from .game import game_resource

migrate = Migrate(db=db)

def create_app(config=Config):
    template_dir = os.path.abspath('app/templates')
    print(template_dir)
    app = Flask(__name__, template_folder=template_dir)
    app.config.from_object(Config)

    # database initialization
    db.init_app(app)
    migrate.init_app(app)
    # resource initializacion
    app.register_blueprint(game_resource)
    return app
