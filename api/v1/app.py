#!/usr/bin/python3
"""Server file"""

# Import necessary modules
import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

# Create a Flask app instance
app = Flask(__name__)

# Retrieve environment variables or set default values for app host and port
app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', '5000'))

# Disable strict slashes in URLs
app.url_map.strict_slashes = False

# Register the blueprint containing API views
app.register_blueprint(app_views)

# Enable Cross-Origin Resource Sharing (CORS) for the app
CORS(app, resources={r"/*": {"origin": app_host}})

# Define a function to be called when the Flask app context torn down


@app.teardown_appcontext
def teardown_flask(exception):
    storage.close()

# Define a custom error handler for HTTP 404


@app.errorhandler(404)
def error_404(error):
    return jsonify(error='Not Found'), 404

# Define a custom error handler for HTTP 400


@app.errorhandler(400)
def error_400(error):
    msg = 'bad request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        msg = error.description
    return jsonify(error=msg), 400


# Start the Flask app if the script is run directly
if __name__ == "__main__":
    app.run(host=app_host, port=app_port, threaded=True)
