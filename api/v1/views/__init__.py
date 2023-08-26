#!/usr/bin/python3
"""Contains the API blueprint"""

# Import the necessary modules
from flask import Blueprint

# Create the blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
