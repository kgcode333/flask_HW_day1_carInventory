from functools import wraps
import secrets


from flask import request, jsonify

from lux_inventory.models import Drone, User

#Token required decorator for protected API Routes
def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']