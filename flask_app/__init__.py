from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.abspath("uploads")
    app.config['OUTPUT_FOLDER'] = os.path.abspath("output")
    app.secret_key = "your-very-secret-key"  # Replace or load from env

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

    from .routes import main
    app.register_blueprint(main)

    return app