import os
from flask_bootstrap import Bootstrap5
from flask import Flask, request, jsonify, render_template
import app.views
import app.homepage
from wsgiref.simple_server import make_server


def create_app():
    myapp = Flask(__name__)
    bootstrap = Bootstrap5(myapp)

    from . import views
    myapp.register_blueprint(views.bp)

    from . import homepage
    myapp.register_blueprint(homepage.bp)

    from . import file
    myapp.register_blueprint(file.bp)


    return myapp


port = int(os.environ.get('SERVER_PORT', 8080))
env = os.environ.get('APP_ENV', 'dev')
app = create_app()
if env == 'dev':
    app.run(host='0.0.0.0', port=port, debug=True)
else:
    with make_server('', port, app) as httpd:
        print("Serving on port " + str(port) + "...")
        httpd.serve_forever()
