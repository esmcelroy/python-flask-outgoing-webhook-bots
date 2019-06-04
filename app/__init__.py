from flask import Flask, jsonify, request



def create_app():
    """Create an application instance."""
    app = Flask(__name__)

    # apply configuration
    #cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    #app.config.from_pyfile(cfg)

    # register blueprints

    from .endpoints import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
