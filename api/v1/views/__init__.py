#!/usr/bin/python3
"""Contains the API blueprint"""

from flask import Blueprint

# Create the blueprint instance
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import to include in blueprint
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
