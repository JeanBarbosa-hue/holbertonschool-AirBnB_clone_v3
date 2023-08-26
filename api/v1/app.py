#!/usr/bin/python3
"""Server file"""
from api.v1.views import app_views
from flask import Flask
from models import storage
"""Status route on app_views"""

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', 5000)),
            threaded=True)

app = Flask(__name__)

app.register_blueprint(app_views)
