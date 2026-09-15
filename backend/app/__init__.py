from flask import Flask

from app.routes.description import descripcion_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(descripcion_bp)
    # app.register_blueprint(descripcion_bp)
    return app