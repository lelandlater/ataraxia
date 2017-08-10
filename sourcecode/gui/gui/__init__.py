from flask import Flask

def create_app(cfg=None):

    app = Flask(__name__)

    if cfg is None:
	    pass
    else:
	    app.config.from_pyfile(cfg)

    from . import views

    app.route('/')(views.index)
    app.route('/contact')(views.contact)
    app.route('/todo')(views.info)

    return app
