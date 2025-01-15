from flask import Flask
from app.routes.avatar import avatar_bp
from app.routes.home import home_bp

def create_app():
    """
    Initialize the Flask application and register the blueprints
    """
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Register blueprints 
    app.register_blueprint(home_bp)
    app.register_blueprint(avatar_bp)

    return app 