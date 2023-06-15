from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1gh2gh3gh'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pikininiscienceapp.db'

    
    db.init_app(app)

    # Import and register blueprints
    from .views import views
    app.register_blueprint(views)

    return app
