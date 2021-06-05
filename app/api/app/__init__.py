"""Flask example"""
from flask import Flask

def create_app(cfg_file='config.json'):
    """
    Function crseate Flask app object from cfongig file

    Args:
    cfg_file(str): path to config file
    
    Returns(obj): Flask app object
    """
    app = Flask(__name__)
    app.config.from_json(cfg_file)


    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/v1')
    
    return app